# tests/test_paciente.py

import unittest
import sys
import os

# Agregar el directorio padre al path para poder importar el modelo
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modelo.modelopaciente import Paciente


class TestPaciente(unittest.TestCase):
    """Tests para la clase Paciente"""
    
    def test_crear_paciente_exitoso(self):
        """Test: Crear un paciente con datos válidos"""
        paciente = Paciente("Juan Pérez", "12345678", "15/03/1990")
        
        self.assertEqual(paciente.obtener_dni(), "12345678")
        self.assertIn("Juan Pérez", str(paciente))
        self.assertIn("12345678", str(paciente))
    
    def test_crear_paciente_nombre_vacio(self):
        """Test: No se puede crear paciente con nombre vacío"""
        with self.assertRaises(ValueError):
            Paciente("", "12345678", "15/03/1990")
    
    def test_crear_paciente_dni_vacio(self):
        """Test: No se puede crear paciente con DNI vacío"""
        with self.assertRaises(ValueError):
            Paciente("Juan Pérez", "", "15/03/1990")
    
    def test_crear_paciente_fecha_vacia(self):
        """Test: No se puede crear paciente con fecha vacía"""
        with self.assertRaises(ValueError):
            Paciente("Juan Pérez", "12345678", "")
    
    def test_crear_paciente_todos_campos_vacios(self):
        """Test: No se puede crear paciente con todos los campos vacíos"""
        with self.assertRaises(ValueError):
            Paciente("", "", "")
    
    def test_str_representation(self):
        """Test: Verificar representación en string del paciente"""
        paciente = Paciente("María García", "87654321", "22/07/1985")
        str_paciente = str(paciente)
        
        self.assertIn("María García", str_paciente)
        self.assertIn("87654321", str_paciente)
        self.assertIn("Paciente:", str_paciente)


if __name__ == '__main__':
    unittest.main()