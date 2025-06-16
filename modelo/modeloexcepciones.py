

class PacienteNoEncontradoException(Exception):
    """Excepción cuando no se encuentra un paciente"""
    pass


class MedicoNoEncontradoException(Exception):
    """Excepción cuando no se encuentra un médico"""
    pass


class MedicoNoDisponibleException(Exception):
    """Excepción cuando el médico no está disponible"""
    pass


class TurnoOcupadoException(Exception):
    """Excepción cuando ya existe un turno en esa fecha/hora"""
    pass


class RecetaInvalidaException(Exception):
    """Excepción cuando la receta es inválida"""
    pass


class EspecialidadNoValidaException(Exception):
    """Excepción cuando la especialidad no es válida"""
    pass


class PacienteDuplicadoException(Exception):
    """Excepción cuando se intenta registrar un paciente duplicado"""
    pass


class MedicoDuplicadoException(Exception):
    """Excepción cuando se intenta registrar un médico duplicado"""
    pass