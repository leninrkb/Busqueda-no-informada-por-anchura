from agente import Agente

def obtenerUbicacion(objetivo:str, matriz:list[list[str]]):
    filas = len(matriz)
    columnas = len(matriz[0])
    for i in range(filas):
        for j in range(columnas):
            if matriz[i][j] == objetivo:
                return (i, j)
    return None

def generarHijos(padre:Agente, cantidad:int): # funcion sucesor 
    hijos = []
    for i in range(cantidad):
        nuevoHijo = Agente(padre)
        hijos.append(nuevoHijo)
    return hijos

def ejecutarMovimientos(agentes:list[Agente]):
    metodos = ['movArriba','movAbajo','movIzquierda','movDerecha']
    posibles = [] 
    for index, agente in enumerate(agentes):
        if getattr(agente, metodos[index])():
            posibles.append(agente)
    return posibles

def dibujarMapaVacio(filas:int, columnas:int):
    mapa = [['_'] * columnas for _ in range(filas)]
    return mapa

def dibujarRutaSolucion(agente:Agente, mapa:list[list[str]]):    
    for punto in agente.caminoRecorrido:
        mapa[punto[0]][punto[1]] = '#'
    for fila in mapa:
        print(fila)   