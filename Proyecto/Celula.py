class celula:
    def __init__(self,tipo=None,anterior=None,siguiente=None,fila=None,columna=None):
        self.tipo=tipo
        self.fila=int(fila)
        self.columna=int(columna)
        self.siguiente=None
        self.anterior=None