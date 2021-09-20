from componentes import Menu,Valida
from helpers import borrarPantalla,gotoxy
from crudArchivos import Archivo
from entidadesUnemi import *
from datetime import date
import time

# Procesos de las Opciones del Menu Mantenimiento
def carreras():
    borrarPantalla()
    gotoxy(20,2);print("MANTENIMIENTO DE CARRERAS")
    gotoxy(15,4);print("Codigo: ")
    gotoxy(15,5);print("Descripcion Carrera: ")
    gotoxy(36,5)
    descarrera = input()
    archiCarrera = Archivo("./datos/carrera.txt",";")
    carreras = archiCarrera.leer()
    if carreras : idSig = int(carreras[-1][0])+1
    else: idSig=1
    carrera = Carrera(idSig,descarrera)
    datos = carrera.getCarrera()
    datos = ';'.join(datos)
    archiCarrera.escribir([datos],"a")

def materia():
    borrarPantalla()
    gotoxy(20,2);print("MANTENIMIENTO DE MATERIAS")
    gotoxy(15,4);print("Codigo: ")
    gotoxy(15,5);print("Descripcion Materias: ")
    gotoxy(36,5)
    desmateria = input()
    archiMateria = Archivo("./datos/materia.txt",";")
    materia = archiMateria.leer()
    if materia : idSig = int(materia[-1][0])+1
    else: idSig=1
    materia = Materia(idSig,desmateria)
    datos = materia.getMateria()
    datos = ';'.join(datos)
    archiMateria.escribir([datos],"a")

def periodos():
    borrarPantalla()
    gotoxy(20,2);print("MANTENIMIENTO DE PERIODOS")
    gotoxy(15,4);print("Periodo: ")
    gotoxy(15,5);print("Descripcion Periodos: ")
    gotoxy(36,5)
    desperiodo = input()
    archiPeriodo = Archivo("./datos/periodo.txt",";")
    periodo = archiPeriodo.leer()
    if periodo : idSig = int(periodo[-1][0])+1
    else: idSig=1
    periodo = Periodo(idSig,desperiodo)
    datos = periodo.getPeriodo()
    datos = ';'.join(datos)
    archiPeriodo.escribir([datos],"a")

def profesores():
    borrarPantalla()
    validar = Valida()
    gotoxy(20,2);print("INGRESO DE PROFESORES")
    gotoxy(15,4);print("Nombre  : ")
    gotoxy(15,5);print("Cedula  : ")
    gotoxy(15,6);print("Titulo  : ")
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
    gotoxy(15,9);print("Esta seguro de Grabar El registro(s/n):")
    gotoxy(54,9);grabar = input().lower()
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
    gotoxy(20,2);print("INGRESO DE ESTUDIANTES")
    gotoxy(15,4);print("Nombre  : ")
    gotoxy(15,5);print("Cedula  : ")
    gotoxy(15,6);print("Direccion  : ")
    gotoxy(15,7);print("Telefono: ")
    gotoxy(15,8);print("Carrera ID[    ]: ")
    gotoxy(25,4);nom = input()
    gotoxy(25,5);ced = input()
    gotoxy(28,6);direc = input()
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
    gotoxy(15,9);print("Esta seguro de Grabar El registro(s/n):")
    gotoxy(54,9);grabar = input().lower()
    if grabar == "s":
        archiEstudiante = Archivo("./datos/estudiante.txt")
        lisEstudiante = archiEstudiante.leer()
        if lisEstudiante : idSig = int(lisEstudiante[-1][0])+1
        else: idSig=1
        entEstudiante = Estudiante(idSig,nom,ced,entCarrera,direc,tel)
        datos = entEstudiante.getEstudiante()
        datos = ';'.join(datos)
        archiEstudiante.escribir([datos],"a")
        gotoxy(15,11);input("Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...")
    else:
        gotoxy(15,11);input("Registro No fue Grabado\n presione una tecla para continuar...")

def matricula():
    borrarPantalla()
    validar = Valida()
    gotoxy(20,2);print("INGRESO DE MATRICULACION")
    gotoxy(15,4);print("Valor : ")
    gotoxy(15,5);print("Estudiante ID[    ] : ")
    gotoxy(15,6);print("Carrera ID[    ]: ")
    gotoxy(15,7);print("Periodo ID[    ]: ")
    # gotoxy(25,4);per = input()
    # gotoxy(25,5);est = input()
    # gotoxy(25,6);mat = input()
    # gotoxy(25,7);prof = input()
    valor=validar.solo_numeros("Error: Solo numeros",25,4)
    lisEstudiante,entEstudiante = [],None
    while not lisEstudiante:
        gotoxy(30,5);id = input().upper()
        archiEstudiante = Archivo("./datos/estudiante.txt")
        lisEstudiante = archiEstudiante.buscar(id)
        if lisEstudiante:
            entEstudiante = Estudiante(lisEstudiante[0],lisEstudiante[1],lisEstudiante[2],lisEstudiante[3],lisEstudiante[4])
            gotoxy(36,5);print(entEstudiante.nombre)
        else:
            gotoxy(36,5);print("No existe Estudiante con ese codigo[{}]:".format(id))
            time.sleep(1);gotoxy(36,5);print(" "*40)
    lisCarrera,entCarrera = [],None
    while not lisCarrera:
        gotoxy(27,6);id = input().upper()
        archiCarrera = Archivo("./datos/carrera.txt")
        lisCarrera = archiCarrera.buscar(id)
        if lisCarrera:
            entCarrera = Carrera(lisCarrera[0],lisCarrera[1])
            gotoxy(33,6);print(entCarrera.descripcion)
        else:
            gotoxy(33,6);print("No existe Carrera con ese codigo[{}]:".format(id))
            time.sleep(1);gotoxy(33,6);print(" "*40)
    lisPeriodo,entPeriodo = [],None
    while not lisPeriodo:
        gotoxy(27,7);id = input().upper()
        archiPeriodo = Archivo("./datos/periodo.txt")
        lisPeriodo = archiPeriodo.buscar(id)
        if lisPeriodo:
            entPeriodo = Periodo(lisPeriodo[0],lisPeriodo[1])
            gotoxy(33,7);print(entPeriodo.descripcion)
        else:
            gotoxy(33,7);print("No existe Periodo con ese codigo[{}]:".format(id))
            time.sleep(1);gotoxy(33,7);print(" "*40)
    gotoxy(15,11);print("Esta seguro de Grabar El registro(s/n):")
    gotoxy(54,11);grabar = input().lower()
    if grabar == "s":
        archiMatricula = Archivo("./datos/matricula.txt")
        lisMatricula = archiMatricula.leer()
        if lisMatricula : idSig = int(lisMatricula[-1][0])+1
        else: idSig=1
        entMatricula = Matricula(idSig,entPeriodo,entEstudiante,entCarrera,valor)
        datos = entMatricula.getMatricula()
        datos = ';'.join(datos)
        archiMatricula.escribir([datos],"a")
        gotoxy(15,11);input("Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...")
    else:
        gotoxy(15,11);input("Registro No fue Grabado\n presione una tecla para continuar...")

