
import os
class celula:
    def __init__(self,tipo=None,anterior=None,siguiente=None,fila=None,columna=None):
        self.tipo=tipo
        self.fila=fila
        self.columna=columna
        self.siguiente=siguiente
        self.anterior=anterior
        



class lista_celulas:
    def __init__(self,tamano,periodo):
        self.periodo=periodo
        self.tamano=tamano
        self.primero=None

#append crea la matriz

    def append(self,fila=None,columna=None,tipo=None):
        if fila==None and columna==None and tipo==None:        
            for i in range(1,self.tamano+1):
                for j in range(1,self.tamano+1):
                        
                    if self.primero is None:
                        nueva_celula=celula(tipo="0",fila=i,columna=j)
                        self.primero=nueva_celula
                        nodo_aux=self.primero

                    else:
                        nueva_celula=celula(tipo="0",fila=i,columna=j,anterior=nodo_aux)
                        nodo_aux.siguiente=nueva_celula
                        nueva_celula.anterior=nodo_aux
                        nodo_aux=nodo_aux.siguiente
        else:
            
            if fila==1 and columna==1:
                self.primero=celula(fila=fila,columna=columna,tipo=tipo,siguiente=None)
                
            else:
                nodo_aux=self.primero
                while nodo_aux.siguiente!=None:
                    nodo_aux=nodo_aux.siguiente
                nueva_celula=celula(fila=fila,columna=columna,tipo=tipo,siguiente=None)
                nodo_aux.siguiente=nueva_celula
                nueva_celula.anterior=nodo_aux
        
                
                    

 #se imprime el patrón inicial                       
                        
    def imprimir(self):
        aux=self.primero
        for i in range(1,self.tamano+1):
            print("x","| ",end="")
            for j in range(1,self.tamano+1):
                print(aux.tipo,end=" ")
                aux=aux.siguiente      
            print()


#se realizo el respectivo cambio de celulas a contagiadas
    def cambio_celula(self,fila,columna):
        aux=self.primero
        for i in range(1,self.tamano+1):
            for j in range(1,self.tamano+1):
                if aux.fila==fila:
                    if aux.columna==columna:
                        aux.tipo="1"
                aux=aux.siguiente


