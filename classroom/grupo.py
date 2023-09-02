from classroom.asignatura import Asignatura
from multimethod import multimethod
class Grupo:
    grado = 12

    def __init__(self, grupo="grupo predeterminado", asignaturas=[],estudiantes =[] ):
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes

    def listadoAsignaturas(self, **kwargs):
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno, lista=None):
        if lista is None:
            lista = []
        lista.append(alumno)
        self.listadoAlumnos = self.listadoAlumnos + lista

    @multimethod
    def __str__(self,x) -> None:
        return "Grupo de estudiantes: " + self._grupo
    
    @multimethod
    def __str__(self,x: int) -> None:
        return "Grado: " + str(x)
    
    @ classmethod
    def asignarNombre(cls, nombre="Grado 10"):
        cls.grado = nombre

    @ classmethod
    def asignarNombre(cls, nombre="Grado 4"):
        cls.grado = nombre
    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre