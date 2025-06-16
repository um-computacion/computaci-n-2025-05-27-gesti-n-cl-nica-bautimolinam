

from typing import List



class Especialidad:
    """Representa una especialidad médica con sus días de atención"""
    
    def __init__(self, tipo: str, dias: List[str]):
        if not tipo or not dias:
            raise ValueError("Tipo y días son obligatorios")
        
        # Validar que los días sean válidos
        dias_validos = ['lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado', 'domingo']
        for dia in dias:
            if dia.lower() not in dias_validos:
                raise ValueError(f"Día inválido: {dia}")
        
        self.__tipo = tipo
        self.__dias = [dia.lower() for dia in dias]  # Normalizar a minúsculas
    
    def obtener_especialidad(self) -> str:
        """Devuelve el nombre de la especialidad"""
        return self.__tipo
    
    def verificar_dia(self, dia: str) -> bool:
        """Verifica si la especialidad está disponible en el día proporcionado"""
        return dia.lower() in self.__dias
    
    def __str__(self) -> str:
        """Representación legible de la especialidad"""
        dias_str = ", ".join(self.__dias)
        return f"{self.__tipo} (Días: {dias_str})"