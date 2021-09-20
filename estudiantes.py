from componentes import Menu,Valida
from helpers import borrarPantalla,gotoxy
from crudArhivos import Archivo
from entidadesUnemi import *
from datetime import date
import time

# Procesos de las Opciones del Menu Mantenimiento
def carreras():
   borrarPantalla()
   gotoxy(20,2);print("MANTENIMIENTO DE CARRERAS")
   gotoxy(15,4);print("Codigo: ")
   gotoxy(13,5);print("Carrera: ")
   gotoxy(33,5)
   descarrera = input()
   archiCarrera = Archivo("./datos/carrera.txt",";")
   carreras = archiCarrera.leer()
   if carreras : idSig = int(carreras[-1][0])+1
   else: idSig=1
   carrera = Carrera(idSig,descarrera)
   datos = carrera.getCarrera()
   datos = ';'.join(datos)
   archiCarrera.escribir([datos],"a")

def materias():
   borrarPantalla()
   gotoxy(20,2);print("INGRESO DE MATERIAS")
   gotoxy(15,4);print("Codigo: ")
   gotoxy(12,5);print("Materias: ")
   gotoxy(33,5)
   desmateria = input()
   archiMateria = Archivo("./datos/materia.txt",";")
   materias = archiMateria.leer()
   if materias : idSig = int(materias[-1][0])+1
   else: idSig=1
   materia = Materia(idSig,desmateria)
   datos = materia.getMateria()
   datos = ';'.join(datos)
   archiMateria.escribir([datos],"a")

def periodos():
   borrarPantalla()
   gotoxy(20,2);print("INGRESO DE PERIODOS")
   gotoxy(15,4);print("Codigo: ")
   gotoxy(12,5);print("Periodos: ")
   gotoxy(33,5)
   desperiodo = input()
   archiPeriodo = Archivo("./datos/periodo.txt",";")
   periodos = archiPeriodo.leer()
   if periodos : idSig = int(periodos[-1][0])+1
   else: idSig=1
   periodo = Periodo(idSig,desperiodo)
   datos = periodo.getPeriodo()
   datos = ';'.join(datos)
   archiPeriodo.escribir([datos],"a")

def profesores():
   borrarPantalla()
   validar = Valida()
   gotoxy(20,2);print("INGRESO DE PROFESORES")
   gotoxy(15,4);print("Nombre: ")
   gotoxy(15,5);print("Cedula: ")
   gotoxy(15,6);print("Titulo: ")
   gotoxy(15,7);print("Telefono: ")
   gotoxy(15,8);print("Carrera ID[    ]: ")
   gotoxy(25,4);nom = input()
   gotoxy(25,5);ced = input()
   gotoxy(25,6);tit = input()
   tel=validar.solo_numeros("Error: Solo numeros",25,7)
   lisCarrera,entCarrera = [],None
   while not lisCarrera:
      gotoxy(27,8);id = input().upper()
      archiCarrera = Archivo("./datos/carrera.txt")
      lisCarrera = archiCarrera.buscar(id)
      if lisCarrera:
          entCarrera = Carrera(lisCarrera[0],lisCarrera[1])
          gotoxy(33,8);print(entCarrera.descripcion)
      else:
         gotoxy(33,8);print("No existe Carrera con ese codigo[{}]:".format(id))
         time.sleep(1);gotoxy(33,8);print(" "*40)
   gotoxy(15,10);print("Esta seguro de Grabar El registro(s/n):")
   gotoxy(54,10);grabar = input().lower()
   if grabar == "s":
        archiProfesor = Archivo("./datos/profesor.txt")
        lisProfesores = archiProfesor.leer()
        if lisProfesores : idSig = int(lisProfesores[-1][0])+1
        else: idSig=1
        entProfesor = Profesor(idSig,nom,ced,entCarrera,tit,tel)
        datos = entProfesor.getProfesor()
        datos = ';'.join(datos)
        archiProfesor.escribir([datos],"a")
        gotoxy(15,11);input("Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...")
   else:
       gotoxy(15,11);input("Registro No fue Grabado\n presione una tecla para continuar...")

