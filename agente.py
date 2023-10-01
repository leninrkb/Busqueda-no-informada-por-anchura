class Agente():
    caminoRecorrido = []
    def __init__(self, dimensionesMatriz:tuple, puntoInicial:tuple, puntoObjetivo:tuple):
        self.ancho = dimensionesMatriz[0]
        self.alto = dimensionesMatriz[1]
        self.puntoInicial = puntoInicial
        self.puntoObjetivo = puntoObjetivo
        self.puntoActual = self.puntoInicial
        self.caminoRecorrido.append(self.puntoActual)
    
    def movArriba(self)->bool:
        return False