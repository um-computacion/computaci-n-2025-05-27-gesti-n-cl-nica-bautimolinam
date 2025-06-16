# tests/test_medico.py

import unittest
import sys
import os

# Agregar el directorio padre al path para poder importar el modelo
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modelo.modelomedico import Medico
from modelo.modeloespecialidad import Especialidad


class TestMedico(unittest.TestCase):
    """Tests para la clase Medico"""
    
    def test_crear_medico_exitoso(self):
        """Test: Crear un médico con datos válidos"""
        medico = Medico("Dr. Carlos López", "MAT001")
        
        self.assertEqual(medico.obtener_matricula(), "MAT001")
        self.assertIn("Dr. Carlos López", str(medico))
        self.assertIn("MAT001", str(medico))
    
    def test_crear_medico_nombre_vacio(self):
        """Test: No se puede crear médico con nombre vacío"""
        with self.assertRaises(ValueError):
            Medico("", "MAT001")
    
    def test_crear_medico_matricula_vacia(self):
        """Test: No se puede crear médico con matrícula vacía"""
        with self.assertRaises(ValueError):
            Medico("Dr. Carlos López", "")
    
    def test_agregar_especialidad_exitosa(self):
        """Test: Agregar especialidad a un médico"""
        medico = Medico("Dr. Ana Martínez", "MAT002")
        especialidad = Especialidad("Pediatría", ["lunes", "miércoles", "viernes"])
        
        medico.agregar_especialidad(especialidad)
        
        self.assertEqual(medico.obtener_especialidad_para_dia("lunes"), "Pediatría")
        self.assertEqual(medico.obtener_especialidad_para_dia("miércoles"), "Pediatría")
        self.assertIsNone(medico.obtener_especialidad_para_dia("martes"))
    
    def test_agregar_especialidad_duplicada(self):
        """Test: No se puede agregar la misma especialidad dos veces"""
        medico = Medico("Dr. Pedro Gómez", "MAT003")
        especialidad1 = Especialidad("Cardiología", ["lunes", "martes"])
        especialidad2 = Especialidad("Cardiología", ["miércoles", "jueves"])
        
        medico.agregar_especialidad(especialidad1)
        
        with self.assertRaises(ValueError):
            medico.agregar_especialidad(especialidad2)
    
    def test_multiple_especialidades(self):
        """Test: Un médico puede tener múltiples especialidades diferentes"""
        medico = Medico("Dr. Laura Fernández", "MAT004")
        pediatria = Especialidad("Pediatría", ["lunes", "miércoles"])
        cardiologia = Especialidad("Cardiología", ["martes", "jueves"])
        
        medico.agregar_especialidad(pediatria)
        medico.agregar_especialidad(cardiologia)
        
        self.assertEqual(medico.obtener_especialidad_para_dia("lunes"), "Pediatría")
        self.assertEqual(medico.obtener_especialidad_para_dia("martes"), "Cardiología")
        self.assertEqual(medico.obtener_especialidad_para_dia("miércoles"), "Pediatría")
        self.assertEqual(medico.obtener_especialidad_para_dia("jueves"), "Cardiología")
        self.assertIsNone(medico.obtener_especialidad_para_dia("viernes"))
    
    def test_medico_sin_especialidades(self):
        """Test: Médico sin especialidades no atiende ningún día"""
        medico = Medico("Dr. Roberto Silva", "MAT005")
        
        self.assertIsNone(medico.obtener_especialidad_para_dia("lunes"))
        self.assertIsNone(medico.obtener_especialidad_para_dia("martes"))
        self.assertIn("Sin especialidades", str(medico))
    
    def test_str_representation_con_especialidades(self):
        """Test: Representación en string del médico con especialidades"""
        medico = Medico("Dr. Elena Ruiz", "MAT006")
        especialidad = Especialidad("Neurología", ["lunes", "miércoles"])
        medico.agregar_especialidad(especialidad)
        
        str_medico = str(medico)
        self.assertIn("Dr. Elena Ruiz", str_medico)
        self.assertIn("MAT006", str_medico)
        self.assertIn("Neurología", str_medico)
        self.assertIn("Especialidades:", str_medico)


if __name__ == '__main__':
    unittest.main()