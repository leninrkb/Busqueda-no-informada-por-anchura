class Agente():
    def __init__(self, agente=None):
        if agente == None:
            self.alto = 0 
            self.ancho = 0
            self.puntoInicial = (0,0) 
            self.puntoObjetivo = (0,0)
            self.puntoActual = (0,0)
            self.caminoRecorrido = [] 
        else:
            self.alto = agente.alto
            self.ancho = agente.ancho
            self.puntoInicial = agente.puntoInicial
            self.puntoObjetivo = agente.puntoObjetivo
            self.puntoActual = agente.puntoActual
            self.caminoRecorrido = agente.caminoRecorrido
        
    def inicio(self, matriz:list[list[str]], puntoInicial:tuple, puntoObjetivo:tuple):
        self.alto = len(matriz)
        self.ancho = len(matriz[0])
        self.puntoInicial = puntoInicial
        self.puntoObjetivo = puntoObjetivo
        self.puntoActual = self.puntoInicial
        self.caminoRecorrido.append(self.puntoActual)
    
    def movArriba(self)->bool:
        if not self.puntoActual[0] - 1 < 0:
            self.puntoActual = (self.puntoActual[0] - 1, self.puntoActual[1])
            return True
        return False

    def movAbajo(self)->bool:
        if not self.puntoActual[0] + 1 > self.alto - 1:
            self.puntoActual = (self.puntoActual[0] + 1, self.puntoActual[1])
            return True
        return False

    def movIzquierda(self)->bool:
        if not self.puntoActual[1] - 1 < 0:
            self.puntoActual = (self.puntoActual[0], self.puntoActual[1] - 1)
            return True
        return False
    
    def movDerecha(self)->bool:
        if not self.puntoActual[1] + 1 > self.ancho - 1:
            self.puntoActual = (self.puntoActual[0], self.puntoActual[1] + 1)
            return True
        return False