import unittest
from datetime import datetime
from modelo.modeloclinica import Clinica
from modelo.modelopaciente import Paciente
from modelo.modelomedico import Medico
from modelo.modeloespecialidad import Especialidad
from modelo.modeloexcepciones import (
    PacienteNoEncontradoException,
    MedicoNoDisponibleException,
    TurnoOcupadoException,
    RecetaInvalidaException
)

class TestExcepciones(unittest.TestCase):

    def setUp(self):
        self.clinica = Clinica()
        self.paciente = Paciente("Juan quintero", "12345678", "01/01/1990")
        self.medico = Medico("Dra. Martínez", "MED001")
        self.especialidad = Especialidad("Pediatría", ["lunes"])
        self.medico.agregar_especialidad(self.especialidad)
        self.clinica.agregar_medico(self.medico)
        self.clinica.agregar_paciente(self.paciente)

    def test_paciente_no_encontrado(self):
        with self.assertRaises(PacienteNoEncontradoException):
            self.clinica.emitir_receta("00000000", "MED001", ["Paracetamol"])

    def test_medico_no_disponible_para_especialidad(self):
        fecha = datetime(2025, 6, 17, 10, 0)  # martes
        with self.assertRaises(MedicoNoDisponibleException):
            self.clinica.agendar_turno("12345678", "MED001", "Pediatría", fecha)

    def test_turno_ocupado(self):
        fecha = datetime(2025, 6, 16, 10, 0)  # lunes
        self.clinica.agendar_turno("12345678", "MED001", "Pediatría", fecha)
        with self.assertRaises(TurnoOcupadoException):
            self.clinica.agendar_turno("12345678", "MED001", "Pediatría", fecha)

    def test_receta_invalida_sin_medicamentos(self):
        with self.assertRaises(RecetaInvalidaException):
            self.clinica.emitir_receta("12345678", "MED001", [])

if __name__ == "__main__":
    unittest.main()
