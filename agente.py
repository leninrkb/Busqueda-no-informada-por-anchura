class Agente():
    caminoRecorrido = []
    def __init__(self, dimensionesMatriz:tuple, puntoInicial:tuple, puntoObjetivo:tuple):
        self.alto = dimensionesMatriz[0]
        self.ancho = dimensionesMatriz[1]
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