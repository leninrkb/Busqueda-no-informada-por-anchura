from agente import Agente

def obtenerUbicacion(objetivo:str, matriz:list[list[str]]):
    filas = len(matriz)
    columnas = len(matriz[0])
    for i in range(filas):
        for j in range(columnas):
            if matriz[i][j] == objetivo:
                return (i, j)
    return None