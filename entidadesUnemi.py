class Carrera:
    def _init_(self,id,descripcion):
        self.__id = id
        self.descripcion = descripcion

    @property
    def id(self):
        return self.__id

    def getCarrera(self):
        return  [str(self.id),self.descripcion]

class Materia:
    def _init_(self,id, descripcion):
        self.__id = id
        self.descripcion = descripcion

    @property
    def id(self):
        return self.__id

    def getMateria(self):
        return  [str(self.id),self.descripcion]

class Periodo:
    def _init_(self,periodo,descripcion):
        self.periodo =periodo     # 202111
        self.descripcion = descripcion # Segundo semestre 2021


    def getPeriodo(self):
        return  [str(self.periodo),self.descripcion]

class Profesor:
    def _init_(self,id,nombre,cedula,carrera,titulo,telefono):
        self.__id = id
        self.nombre = nombre
        self.cedula = cedula
        self.titulo = titulo
        self.telefono = telefono
        self.carrera=carrera

    @property
    def id(self):
        return self.__id

    def getProfesor(self):
        return  [str(self.id),self.nombre,self.cedula,self.titulo,self.telefono,self.carrera.id]

class Estudiante:
    def _init_(self,id,nombre,cedula,direccion,telefono):
        self.__id = id
        self.nombre = nombre
        self.cedula = cedula
        self.direccion=direccion
        self.telefono = telefono

    @property
    def id(self):
        return self.__id

    def getEstudiante(self):
        return  [str(self.id),self.nombre,str(self.cedula),str(self.direccion),str(self.telefono)]

class Matricula:
    def _init_(self,id,estudiante,carrera,periodo,valor):
        self.__id = id
        self.periodo= periodo
        self.estudiante = estudiante
        self.carrera = carrera
        self.valor = valor

    @property
    def id(self):
        return self.__id

    def getMatricula(self):
        return  [str(self.id),self.periodo.periodo,self.estudiante.id,self.carrera.id,str(self.valor)]

class Nota:
    def _init_(self,id,periodo,estudiante,materia,profesor,nota1,nota2):
        self.__id = id
        self.periodo = periodo
        self.estudiante = estudiante
        self.materia = materia
        self.profesor= profesor
        self.nota1 = nota1
        self.nota2 = nota2

    @property
    def id(self):
        return self.__id

    def getNota(self):
        return  [str(self.id),self.periodo.periodo,self.estudiante.id,self.materia.id,self.profesor.id,str(self.nota1),str(self.nota2)]
