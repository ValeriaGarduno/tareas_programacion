import random
from medico.medico import Medico
from paciente.paciente import Paciente

class Consulta:
    id = int
    fecha_hora = str
    consultorio = str
    medico = str
    paciente = str

    def __init__(self, fecha_hora, consultorio, medico, paciente):
        self.id = random.randint(1, 10000)
        self.fecha_hora = fecha_hora
        self.consultorio = consultorio
        self.medico = medico
        self.paciente = paciente

    @property
    def id(self):
        return self.id
    
    @property
    def fecha_hora(self):
        return self.fecha_hora
    
    @property
    def consultorio(self):
        return self.consultorio
    
    @property
    def medico(self):
        return self.medico
    
    @property
    def paciente(self):
        return self.paciente