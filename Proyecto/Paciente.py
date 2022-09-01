
from Celula import lista_celulas
from Rejilla import lista_rejilla
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



