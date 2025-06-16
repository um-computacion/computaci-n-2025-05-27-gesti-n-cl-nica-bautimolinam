

from datetime import datetime
from modeloclinica import (
    Clinica, Paciente, Medico, Especialidad,
    PacienteNoEncontradoException,
    MedicoNoEncontradoException,
    MedicoNoDisponibleException,
    TurnoOcupadoException,
    RecetaInvalidaException,
    EspecialidadNoValidaException,
    PacienteDuplicadoException,
    MedicoDuplicadoException
)


class CLI:
    """Interfaz de consola para el sistema de gestión de la clínica"""
    
    def __init__(self):
        self.clinica = Clinica()
    
    def mostrar_menu(self):
        """Muestra el menú principal"""
        print("\n" + "="*50)
        print("         SISTEMA DE GESTIÓN - CLÍNICA")
        print("="*50)
        print("1) Agregar paciente")
        print("2) Agregar médico")
        print("3) Agregar especialidad a médico")
        print("4) Agendar turno")
        print("5) Emitir receta")
        print("6) Ver historia clínica")
        print("7) Ver todos los turnos")
        print("8) Ver todos los pacientes")
        print("9) Ver todos los médicos")
        print("0) Salir")
        print("="*50)
    
    def ejecutar(self):
        """Ejecuta el bucle principal de la aplicación"""
        print("¡Bienvenido al Sistema de Gestión de la Clínica!")
        
        while True:
            try:
                self.mostrar_menu()
                opcion = input("Seleccione una opción: ").strip()
                
                if opcion == "1":
                    self.agregar_paciente()
                elif opcion == "2":
                    self.agregar_medico()
                elif opcion == "3":
                    self.agregar_especialidad()
                elif opcion == "4":
                    self.agendar_turno()
                elif opcion == "5":
                    self.emitir_receta()
                elif opcion == "6":
                    self.ver_historia_clinica()
                elif opcion == "7":
                    self.ver_turnos()
                elif opcion == "8":
                    self.ver_pacientes()
                elif opcion == "9":
                    self.ver_medicos()
                elif opcion == "0":
                    print("¡Gracias!")
                    break
                else:
                    print("Opción inválida. Por favor, seleccione una opción del menú.")
                
                input("\nPresione Enter para continuar...")
                
            except KeyboardInterrupt:
                print("\n\n¡Hasta luego!")
                break
            except Exception as e:
                print(f"Error inesperado: {e}")
                input("\nPresione Enter para continuar...")
    
    def agregar_paciente(self):
        """Solicita datos y registra un nuevo paciente"""
        print("\n--- AGREGAR PACIENTE ---")
        try:
            nombre = input("Nombre completo: ").strip()
            dni = input("DNI: ").strip()
            fecha_nacimiento = input("Fecha de nacimiento (dd/mm/aaaa): ").strip()
            
            if not nombre or not dni or not fecha_nacimiento:
                print(" Todos los campos son obligatorios.")
                return
            
            paciente = Paciente(nombre, dni, fecha_nacimiento)
            self.clinica.agregar_paciente(paciente)
            print(f"Paciente {nombre} registrado exitosamente.")
            
        except PacienteDuplicadoException as e:
            print(f" {e}")
        except ValueError as e:
            print(f" Error en los datos: {e}")
        except Exception as e:
            print(f" Error inesperado: {e}")
    
    def agregar_medico(self):
        """Solicita datos y registra un nuevo médico"""
        print("\n--- AGREGAR MÉDICO ---")
        try:
            nombre = input("Nombre completo: ").strip()
            matricula = input("Matrícula: ").strip()
            
            if not nombre or not matricula:
                print(" Todos los campos son obligatorios.")
                return
            
            medico = Medico(nombre, matricula)
            self.clinica.agregar_medico(medico)
            print(f"Médico Dr. {nombre} registrado exitosamente.")
            
        except MedicoDuplicadoException as e:
            print(f" {e}")
        except ValueError as e:
            print(f" Error en los datos: {e}")
        except Exception as e:
            print(f" Error inesperado: {e}")
    
    def agregar_especialidad(self):
        """Agrega una especialidad a un médico existente"""
        print("\n--- AGREGAR ESPECIALIDAD ---")
        try:
            matricula = input("Matrícula del médico: ").strip()
            
            if not matricula:
                print(" La matrícula es obligatoria.")
                return
            
          
            medico = self.clinica.obtener_medico_por_matricula(matricula)
            
            tipo_especialidad = input("Tipo de especialidad: ").strip()
            if not tipo_especialidad:
                print(" El tipo de especialidad es obligatorio.")
                return
            
            print("Días de atención (separados por comas):")
            print("Ejemplo: lunes, miércoles, viernes")
            dias_input = input("Días: ").strip()
            
            if not dias_input:
                print(" Debe especificar al menos un día.")
                return
            
            dias = [dia.strip() for dia in dias_input.split(",")]
            
            especialidad = Especialidad(tipo_especialidad, dias)
            medico.agregar_especialidad(especialidad)
            
            print(f"Especialidad {tipo_especialidad} agregada exitosamente al Dr. {matricula}.")
            
        except MedicoNoEncontradoException as e:
            print(f" {e}")
        except ValueError as e:
            print(f" Error en los datos: {e}")
        except Exception as e:
            print(f" Error inesperado: {e}")
    
    def agendar_turno(self):
        """Agenda un nuevo turno"""
        print("\n--- AGENDAR TURNO ---")
        try:
            dni = input("DNI del paciente: ").strip()
            matricula = input("Matrícula del médico: ").strip()
            especialidad = input("Especialidad solicitada: ").strip()
            
            if not dni or not matricula or not especialidad:
                print(" Todos los campos son obligatorios.")
                return
            
            print("Fecha y hora del turno:")
            fecha_str = input("Fecha (dd/mm/aaaa): ").strip()
            hora_str = input("Hora (HH:MM): ").strip()
            
            if not fecha_str or not hora_str:
                print(" Fecha y hora son obligatorias.")
                return
            
            
            try:
                fecha_hora = datetime.strptime(f"{fecha_str} {hora_str}", "%d/%m/%Y %H:%M")
            except ValueError:
                print(" Formato de fecha u hora inválido. Use dd/mm/aaaa para fecha y HH:MM para hora.")
                return
            
            self.clinica.agendar_turno(dni, matricula, especialidad, fecha_hora)
            print(f" Turno agendado exitosamente para el {fecha_str} a las {hora_str}.")
            
        except (PacienteNoEncontradoException, MedicoNoEncontradoException, 
                MedicoNoDisponibleException, TurnoOcupadoException, 
                EspecialidadNoValidaException) as e:
            print(f" {e}")
        except Exception as e:
            print(f" Error inesperado: {e}")
    
    def emitir_receta(self):
        """Emite una nueva receta"""
        print("\n--- EMITIR RECETA ---")
        try:
            dni = input("DNI del paciente: ").strip()
            matricula = input("Matrícula del médico: ").strip()
            
            if not dni or not matricula:
                print(" DNI y matrícula son obligatorios.")
                return
            
            print("Medicamentos (separados por comas):")
            medicamentos_input = input("Medicamentos: ").strip()
            
            if not medicamentos_input:
                print(" Debe especificar al menos un medicamento.")
                return
            
            medicamentos = [med.strip() for med in medicamentos_input.split(",")]
            medicamentos = [med for med in medicamentos if med]  # Filtrar vacíos
            
            if not medicamentos:
                print(" Debe especificar al menos un medicamento válido.")
                return
            
            self.clinica.emitir_receta(dni, matricula, medicamentos)
            print("Receta emitida exitosamente.")
            
        except (PacienteNoEncontradoException, MedicoNoEncontradoException, 
                RecetaInvalidaException) as e:
            print(f" {e}")
        except Exception as e:
            print(f" Error inesperado: {e}")
    
    def ver_historia_clinica(self):
        """Muestra la historia clínica de un paciente"""
        print("\n--- HISTORIA CLÍNICA ---")
        try:
            dni = input("DNI del paciente: ").strip()
            
            if not dni:
                print(" El DNI es obligatorio.")
                return
            
            historia = self.clinica.obtener_historia_clinica(dni)
            print("\n" + str(historia))
            
        except PacienteNoEncontradoException as e:
            print(f"{e}")
        except Exception as e:
            print(f" Error inesperado: {e}")
    
    def ver_turnos(self):
        """Muestra todos los turnos agendados"""
        print("\n--- TODOS LOS TURNOS ---")
        try:
            turnos = self.clinica.obtener_turnos()
            
            if not turnos:
                print("No hay turnos agendados.")
                return
            
            print(f"Total de turnos: {len(turnos)}\n")
            for i, turno in enumerate(turnos, 1):
                print(f"{i}. {turno}")
                
        except Exception as e:
            print(f" Error inesperado: {e}")
    
    def ver_pacientes(self):
        """Muestra todos los pacientes registrados"""
        print("\n--- TODOS LOS PACIENTES ---")
        try:
            pacientes = self.clinica.obtener_pacientes()
            
            if not pacientes:
                print("No hay pacientes registrados.")
                return
            
            print(f"Total de pacientes: {len(pacientes)}\n")
            for i, paciente in enumerate(pacientes, 1):
                print(f"{i}. {paciente}")
                
        except Exception as e:
            print(f" Error inesperado: {e}")
    
    def ver_medicos(self):
        """Muestra todos los médicos registrados"""
        print("\n--- TODOS LOS MÉDICOS ---")
        try:
            medicos = self.clinica.obtener_medicos()
            
            if not medicos:
                print("No hay médicos registrados.")
                return
            
            print(f"Total de médicos: {len(medicos)}\n")
            for i, medico in enumerate(medicos, 1):
                print(f"{i}. {medico}")
                
        except Exception as e:
            print(f" Error inesperado: {e}")


def main():
    """Función principal para ejecutar la aplicación"""
    cli = CLI()
    cli.ejecutar()


if __name__ == "__main__":
    main()