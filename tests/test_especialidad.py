

import unittest
import sys
import os


sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modelo.modeloespecialidad import Especialidad


class TestEspecialidad(unittest.TestCase):
    """Tests para la clase Especialidad"""
    
    def test_crear_especialidad_exitosa(self):
        """Test: Crear una especialidad con datos válidos"""
        especialidad = Especialidad("Pediatría", ["lunes", "miércoles", "viernes"])
        
        self.assertEqual(especialidad.obtener_especialidad(), "Pediatría")
        self.assertTrue(especialidad.verificar_dia("lunes"))
        self.assertTrue(especialidad.verificar_dia("miércoles"))
        self.assertTrue(especialidad.verificar_dia("viernes"))
        self.assertFalse(especialidad.verificar_dia("martes"))
    
    def test_verificar_dia_case_insensitive(self):
        """Test: Verificar que la comparación de días no sea sensible a mayúsculas"""
        especialidad = Especialidad("Cardiología", ["LUNES", "Martes"])
        
        self.assertTrue(especialidad.verificar_dia("lunes"))
        self.assertTrue(especialidad.verificar_dia("LUNES"))
        self.assertTrue(especialidad.verificar_dia("Lunes"))
        self.assertTrue(especialidad.verificar_dia("martes"))
        self.assertTrue(especialidad.verificar_dia("MARTES"))
        self.assertFalse(especialidad.verificar_dia("miércoles"))
    
    def test_crear_especialidad_tipo_vacio(self):
        """Test: No se puede crear especialidad con tipo vacío"""
        with self.assertRaises(ValueError):
            Especialidad("", ["lunes", "martes"])
    
    def test_crear_especialidad_dias_vacios(self):
        """Test: No se puede crear especialidad sin días"""
        with self.assertRaises(ValueError):
            Especialidad("Pediatría", [])
    
    def test_crear_especialidad_dia_invalido(self):
        """Test: No se puede crear especialidad con día inválido"""
        with self.assertRaises(ValueError):
            Especialidad("Pediatría", ["lunes", "día_inventado"])
    
    def test_str_representation(self):
        """Test: Verificar representación en string de la especialidad"""
        especialidad = Especialidad("Neurología", ["martes", "jueves"])
        str_especialidad = str(especialidad)
        
        self.assertIn("Neurología", str_especialidad)
        self.assertIn("martes", str_especialidad)
        self.assertIn("jueves", str_especialidad)
        self.assertIn("Días:", str_especialidad)
    
    def test_dias_normalizados_a_minusculas(self):
        """Test: Los días se normalizan a minúsculas internamente"""
        especialidad = Especialidad("Pediatría", ["LUNES", "Miércoles", "VIERNES"])
        
        # Verificar que acepta días en cualquier formato
        self.assertTrue(especialidad.verificar_dia("lunes"))
        self.assertTrue(especialidad.verificar_dia("miércoles"))
        self.assertTrue(especialidad.verificar_dia("viernes"))


if __name__ == '__main__':
    unittest.main()
