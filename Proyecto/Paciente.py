from tkinter import N
from Celula import listasdoble_celula

class paciente:
    def __init__(self,nombre,edad,tamano,periodo,siguiente=None,anterior=None) -> None:
        self.nombre=nombre
        self.edad=edad
        self.tamano=tamano
        self.periodo=periodo
        self.celula=listasdoble_celula()
        


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
            print(nodoaux.paciente.nombre,nodoaux.paciente.edad)
            nodoaux=nodoaux.siguiente


    def buscar(self,nombre):
        nodoaux=self.primero
        while nodoaux.paciente.nombre!=nombre:
            if nodoaux.siguiente!=None:
                nodoaux=nodoaux.siguiente
            else:
                print("Paciente no encontrado")
                return  
        return nodoaux