def estudiantes():
   borrarPantalla()
   validar = Valida()
   gotoxy(20,2);print("INGRESO DE ESTUDIANTES ")
   gotoxy(15,4);print("Nombre: ")
   gotoxy(15,5);print("Cedula: ")
   gotoxy(14,6);print("Direccion: ")
   gotoxy(15,7);print("Telefono: ")
   gotoxy(15,8);print("Carrera ID[    ]: ")
   gotoxy(25,4);nom = input()
   ced=validar.solo_numeros("Error: Solo numeros",25,5)
   gotoxy(25,6);dire = input()
   tell=validar.solo_numeros("Error: Solo numeros",25,7)
   lisCarrera,entCarrera = [],None
   while not lisCarrera:
      gotoxy(27,8);id = input().upper()
      archiCarrera = Archivo("./datos/carrera.txt")
      lisCarrera = archiCarrera.buscar(id)
      if lisCarrera:
          entCarrera = Carrera(lisCarrera[0],lisCarrera[1])
          gotoxy(33,8);print(entCarrera.descripcion)
      else:
         gotoxy(33,8);print("No existe Carrera con ese codigo[{}]:".format(id))
         time.sleep(1);gotoxy(33,8);print(" "*40)
   gotoxy(15,10);print("Esta seguro de Grabar El registro(s/n):")
   gotoxy(54,10);grabar = input().lower()
   if grabar == "s":
        archiEstudiante = Archivo("./datos/estudiante.txt")
        lisEstudiantes = archiEstudiante.leer()
        if lisEstudiantes : idSig = int(lisEstudiantes[-1][0])+1
        else: idSig=1
        entEstudiante = Estudiante(idSig,nom,ced,dire,tell)
        datos = entEstudiante.getEstudiante()
        datos = ';'.join(datos)
        archiEstudiante.escribir([datos],"a")
        gotoxy(15,11);input("Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...")
   else:
       gotoxy(15,11);input("Registro No fue Grabado\n presione una tecla para continuar...")

def matriculas():
    borrarPantalla()
    validar = Valida()
    gotoxy(20,1);print("INGRESO DE MATRICULA ")
    gotoxy(14,4);print("Valor: ")
    gotoxy(14,5);print("Estudiante ID[   ]: ")
    gotoxy(14,6);print("Carrera ID[    ]: ")
    gotoxy(14,7);print("Periodo ID[   ]: ")
    val = validar.solo_numeros("Error: Solo numeros",23,4)
    lisEstudiante,entEstudiante = [], None
    while not lisEstudiante:
        gotoxy(29,5); idPr = input().upper()
        archiEstudiante = Archivo("./datos/estudiante.txt")
        lisEstudiante = archiEstudiante.buscar(idPr)
        if lisEstudiante:
            entEstudiante = Estudiante(lisEstudiante[0],lisEstudiante[1],lisEstudiante[2],lisEstudiante[3],lisEstudiante[4])
            gotoxy(35,5);print(entEstudiante.nombre)
        else:
            gotoxy(35,5);print("No existe carrera con ese codigo.")
            time.sleep(1);gotoxy(35,5);print(" "*40)
    lisCarrera,entCarrera = [], None
    while not lisCarrera:
        gotoxy(27,6); idCr = input().upper()
        archiCarrera = Archivo("./datos/carrera.txt")
        lisCarrera = archiCarrera.buscar(idCr)
        if lisCarrera:
            entCarrera = Carrera(lisCarrera[0],lisCarrera[1])
            gotoxy(31,6);print(entCarrera.descripcion)
        else:
            gotoxy(31,6);print("No existe carrera con ese codigo.")
            time.sleep(1);gotoxy(31,6);print(" "*40)
    lisPeriodo,entPeriodo = [], None
    while not lisPeriodo:
        gotoxy(27,7);idPrd = input().upper()
        archiPeriodo = Archivo("./datos/periodo.txt")
        lisPeriodo = archiPeriodo.buscar(idPrd)
        if lisPeriodo:
            entPeriodo = Periodo(lisPeriodo[0],lisPeriodo[1])
            gotoxy(31,7);print(entPeriodo.descripcion)
        else:
            gotoxy(31,7);print("No existe carrera con ese codigo.")
            time.sleep(1);gotoxy(31,7);print(" "*40)
    gotoxy(15,9);print("Esta seguro de  Grabar El registro(s/n):")
    gotoxy(54,10);grabar = input().lower()
    if grabar == "s":
        archiMatricula = Archivo("./datos/matricula.txt")
        lisMatricula = archiMatricula.leer()
        if lisMatricula: idM = int(lisMatricula[-1][0])+1
        else: idM =1
        entMatricula = Matricula(idM,entEstudiante,entCarrera,entPeriodo,val)
        dato = entMatricula.getMatricula()
        dato = ';'.join(dato)
        archiMatricula.escribir([dato],"a")
        gotoxy(14,11); input("Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...")
    else:
       gotoxy(14,11);input("Registro No fue Grabado\n presione una tecla para continuar...")

