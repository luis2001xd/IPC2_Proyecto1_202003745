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
        print(Fore.CYAN+"2. Ver pacientes cargados")
        print(Fore.CYAN+"3. Elegir paciente para realizar su respectivo análisis")
        print(Fore.CYAN+"4.Salir")
        print()
        opcion=int(input())
        if opcion==1:
            nombre_archivo=input("Introduzca la ruta del archivo \n")
            ruta=nombre_archivo
            cargar_archivo(ruta)
            print("Su archivo ha sido cargado con éxito :)")

        if opcion==2:
            npacientes.print()

        if opcion==3:
            print("Escoja su paciente")
            paciente=input()
            paciente_buscado=npacientes.buscar(paciente)
            if paciente_buscado is None:
                print(Fore.RED+("El paciente no ha sido encontrado"))
            else:
                while opcion_ejecucion != 2:
                    print(Fore.GREEN+"1. Ejecutar períodos proporcionados por el xml")
                    print(Fore.GREEN+"2. Salir")
                    opcion_ejecucion=int(input())
                    
                    
                    if opcion_ejecucion == 1:
                        print("Patrón inicial:")
                        
                        paciente_buscado.paciente.celula.imprimir()
                        x=1
                        rejilla=paciente_buscado.paciente.celula.retornar_rejillas()
                        paciente_buscado.paciente.rejilla.append(rejilla,x)
                        paciente_buscado.paciente.celula.graficar(x)
                        while x<=paciente_buscado.paciente.periodo:
                            print()
                            print("__________________________________________\n")
                            print("Período No",x)
                            print()
                            paciente_buscado.paciente.celula.periodos()
                            rejilla=paciente_buscado.paciente.celula.retornar_rejillas()
                            paciente_buscado.paciente.celula.imprimir()
                            x+=1
                            paciente_buscado.paciente.celula.graficar(x)
                            paciente_buscado.paciente.rejilla.append(rejilla,x)  
                        paciente_buscado.paciente.rejilla.verificar_repeticion()
                        print()
                        print("Períodos finalizados")
                        print()
                        print("---Aquí están los resultados---")
                        estado=paciente_buscado.paciente.rejilla.estado_paciente()
                        print("Tipo de enfermedad:",estado)
                        periodo=paciente_buscado.paciente.rejilla.periodoinfectado()
                        print("Periodo que se empieza a repetir:",periodo)
                        repeticiones=paciente_buscado.paciente.rejilla.repeticiones()
                        print("Cuantas veces se repite:",repeticiones)
                        inicial=paciente_buscado.paciente.rejilla.retornar_patron()
                        paciente_buscado.paciente.celula.volver_inicial(inicial)
                        paciente_buscado.paciente.rejilla.delete()
                        print()

                        
                        
                    

                    






            

        


def cargar_archivo(ruta):
    try:
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
                if celda.attrib=={}:
                    break
                fila_entero=int(celda.attrib["f"])
                columna_entero=int(celda.attrib["c"])
                paciente_nuevo.celula.cambio_celula(fila_entero,columna_entero)

            
            x=1
            rejilla=paciente_nuevo.celula.retornar_rejillas()
            paciente_nuevo.rejilla.append(rejilla,x)
            while x<=paciente_nuevo.periodo:
                paciente_nuevo.celula.periodos()
                rejilla=paciente_nuevo.celula.retornar_rejillas()
                x+=1
                paciente_nuevo.rejilla.append(rejilla,x)  
            #se verifica el estado del paciente 
            paciente_nuevo.rejilla.verificar_repeticion()
            estado=paciente_nuevo.rejilla.estado_paciente()
            paciente_nuevo.estado=estado
            periodo=paciente_nuevo.rejilla.periodoinfectado()
            paciente_nuevo.periodo_repetido=periodo
            repeticiones=paciente_nuevo.rejilla.repeticiones()
            paciente_nuevo.numero=repeticiones
            inicial=paciente_nuevo.rejilla.retornar_patron()
            paciente_nuevo.celula.volver_inicial(inicial)
            paciente_nuevo.rejilla.delete()
    except Exception as e:
        print("El archivo no fue cargado correctamente")       

def generar_xml(cadenaxml):
    cadena="<?xml version=\"1.0\" encoding=\"UTF-8\"?> \n"







    

 
   
        


menu()