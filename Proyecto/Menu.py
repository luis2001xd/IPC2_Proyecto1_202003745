from colorama import Fore
import xml.etree.ElementTree as ET
from Paciente import paciente
from Paciente import lista_paciente
npacientes=lista_paciente()


def menu():
    print(Fore.YELLOW+"------------Bienvenido usuario ♣--------------")
    opcion=""
    
    while opcion!=4:
        opcion_ejecucion=""
        print()
        print(Fore.CYAN+"------------Menú---------------")
        print()
        print(Fore.CYAN+"1. Cargar Archivo")
        print(Fore.CYAN+"2. Ver pacientes")
        print(Fore.CYAN+"3. Elegir paciente")
        print(Fore.CYAN+"4.Salir")
        print()
        opcion=int(input())
        if opcion==1:
            cargar_archivo("prueba.xml")
            print("Archivo cargado con éxito :)")

        if opcion==2:
            npacientes.print()

        if opcion==3:
            print("Escoja su paciente")
            paciente=input()
            paciente_buscado=npacientes.buscar(paciente)
            if paciente_buscado is None:
                print(Fore.RED+("El paciente no ha sido encontrado"))
            else:
                while opcion_ejecucion != 3:
                    print(Fore.GREEN+"1. Ejecutar períodos proporcionados por el xml")
                    print(Fore.GREEN+"2. Ejecutar períodos hasta que la enfermedad sea grave")
                    print(Fore.GREEN+"3. Salir")
                    opcion_ejecucion=int(input())
                    
                    if opcion_ejecucion == 1:
                        print("Patrón inicial:")
                        
                        print(paciente_buscado.paciente.celula.imprimir())
                        x=1
                        while x<=paciente_buscado.paciente.periodo:
                            print()
                            print("__________________________________________\n")
                            print("Período No",x)
                            print()
                            paciente_buscado.paciente.celula.periodos()
                            print(paciente_buscado.paciente.celula.imprimir())
                            x+=1
                    npacientes.delete()
                    cargar_archivo("prueba.xml")
                    paciente_buscado=npacientes.buscar(paciente)

                    if opcion_ejecucion==2:
                        print("Patrón inicial:")
                        
                        print(paciente_buscado.paciente.celula.imprimir())
                        x=1
                        while x<=10000:
                            print()
                            print("__________________________________________\n")
                            print("Período No",x)
                            print()
                            paciente_buscado.paciente.celula.periodos()
                            print(paciente_buscado.paciente.celula.imprimir())
                            x+=1
                    npacientes.delete()
                    cargar_archivo("prueba.xml")
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
        periodo=nuevo_paciente.find("periodos").text
        periodo_entero=int(periodo)

        #creación de un nuevo paciente
        paciente_nuevo=paciente(nombre,edad_entero,tamano_entero,periodo_entero)
        npacientes.append(paciente_nuevo)
        paciente_nuevo.celula.append()
        
        #creación de rejilla
        #lectura de filas y columnas contagiadas
        for celda in nuevo_paciente.iter("celda"):
            fila_entero=int(celda.attrib["f"])
            columna_entero=int(celda.attrib["c"])
            paciente_nuevo.celula.cambio_celula(fila_entero,columna_entero)
        
            
    
    
        


    

 
   
        


menu()