from colorama import Fore
import xml.etree.ElementTree as ET
from xml.dom import minidom
from Paciente import paciente
from Paciente import lista_paciente
npacientes=lista_paciente()


def menu():
    print(Fore.YELLOW+"------------Bienvenido usuario ♣--------------")
    opcion=""
    while opcion!=4:
        
        print()
        print(Fore.CYAN+"------------Menú---------------")
        print()
        print(Fore.CYAN+"1. Cargar Archivo")
        print(Fore.CYAN+"2. Imprimir pacientes")
        print(Fore.CYAN+"3. Elegir paciente")
        print(Fore.CYAN+"4.Salir")
        print()
        opcion=int(input())
        if opcion==1:
            cargar_archivo("prueba.xml")
            print("Archivo cargado con éxito")

        if opcion==2:
            npacientes.print()

        if opcion==3:
            print("Escoja su paciente")
            paciente=input()
            paciente_buscado=npacientes.buscar(paciente)
            

        


def cargar_archivo(ruta):
    tree = ET.parse(ruta)
    pacientes = tree.getroot()
    

    for nuevo_paciente in pacientes.findall("paciente"):
        datos_personales=nuevo_paciente.find("datospersonales")
        nombre=datos_personales.find("nombre").text
        edad=datos_personales.find("edad").text

        #covertir mis variables a enteros
        edad_entero=int(edad)
        tamano=nuevo_paciente.find("m").text
        tamano_entero=int(tamano)
        periodo=nuevo_paciente.find("periodos")
        periodo_entero=int(periodo)

        #creación de un nuevo paciente
        paciente_nuevo=paciente(nombre,edad_entero,tamano_entero,periodo_entero)
        npacientes.append(paciente_nuevo)

        #lectura de filas y columnas contagiadas
        for x in pacientes.findall("rejilla"):
            for y in x.findall("celda"):
                fila=y.get("f")
                columna=y.get("c")
                print(fila,columna)
    
    
        


    

 
   
        


menu()