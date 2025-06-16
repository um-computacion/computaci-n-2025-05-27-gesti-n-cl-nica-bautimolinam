

from typing import List, Optional
from modeloespecialidad import Especialidad


class Medico:
    """Representa a un médico del sistema"""
    
    def __init__(self, nombre: str, matricula: str):
        if not nombre or not matricula:
            raise ValueError("Nombre y matrícula son obligatorios")
        
        self.__nombre = nombre
        self.__matricula = matricula
        self.__especialidades = []
    
    def agregar_especialidad(self, especialidad: Especialidad):
        """Agrega una especialidad a la lista del médico"""
        # Verificar que no exista ya esta especialidad
        for esp in self.__especialidades:
            if esp.obtener_especialidad() == especialidad.obtener_especialidad():
                raise ValueError(f"La especialidad {especialidad.obtener_especialidad()} ya existe para este médico")
        
        self.__especialidades.append(especialidad)
    
    def obtener_matricula(self) -> str:
        """Devuelve la matrícula del médico"""
        return self.__matricula
    
    def obtener_especialidad_para_dia(self, dia: str) -> Optional[str]:
        """Devuelve el nombre de la especialidad disponible en el día especificado"""
        for especialidad in self.__especialidades:
            if especialidad.verificar_dia(dia):
                return especialidad.obtener_especialidad()
        return None
    
    def __str__(self) -> str:
        """Representación legible del médico"""
        if not self.__especialidades:
            return f"Dr. {self.__nombre} (Matrícula: {self.__matricula}) - Sin especialidades"
        
        especialidades_str = ", ".join([str(esp) for esp in self.__especialidades])
        return f"Dr. {self.__nombre} (Matrícula: {self.__matricula}) - Especialidades: {especialidades_str}"