from typing import List
from escuela.escuela import Escuela
from estudiantes.estudiantes import Estudiante
from datetime import datetime
from maestros.maestros import Maestro
from materias.materias import Materia
from grupo.grupo import Grupo
from random import randint
class Semestre:
    id: str
    numero: int
    id_carrera: str
    materias: List[Materia]
    grupo: List[Grupo]

    def __init__(self, numero: int, id_carrera: str):
        self.id = self.generar_id_semestre(numero)
        self.id_carrera = id_carrera

    def generar_id_semestre(self, numero_semestre: int) -> str:
        return f"{numero_semestre}-{randint(0,100000)}-{randint(0,100000)}"