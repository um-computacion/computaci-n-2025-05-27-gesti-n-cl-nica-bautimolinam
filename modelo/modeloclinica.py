

from datetime import datetime
from typing import List, Dict
from modelopaciente import Paciente
from modelomedico import Medico
from modeloturno import Turno
from modeloreceta import Receta
from modelohistoriaclinica import HistoriaClinica
from modeloespecialidad import Especialidad
from modeloexcepciones import (
    PacienteNoEncontradoException,
    MedicoNoEncontradoException,
    MedicoNoDisponibleException,
    TurnoOcupadoException,
    RecetaInvalidaException,
    EspecialidadNoValidaException,
    PacienteDuplicadoException,
    MedicoDuplicadoException
)


class Clinica:
    """Clase principal que representa el sistema de gestión de la clínica"""
    
    def __init__(self):
        self.__pacientes: Dict[str, Paciente] = {}
        self.__medicos: Dict[str, Medico] = {}
        self.__turnos: List[Turno] = []
        self.__historias_clinicas: Dict[str, HistoriaClinica] = {}
    
    def agregar_paciente(self, paciente: Paciente):
        """Registra un paciente y crea su historia clínica"""
        dni = paciente.obtener_dni()
        if dni in self.__pacientes:
            raise PacienteDuplicadoException(f"Ya existe un paciente con DNI {dni}")
        
        self.__pacientes[dni] = paciente
        self.__historias_clinicas[dni] = HistoriaClinica(paciente)
    
    def agregar_medico(self, medico: Medico):
        """Registra un médico"""
        matricula = medico.obtener_matricula()
        if matricula in self.__medicos:
            raise MedicoDuplicadoException(f"Ya existe un médico con matrícula {matricula}")
        
        self.__medicos[matricula] = medico
    
    def obtener_pacientes(self) -> List[Paciente]:
        """Devuelve todos los pacientes registrados"""
        return list(self.__pacientes.values())
    
    def obtener_medicos(self) -> List[Medico]:
        """Devuelve todos los médicos registrados"""
        return list(self.__medicos.values())
    
    def obtener_medico_por_matricula(self, matricula: str) -> Medico:
        """Devuelve un médico por su matrícula"""
        if matricula not in self.__medicos:
            raise MedicoNoEncontradoException(f"No existe médico con matrícula {matricula}")
        return self.__medicos[matricula]
    
    def validar_existencia_paciente(self, dni: str):
        """Verifica si un paciente está registrado"""
        if dni not in self.__pacientes:
            raise PacienteNoEncontradoException(f"No existe paciente con DNI {dni}")
    
    def validar_existencia_medico(self, matricula: str):
        """Verifica si un médico está registrado"""
        if matricula not in self.__medicos:
            raise MedicoNoEncontradoException(f"No existe médico con matrícula {matricula}")
    
    def validar_turno_no_duplicado(self, matricula: str, fecha_hora: datetime):
        """Verifica que no haya un turno duplicado"""
        for turno in self.__turnos:
            if (turno.obtener_medico().obtener_matricula() == matricula and 
                turno.obtener_fecha_hora() == fecha_hora):
                raise TurnoOcupadoException(f"Ya existe un turno para el médico {matricula} en esa fecha y hora")
    
    def obtener_dia_semana_en_espanol(self, fecha_hora: datetime) -> str:
        """Traduce un objeto datetime al día de la semana en español"""
        dias = ['lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado', 'domingo']
        return dias[fecha_hora.weekday()]
    
    def obtener_especialidad_disponible(self, medico: Medico, dia_semana: str) -> str:
        """Obtiene la especialidad disponible para un médico en un día"""
        especialidad = medico.obtener_especialidad_para_dia(dia_semana)
        if not especialidad:
            raise MedicoNoDisponibleException(f"El médico no atiende el día {dia_semana}")
        return especialidad
    
    def validar_especialidad_en_dia(self, medico: Medico, especialidad_solicitada: str, dia_semana: str):
        """Verifica que el médico atienda esa especialidad ese día"""
        especialidad_disponible = medico.obtener_especialidad_para_dia(dia_semana)
        if not especialidad_disponible:
            raise MedicoNoDisponibleException(f"El médico no atiende el día {dia_semana}")
        
        if especialidad_disponible.lower() != especialidad_solicitada.lower():
            raise EspecialidadNoValidaException(
                f"El médico no atiende {especialidad_solicitada} el día {dia_semana}. "
                f"Ese día atiende: {especialidad_disponible}"
            )
    
    def agendar_turno(self, dni: str, matricula: str, especialidad: str, fecha_hora: datetime):
        """Agenda un turno si se cumplen todas las condiciones"""
        # Validar existencia de paciente y médico
        self.validar_existencia_paciente(dni)
        self.validar_existencia_medico(matricula)
        
        # Obtener objetos
        paciente = self.__pacientes[dni]
        medico = self.__medicos[matricula]
        
        # Validar que no haya turno duplicado
        self.validar_turno_no_duplicado(matricula, fecha_hora)
        
        # Validar día y especialidad
        dia_semana = self.obtener_dia_semana_en_espanol(fecha_hora)
        self.validar_especialidad_en_dia(medico, especialidad, dia_semana)
        
        # Crear y registrar turno
        turno = Turno(paciente, medico, fecha_hora, especialidad)
        self.__turnos.append(turno)
        
        # Agregar a historia clínica
        self.__historias_clinicas[dni].agregar_turno(turno)
    
    def obtener_turnos(self) -> List[Turno]:
        """Devuelve todos los turnos agendados"""
        return self.__turnos.copy()
    
    def emitir_receta(self, dni: str, matricula: str, medicamentos: List[str]):
        """Emite una receta para un paciente"""
        # Validar existencia
        self.validar_existencia_paciente(dni)
        self.validar_existencia_medico(matricula)
        
        if not medicamentos or len(medicamentos) == 0:
            raise RecetaInvalidaException("La receta debe incluir al menos un medicamento")
        
        # Obtener objetos
        paciente = self.__pacientes[dni]
        medico = self.__medicos[matricula]
        
        # Crear receta
        receta = Receta(paciente, medico, medicamentos)
        
        # Agregar a historia clínica
        self.__historias_clinicas[dni].agregar_receta(receta)
    
    def obtener_historia_clinica(self, dni: str) -> HistoriaClinica:
        """Devuelve la historia clínica completa de un paciente"""
        self.validar_existencia_paciente(dni)
        return self.__historias_clinicas[dni]