def notas():
    borrarPantalla()
    validar = Valida()
    gotoxy(20,1);print("INGRESO DE NOTAS ")
    gotoxy(15,5);print("Periodo ID [   ]: ")
    gotoxy(15,6);print("Estudiante ID [   ]: ")
    gotoxy(15,7);print("Materia ID [   ]: ")
    gotoxy(15,8);print("Profesor ID [   ]: ")
    gotoxy(15,9);print("nota1: ")
    gotoxy(15,10);print("nota2: ")
    lisPeriodo,entPeriodo = [],None
    while not lisPeriodo:
        gotoxy(28,5);idPer = input().upper()
        archiPeriodo = Archivo("./datos/periodo.txt")
        lisPeriodo = archiPeriodo.buscar(idPer)
        if lisPeriodo:
            entPeriodo = Periodo(lisPeriodo[0],lisPeriodo[1])
            gotoxy(34,5);print(entPeriodo.descripcion)
        else:
            gotoxy(34,5);print("No existe Carrera con ese codigo[{}]:".format(idPer))
            time.sleep(1);gotoxy(34,5);print(" "*40)
    lisEstudiante,entEstudiante = [],None
    while not lisEstudiante:
        gotoxy(31,6);id = input().upper()
        archiEstudiante = Archivo("./datos/estudiante.txt")
        lisEstudiante = archiEstudiante.buscar(id)
        if lisEstudiante:
            entEstudiante = Estudiante(lisEstudiante[0],lisEstudiante[1],lisEstudiante[2],lisEstudiante[3],lisEstudiante[4]) 
            gotoxy(36,6);print(entEstudiante.nombre)
        else:
            gotoxy(36,6);print("No existe Carrera con ese codigo[{}]:".format(id))
            time.sleep(1);gotoxy(36,6);print(" "*40)
    lisMateria,entMateria = [],None
    while not lisMateria:
        gotoxy(29,7);id = input().upper()
        archiMateria= Archivo("./datos/materia.txt")
        lisMateria = archiMateria.buscar(id)
        if lisMateria:
            entMateria = Materia(lisMateria[0],lisMateria[1])
            gotoxy(35,7);print(entMateria.descripcion)
        else:
            gotoxy(35,7);print("No existe Carrera con ese codigo[{}]:".format(id))
            time.sleep(1);gotoxy(29,7);print(" "*40)
    lisProfesor,entProfesor = [],None
    while not lisProfesor:
        gotoxy(29,8);id = input().upper()
        archiProfesor = Archivo("./datos/profesor.txt")
        lisProfesor = archiProfesor.buscar(id)
        if lisProfesor:
            entProfesor = Profesor(lisProfesor[0],lisProfesor[1],lisProfesor[2],lisProfesor[3],lisProfesor[4],lisProfesor[5]) 
            gotoxy(32,8);print(entProfesor.nombre)
        else:
            gotoxy(32,8);print("No existe Carrera con ese codigo[{}]:".format(id))
            time.sleep(1);gotoxy(32,8);print(" "*40)
    not1=validar.solo_numeros("Error: Solo numeros",25,9)
    not2=validar.solo_numeros("Error: Solo numeros",25,10)
    gotoxy(15,12);print("Esta seguro de Grabar El registro(s/n):")
    gotoxy(54,12);grabar = input().lower()
    if grabar == "s":
        archiNota = Archivo("./datos/nota.txt")
        lisNotas = archiNota.leer()
        if lisNotas : idSig = int(lisNotas[-1][0])+1
        else: idSig=1
        entNota = Nota(idSig,entPeriodo,entEstudiante,entMateria,entProfesor,not1,not2)
        datos = entNota.getNota()
        datos = ';'.join(datos)
        archiNota.escribir([datos],"a")
        gotoxy(15,14);input("Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...")
    else:
        gotoxy(15,14);input("Registro No fue Grabado\n presione una tecla para continuar...")

# Menu Principal
opc=''
while opc !='4':
    borrarPantalla()
    menu = Menu("Menu Principal",["1) Mantenimiento","2) Matriculacion","3) Notas","4) Salir"],20,10)
    opc = menu.menu()
    if opc == "1":
        opc1 = ''
        while opc1 !='6':
            borrarPantalla()
            menu1 = Menu("Menu Mantenimiento",["1) Carrera","2) Materias","3) Periodos","4) Profesores","5) Estudiantes","6) Salir"],20,10)
            opc1 = menu1.menu()
            if opc1 == "1":
                carreras()
            elif opc1 == "2":
                materias()
            elif opc1 == "3":
                periodos()
            elif opc1 == "4":
                profesores()
            elif opc1 == "5":
                estudiantes()
    elif opc == "2":
            borrarPantalla()
            menu2 = Menu("Menu Matriculacion",["1) Matricula","2) Salir"],20,10)
            opc2 = menu2.menu()
            if opc2 == "1":
                matriculas()
    elif opc == "3":
            borrarPantalla()
            menu3 = Menu("Menu Notas",["1) Notas","2) Salir"],20,10)
            opc3 = menu3.menu()
            if opc3 == "1":
                notas()
    elif opc == "4":
           borrarPantalla()
           print("Gracias por su visita....")
    else:
          print("Opcion no valida")

input("Presione una tecla para salir")
borrarPantalla()

