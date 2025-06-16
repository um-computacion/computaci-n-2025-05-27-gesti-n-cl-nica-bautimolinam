# tests/test_historia_clinica.py

import unittest
from datetime import datetime
import sys
import os

# Agregar el directorio padre al path para poder importar el modelo
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modelo.modelopaciente import Paciente
from modelo.modelomedico import Medico
from modelo.modeloturno import Turno
from modelo.modeloreceta import Receta
from modelo.modelohistoriaclinica import HistoriaClinica


class TestHistoriaClinica(unittest.TestCase):
    """Tests para la clase HistoriaClinica"""
    
    def setUp(self):
        """Configuración inicial para los tests"""
        self.paciente = Paciente("Ana López", "11223344", "25/12/1992")
        self.medico = Medico("Dr. José Pérez", "MAT003")
        self.fecha_hora = datetime(2025, 6, 25, 10, 0)
        self.historia = HistoriaClinica(self.paciente)
    
    def test_crear_historia_clinica_exitosa(self):
        """Test: Crear historia clínica con paciente válido"""
        historia = HistoriaClinica(self.paciente)
        
        self.assertEqual(len(historia.obtener_turnos()), 0)
        self.assertEqual(len(historia.obtener_recetas()), 0)
        
        str_historia = str(historia)
        self.assertIn("Ana López", str_historia)
        self.assertIn("11223344", str_historia)
        self.assertIn("No hay turnos", str_historia)
        self.assertIn("No hay recetas", str_historia)
    
    def test_crear_historia_clinica_paciente_none(self):
        """Test: No se puede crear historia clínica sin paciente"""
        with self.assertRaises(ValueError):
            HistoriaClinica(None)
    
    def test_agregar_turno_exitoso(self):
        """Test: Agregar turno a la historia clínica"""
        turno = Turno(self.paciente, self.medico, self.fecha_hora, "Pediatría")
        
        self.historia.agregar_turno(turno)
        
        turnos = self.historia.obtener_turnos()
        self.assertEqual(len(turnos), 1)
        self.assertEqual(turnos[0], turno)
    
    def test_agregar_turno_none(self):
        """Test: No se puede agregar turno None"""
        with self.assertRaises(ValueError):
            self.historia.agregar_turno(None)
    
    def test_agregar_receta_exitosa(self):
        """Test: Agregar receta a la historia clínica"""
        medicamentos = ["Paracetamol", "Ibuprofeno"]
        receta = Receta(self.paciente, self.medico, medicamentos)
        
        self.historia.agregar_receta(receta)
        
        recetas = self.historia.obtener_recetas()
        self.assertEqual(len(recetas), 1)
        self.assertEqual(recetas[0], receta)
    
    def test_agregar_receta_none(self):
        """Test: No se puede agregar receta None"""
        with self.assertRaises(ValueError):
            self.historia.agregar_receta(None)
    
    def test_multiples_turnos_y_recetas(self):
        """Test: Agregar múltiples turnos y recetas"""
        # Agregar turnos
        turno1 = Turno(self.paciente, self.medico, self.fecha_hora, "Pediatría")
        turno2 = Turno(self.paciente, self.medico, 
                      datetime(2025, 7, 1, 15, 30), "Cardiología")
        
        self.historia.agregar