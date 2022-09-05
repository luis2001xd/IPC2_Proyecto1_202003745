from ast import Nonlocal


class rejilla:
    def __init__(self,datos,numero,anterior=None,siguiente=None) -> None:
        self.datos=datos
        self.numero=numero
        self.anterior=anterior
        self.siguiente=siguiente


class lista_rejilla:
    def __init__(self,periodo=None) -> None:
        self.primero=None
        self.periodo=periodo
        self.repeticion=None
        self.estado=None
        self.periodo_infectado=None
        


    def append(self,nueva,numero):
        if self.primero is None:
            nueva_rejilla=rejilla(nueva,numero)
            self.primero=nueva_rejilla

        else:
            nodoaux=self.primero
            while nodoaux.siguiente!=None:
                nodoaux=nodoaux.siguiente
            nueva_rejilla=rejilla(nueva,numero)
            nodoaux.siguiente=nueva_rejilla
            nueva_rejilla.anterior=nodoaux

    def imprimir(self):
        nodoaux=self.primero
        while nodoaux!=None:
            print(nodoaux.datos,":",nodoaux.numero)
            nodoaux=nodoaux.siguiente


    #función que determina el estado del paciente
    def verificar_repeticion(self):
        nodoaux=self.primero.siguiente
        nodo_secundario=nodoaux

            
        x=1

        while nodoaux.siguiente!=None:
            if nodoaux.datos==self.primero.datos:
                if nodoaux.siguiente!=None:
                    if nodoaux.datos==nodoaux.siguiente.datos:
                        self.estado="Mortal"
                        self.periodo_infectado="Patron inicial"
                        self.repeticion=x
                        return

                self.estado="Grave"
                self.periodo_infectado="Patron inicial"
                self.repeticion=x
                return
            nodoaux=nodoaux.siguiente
            x+=1

        nodoaux=self.primero.siguiente

        while nodoaux.siguiente!=None:
            x=1
            if nodoaux.datos==nodoaux.siguiente.datos:
                self.estado="Mortal"
                self.periodo_infectado=nodoaux.numero-1
                self.repeticion=x
                return
            else:
                nodo_secundario=nodoaux
                while nodo_secundario!=None:
                    if nodo_secundario.numero==nodoaux.numero:
                        nodo_secundario=nodo_secundario.siguiente
                        continue
                    else:
                        if nodoaux.datos==nodo_secundario.datos:
                            if nodo_secundario.siguiente!=None:
                                if nodo_secundario.siguiente.datos==nodo_secundario.datos: #se verifica si la enfermedad es mortal
                                    self.estado="Mortal"
                                    self.periodo_infectado=nodoaux.numero-1
                                    self.repeticion=x
                                    return
                            #sino es mortal pero no se repite seguido, significa que será grave
                            self.estado="Grave"
                            self.periodo_infectado=nodoaux.numero-1
                            self.repeticion=x
                            return
                        else:
                            nodo_secundario=nodo_secundario.siguiente
                            x+=1
            nodoaux=nodoaux.siguiente
            nodo_secundario=nodoaux
        self.estado="Leve"
        self.periodo_infectado= "Ninguno"
        self.repeticion= "Ninguno"
        return



    def retornar_patron(self):
        return self.primero.datos



    def delete(self):
        self.primero=None

    def estado_paciente(self):
        return self.estado

    def periodoinfectado(self):
        return self.periodo_infectado

    def repeticiones(self):
        return self.repeticion

        








