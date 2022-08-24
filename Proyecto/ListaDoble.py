from Celula import celula

class lista_doble:
    def __init__(self):
        self.primero=None

    def append(self,tamano):
        for i in range(tamano):
            for j in range (tamano):
                nueva_celula=celula(tipo="")