def notas():
    borrarPantalla()
    validar = Valida()
    gotoxy(20,2);print("INGRESO DE NOTAS")
    gotoxy(15,4);print("Periodo ID[   ]: ")
    gotoxy(15,5);print("Estudiante ID[   ]: ")
    gotoxy(15,6);print("Materia ID[   ]: ")
    gotoxy(15,7);print("Profesor ID[   ]: ")
    gotoxy(15,8);print("Nota1: ")
    gotoxy(15,9);print("Nota2: ")
    not1=validar.solo_numeros("Error: Solo numeros",25,8)
    not2=validar.solo_numeros("Error: Solo numeros",25,9)
    lisPeriodo,entPeriodo = [],None
    while not lisPeriodo:
        gotoxy(27,4);id = input().upper()
        archiPeriodo = Archivo("./datos/periodo.txt")
        lisPeriodo = archiPeriodo.buscar(id)
        if lisPeriodo:
            entPeriodo = Periodo(lisPeriodo[0],lisPeriodo[1])
            gotoxy(33,4);print(entPeriodo.descripcion)
        else:
            gotoxy(33,4);print("No existe Periodo con ese codigo[{}]:".format(id))
            time.sleep(1);gotoxy(33,4);print(" "*40)
    lisEstudiante,entEstudiante = [],None
    while not lisEstudiante:
        gotoxy(27,4);id = input().upper()
        archiEstudiante = Archivo("./datos/estudiante.txt")
        lisEstudiante = archiEstudiante.buscar(id)
        if lisEstudiante:
            entEstudiante = Estudiante(lisEstudiante[0],lisEstudiante[1],lisEstudiante[2],lisEstudiante[3],lisEstudiante[4])
            gotoxy(33,4);print(entEstudiante.nombre)
        else:
            gotoxy(33,5);print("No existe Estudiante con ese codigo[{}]:".format(id))
            time.sleep(1);gotoxy(33,5);print(" "*40)
    lisMateria,entMateria = [],None
    while not lisMateria:
        gotoxy(27,6);id = input().upper()
        archiMateria = Archivo("./datos/materia.txt")
        lisMateria = archiMateria.buscar(id)
        if lisMateria:
            entMateria = Materia(lisMateria[0],lisMateria[1])
            gotoxy(33,6);print(entMateria.descripcion)
        else:
            gotoxy(33,6);print("No existe Materia con ese codigo[{}]:".format(id))
            time.sleep(1);gotoxy(33,6);print(" "*40)
    lisProfesor,entProfesor = [],None
    while not lisProfesor:
        gotoxy(27,7);id = input().upper()
        archiProfesor = Archivo("./datos/profesor.txt")
        lisProfesor = archiProfesor.buscar(id)
        if lisProfesor:
            entProfesor = Profesor(lisProfesor[0],lisProfesor[1],lisProfesor[2],lisProfesor[3],lisProfesor[4],lisProfesor[5])
            gotoxy(33,7);print(entProfesor.nombre)
        else:
            gotoxy(33,7);print("No existe Profesor con ese codigo[{}]:".format(id))
            time.sleep(1);gotoxy(33,7);print(" "*40)
    gotoxy(15,11);print("Esta seguro de Grabar El registro(s/n):")
    gotoxy(54,11);grabar = input().lower()
    if grabar == "s":
        archiNotas = Archivo("./datos/notas.txt")
        lisNotas = archiNotas.leer()
        if lisNotas : idSig = int(lisNotas[-1][0])+1
        else: idSig=1
        entNotas = Nota(idSig,entPeriodo,entEstudiante,entMateria,entProfesor,not1,not2)
        datos = entNotas.getNotas()
        datos = ';'.join(datos)
        archiNotas.escribir([datos],"a")
        gotoxy(15,11);input("Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...")
    else:
        gotoxy(15,11);input("Registro No fue Grabado\n presione una tecla para continuar...")

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
                materia()
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
                matricula()
            # elif opc2 == "2":
            #     pass

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