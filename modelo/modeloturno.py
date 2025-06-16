

from datetime import datetime
from modelopaciente import Paciente
from modelomedico import Medico


class Turno:
    """Representa un turno médico"""
    
    def __init__(self, paciente: Paciente, medico: Medico, fecha_hora: datetime, especialidad: str):
        if not paciente or not medico or not fecha_hora or not especialidad:
            raise ValueError("Todos los campos son obligatorios")
        
        self.__paciente = paciente
        self.__medico = medico
        self.__fecha_hora = fecha_hora
        self.__especialidad = especialidad
    
    def obtener_medico(self) -> Medico:
        """Devuelve el médico asignado al turno"""
        return self.__medico
    
    def obtener_fecha_hora(self) -> datetime:
        """Devuelve la fecha y hora del turno"""
        return self.__fecha_hora
    
    def __str__(self) -> str:
        """Representación legible del turno"""
        fecha_str = self.__fecha_hora.strftime("%d/%m/%Y %H:%M")
        return f"Turno: {self.__paciente} con Dr. {self.__medico.obtener_matricula()} - {self.__especialidad} el {fecha_str}"