#realizar los períodos de las celulas

    def periodos(self):
        x=0
        celula_estudiada=self.primero
        vecino_siguiente=self.primero
        vecino_anterior=self.primero
       
        fila_siguiente=0
        columna_estudiada=0
        
        while x!=self.tamano*self.tamano: 
            contador_contagiadas=0
            fila_siguiente=0
            columna_estudiada=0
            fila_anterior=0

            #Para los extremos, la primera y última fila, última columna y primera columna son casos especiales
            #si celula está en un extremo es un caso especial
            #si la celula está en la primera fila y primer columna
            if celula_estudiada.fila==1:
                if celula_estudiada.columna==1:
                    if celula_estudiada.siguiente.tipo=="1":
                        contador_contagiadas+=1
                    fila_siguiente=celula_estudiada.fila+1
                    columna_estudiada=celula_estudiada.columna
                    vecino_siguiente=celula_estudiada

                    
                    while vecino_siguiente.fila!=fila_siguiente or vecino_siguiente.columna!=columna_estudiada:
                        vecino_siguiente=vecino_siguiente.siguiente
                    if vecino_siguiente.tipo=="1":
                        contador_contagiadas+=1
                    if vecino_siguiente.siguiente.tipo=="1":
                        contador_contagiadas+=1

                #para las células de la primera fila, siempre y cuando no sea la última
                if celula_estudiada.columna!=self.tamano and celula_estudiada.columna!=1 and celula_estudiada.columna!=self.tamano:
                    if celula_estudiada.siguiente.tipo=="1":
                        contador_contagiadas+=1
                    if celula_estudiada.anterior.tipo=="1":
                        contador_contagiadas+=1

                    fila_siguiente=celula_estudiada.fila+1
                    columna_estudiada=celula_estudiada.columna
                    vecino_siguiente=celula_estudiada.siguiente
                    while vecino_siguiente.fila!=fila_siguiente or vecino_siguiente.columna!=columna_estudiada:
                        vecino_siguiente=vecino_siguiente.siguiente
                        
                    if vecino_siguiente.anterior.tipo=="1":
                        contador_contagiadas+=1

                    if vecino_siguiente.siguiente.tipo=="1":
                        contador_contagiadas+=1

                    if vecino_siguiente.tipo=="1":
                        contador_contagiadas+=1
                   
                #si la celula estudiada es la última de la primera fila
                if celula_estudiada.fila==1 and celula_estudiada.columna==self.tamano:
                    if celula_estudiada.anterior.tipo=="1":
                        contador_contagiadas+=1

                    fila_siguiente=celula_estudiada.fila+1
                    columna_estudiada=celula_estudiada.columna
                    vecino_siguiente=celula_estudiada.siguiente
                    while vecino_siguiente.fila!=fila_siguiente or vecino_siguiente.columna!=columna_estudiada:
                        vecino_siguiente=vecino_siguiente.siguiente

                    if vecino_siguiente.anterior.tipo=="1":
                        contador_contagiadas+=1

                    if vecino_siguiente.tipo=="1":
                        contador_contagiadas+=1


            #si la celula estudiada pertenece a la primera columna y no sea de la última fila
            if celula_estudiada.columna==1 and celula_estudiada.fila!=self.tamano and celula_estudiada.fila!=1:
                if celula_estudiada.siguiente.tipo=="1":
                    contador_contagiadas+=1

                columna_estudiada=celula_estudiada.columna
                fila_anterior=celula_estudiada.fila-1
                fila_siguiente=celula_estudiada.fila+1
                vecino_siguiente=celula_estudiada.siguiente
                vecino_anterior=celula_estudiada.anterior

                while vecino_anterior.fila!=fila_anterior or vecino_anterior.columna!=columna_estudiada:
                    vecino_anterior=vecino_anterior.anterior

                if vecino_anterior.tipo=="1":
                    contador_contagiadas+=1
                
                if vecino_anterior.siguiente.tipo=="1":
                    contador_contagiadas+=1

                
                while vecino_siguiente.fila!=fila_siguiente or vecino_siguiente.columna!=columna_estudiada:
                    vecino_siguiente=vecino_siguiente.siguiente

                if vecino_siguiente.tipo=="1":
                    contador_contagiadas+=1

                if vecino_siguiente.siguiente.tipo=="1":
                    contador_contagiadas+=1


            #para los extremos de la última fila
            #extremo de la columna 1

            if celula_estudiada.columna==1 and celula_estudiada.fila==self.tamano:
                if celula_estudiada.siguiente.tipo=="1":
                    contador_contagiadas+=1

                columna_estudiada=celula_estudiada.columna
                fila_anterior=celula_estudiada.fila-1
                vecino_anterior=celula_estudiada.anterior
                while vecino_anterior.fila!=fila_anterior or vecino_anterior.columna!=columna_estudiada:
                    vecino_anterior=vecino_anterior.anterior

                if vecino_anterior.tipo=="1":
                    contador_contagiadas+=1

                if vecino_anterior.siguiente.tipo=="1":
                    contador_contagiadas+=1



            #para las células de la última fila siempre y cuando no sean los extremos

            if celula_estudiada.fila==self.tamano and celula_estudiada.columna!=self.tamano and celula_estudiada.columna!=1:

                if celula_estudiada.anterior.tipo=="1":
                    contador_contagiadas+=1

                if celula_estudiada.siguiente.tipo=="1":
                    contador_contagiadas+=1

                
                columna_estudiada=celula_estudiada.columna
                fila_anterior=celula_estudiada.fila-1
                vecino_anterior=celula_estudiada.anterior


                while vecino_anterior.fila!=fila_anterior or vecino_anterior.columna!=columna_estudiada:
                    vecino_anterior=vecino_anterior.anterior


            
                if vecino_anterior.tipo=="1":
                    contador_contagiadas+=1

                if vecino_anterior.siguiente.tipo=="1":
                    contador_contagiadas+=1

                if vecino_anterior.anterior.tipo=="1":
                    contador_contagiadas+=1


        #para la celula que está en el último extremo:

            if celula_estudiada.columna==self.tamano and celula_estudiada.fila==self.tamano:
                if celula_estudiada.anterior.tipo=="1":
                    contador_contagiadas+=1
                
                fila_anterior=celula_estudiada.fila-1
                columna_estudiada=celula_estudiada.columna
                vecino_anterior=celula_estudiada.anterior

                while vecino_anterior.fila!=fila_anterior or vecino_anterior.columna!=columna_estudiada:
                    vecino_anterior=vecino_anterior.anterior

                if vecino_anterior.tipo=="1":
                    contador_contagiadas+=1
                
                if vecino_anterior.anterior=="1":
                    contador_contagiadas+=1


        #para las celulas de la última columna

            if celula_estudiada.columna==self.tamano and celula_estudiada.fila!=1 and celula_estudiada.fila!=self.tamano:
                if celula_estudiada.anterior.tipo=="1":
                    contador_contagiadas+=1
                columna_estudiada=celula_estudiada.columna
                fila_anterior=celula_estudiada.fila-1
                fila_siguiente=celula_estudiada.fila+1
                vecino_siguiente=celula_estudiada.siguiente
                vecino_anterior=celula_estudiada.anterior

                while vecino_anterior.fila!=fila_anterior or vecino_anterior.columna!=columna_estudiada:
                    vecino_anterior=vecino_anterior.anterior

                if vecino_anterior.tipo=="1":
                    contador_contagiadas+=1
                
                if vecino_anterior.anterior.tipo=="1":
                    contador_contagiadas+=1

                
                while vecino_siguiente.fila!=fila_siguiente or vecino_siguiente.columna!=columna_estudiada:
                    vecino_siguiente=vecino_siguiente.siguiente

                if vecino_siguiente.tipo=="1":
                    contador_contagiadas+=1

                if vecino_siguiente.anterior.tipo=="1":
                    contador_contagiadas+=1

                

        #después de todas las validaciones quedan las celulas del centro

            if celula_estudiada.fila!=1 and celula_estudiada.columna!=1 and celula_estudiada.fila!=self.tamano and celula_estudiada.columna!=self.tamano:

                if celula_estudiada.siguiente.tipo=="1":
                    contador_contagiadas+=1

                if celula_estudiada.anterior.tipo=="1":
                    contador_contagiadas+=1

                fila_anterior=celula_estudiada.fila-1
                fila_siguiente=celula_estudiada.fila+1
                columna_estudiada=celula_estudiada.columna
                vecino_siguiente=celula_estudiada.siguiente
                vecino_anterior=celula_estudiada.anterior

                while vecino_anterior.fila!=fila_anterior or vecino_anterior.columna!=columna_estudiada:
                    vecino_anterior=vecino_anterior.anterior

                if vecino_anterior.tipo=="1":
                        contador_contagiadas+=1
                
                if vecino_anterior.anterior.tipo=="1":
                        contador_contagiadas+=1

                if vecino_anterior.siguiente.tipo=="1":
                        contador_contagiadas+=1



                while vecino_siguiente.fila!=fila_siguiente or vecino_siguiente.columna!=columna_estudiada:
                        vecino_siguiente=vecino_siguiente.siguiente

                if vecino_siguiente.tipo=="1":
                    contador_contagiadas+=1

                if vecino_siguiente.anterior.tipo=="1":
                    contador_contagiadas+=1

                
                if vecino_siguiente.siguiente.tipo=="1":
                    contador_contagiadas+=1

                #validaciones de las células
            if celula_estudiada.tipo=="1":
                if contador_contagiadas==3 or contador_contagiadas==2:
                    self.append(celula_estudiada.fila,celula_estudiada.columna,celula_estudiada.tipo)
                elif contador_contagiadas>=4 or contador_contagiadas<2:
                    self.append(celula_estudiada.fila,celula_estudiada.columna,"0")

            if celula_estudiada.tipo=="0":
                if contador_contagiadas==3:
                    self.append(celula_estudiada.fila,celula_estudiada.columna,"1")
                else:
                    self.append(celula_estudiada.fila,celula_estudiada.columna,celula_estudiada.tipo)
            x+=1
            celula_estudiada=celula_estudiada.siguiente
        


                



       
        


                    

                    
                            



                    

                    





    
        





