
from Celula import lista_celulas
from Rejilla import lista_rejilla
import os
class paciente:
    def __init__(self,nombre,edad,tamano,periodo,estado=None,periodo_repetido=None,numero=None,siguiente=None,anterior=None) -> None:
        self.nombre=nombre
        self.edad=edad
        self.tamano=tamano
        self.periodo=periodo
        self.rejilla=lista_rejilla(periodo)
        self.celula=lista_celulas(tamano,periodo)
        self.estado=estado
        self.periodo_repetido=periodo_repetido
        self.numero=numero


class nodo_paciente:
    def __init__(self,paciente=None,siguiente=None) -> None:
        self.paciente=paciente
        self.siguiente=siguiente



class lista_paciente:
    def __init__(self):
        self.primero=None
    
    def append(self,nuevopaciente):
        if self.primero is None:
            nuevo=nodo_paciente(paciente=nuevopaciente)
            self.primero=nuevo
        else:
            aux=self.primero
            while aux.siguiente!=None:
                aux=aux.siguiente
            nuevo=nodo_paciente(paciente=nuevopaciente)
            aux.siguiente=nuevo

    def print(self):
        nodoaux=self.primero
        while nodoaux!=None:
            print("Nombre:",nodoaux.paciente.nombre,"Edad:",nodoaux.paciente.edad,"Períodos:",nodoaux.paciente.periodo,"Tamaño matriz",nodoaux.paciente.tamano)
            nodoaux=nodoaux.siguiente


    def buscar(self,nombre):
        nodoaux=self.primero
        while nodoaux.paciente.nombre!=nombre:
            if nodoaux.siguiente!=None:
                nodoaux=nodoaux.siguiente
            else:
                print("Paciente no encontrado")
                return  None
        return nodoaux

    def delete(self):
        if self.primero is not None:
            self.primero=None


    def generar_xml(self):
        nodoaux=self.primero
        cadena="<?xml version=\"1.0\" encoding=\"UTF-8\"?> \n"
        cadena+="<pacientes> \n"
        while nodoaux!=None:
            cadena+="   <paciente>\n"
            cadena+="      <datospersonales>\n"
            cadena+="         <nombre>"+nodoaux.paciente.nombre+"</nombre>\n"
            cadena+="         <edad>"+str(nodoaux.paciente.edad)+"</edad>\n"
            cadena+="      </datospersonales>\n"
            cadena+="      <periodos>"+str(nodoaux.paciente.periodo)+"</periodos>\n"
            cadena+="      <tamano>"+str(nodoaux.paciente.tamano)+"</tamano>\n"
            cadena+="      <resultado>"+nodoaux.paciente.estado+"</resultado>\n"
            cadena+="      <n>"+str(nodoaux.paciente.periodo_repetido)+"</n>\n"
            cadena+="      <n1>"+str(nodoaux.paciente.numero)+"</n1>\n"
            nodoaux=nodoaux.siguiente

        cadena+="</pacientes>"
        file = open("Resultados.xml", "w")
        file.write(cadena)
        file.close() 




