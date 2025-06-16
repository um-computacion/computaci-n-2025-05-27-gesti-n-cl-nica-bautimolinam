

from typing import List
from modelopaciente import Paciente
from modeloturno import Turno
from modeloreceta import Receta


class HistoriaClinica:
    """Almacena la información médica de un paciente"""
    
    def __init__(self, paciente: Paciente):
        if not paciente:
            raise ValueError("El paciente es obligatorio")
        
        self.__paciente = paciente
        self.__turnos = []
        self.__recetas = []
    
    def agregar_turno(self, turno: Turno):
        """Agrega un nuevo turno a la historia clínica"""
        if not turno:
            raise ValueError("El turno es obligatorio")
        self.__turnos.append(turno)
    
    def agregar_receta(self, receta: Receta):
        """Agrega una receta médica a la historia clínica"""
        if not receta:
            raise ValueError("La receta es obligatoria")
        self.__recetas.append(receta)
    
    def obtener_turnos(self) -> List[Turno]:
        """Devuelve una copia de la lista de turnos del paciente"""
        return self.__turnos.copy()
    
    def obtener_recetas(self) -> List[Receta]:
        """Devuelve una copia de la lista de recetas del paciente"""
        return self.__recetas.copy()
    
    def __str__(self) -> str:
        """Representación textual de la historia clínica"""
        resultado = f"Historia Clínica de {self.__paciente}\n"
        resultado += "=" * 50 + "\n"
        
        resultado += f"TURNOS ({len(self.__turnos)}):\n"
        if self.__turnos:
            for i, turno in enumerate(self.__turnos, 1):
                resultado += f"  {i}. {turno}\n"
        else:
            resultado += "  No hay turnos registrados.\n"
        
        resultado += f"\nRECETAS ({len(self.__recetas)}):\n"
        if self.__recetas:
            for i, receta in enumerate(self.__recetas, 1):
                resultado += f"  {i}. {receta}\n"
        else:
            resultado += "  No hay recetas registradas.\n"
        
        return resultado