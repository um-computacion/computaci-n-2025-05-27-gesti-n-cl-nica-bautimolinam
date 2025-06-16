

from datetime import datetime
from typing import List
from modelopaciente import Paciente
from modelomedico import Medico


class Receta:
    """Representa una receta médica"""
    
    def __init__(self, paciente: Paciente, medico: Medico, medicamentos: List[str]):
        if not paciente or not medico or not medicamentos:
            raise ValueError("Todos los campos son obligatorios")
        
        if len(medicamentos) == 0:
            raise ValueError("Debe incluir al menos un medicamento")
        
        self.__paciente = paciente
        self.__medico = medico
        self.__medicamentos = medicamentos
        self.__fecha = datetime.now()
    
    def __str__(self) -> str:
        """Representación en cadena de la receta"""
        fecha_str = self.__fecha.strftime("%d/%m/%Y %H:%M")
        medicamentos_str = ", ".join(self.__medicamentos)
        return f"Receta del {fecha_str} - Dr. {self.__medico.obtener_matricula()} para {self.__paciente} - Medicamentos: {medicamentos_str}"