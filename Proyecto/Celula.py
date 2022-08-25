

class celula:
    def __init__(self,tipo=None,anterior=None,siguiente=None,fila=None,columna=None):
        self.tipo=tipo
        self.fila=fila
        self.columna=columna
        self.siguiente=siguiente
        self.anterior=anterior
        



class listadoble_celula:
    def __init__(self):
        self.primero=None

    def append(self,tamano):
            
            for i in range(1,tamano+1):
                for j in range(1,tamano+1):

                    if self.primero is None:
                       nueva_celula=celula(tipo="1",fila=i,columna=j)
                       self.primero=nueva_celula
                       nodo_aux=self.primero


                    else:
                        
                        nueva_celula=celula(tipo="1",fila=i,columna=j)
                        nodo_aux.siguiente=nueva_celula
                        nueva_celula.anterior=nodo_aux
                        nodo_aux=nodo_aux.siguiente
                        
    def print(self,tamano):
        aux=self.primero
        x=1
        
        for i in range(1,tamano+1):
            print("Fila",x,"| ",end="")
            for j in range(1,tamano+1):
                print(aux.tipo,end=" ")
                aux=aux.siguiente
            x+=1
            print()




