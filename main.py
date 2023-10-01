from queue import Queue
from agente import Agente
import manager as mn

mapa = [
    ['UTA',          'MALL', 'av eloy alfaro', 'wefsdf',        'calle ficoa'],
    ['calle aaa',    'av jjj',      'av sss',         'calle aac',  'calle aba'],
    ['calle bbb',    'av kkk',      'av ttt',         'calle aad',  'calle aca'],
    ['calle ccc',    'av lll',      'av uuu',         'calle aae',  'calle ada'],
    ['calle ddd',    'av mmm',      'av vvv',         'calle aaf',  'calle aea'],
    ['calle eee',    'av nnn',      'av www',         'calle aag',  'calle afa'],
    ['calle fff',    'wbdghf',      'gjfgsf',         'calle aah',  'calle aga'],
    ['calle ggg',    'av ppp',      'av yyy',         'fgdg',  'calle aha'],
    ['calle hhh',    'av qqq',      'dfgdf',         'calle aaj',  'calle ata'],
    ['calle iii',    'av rrr',      'dgfgdg',         'calle aak',  'calle axa'],
]


puntoInicial = mn.obtenerUbicacion('UTA', mapa)
puntoObjetivo = mn.obtenerUbicacion('MALL', mapa)
print(f'UTA {puntoInicial}')
print(f'MALL {puntoObjetivo}')

raiz = Agente()
raiz.inicio(mapa, puntoInicial, puntoObjetivo)

cola = Queue()
cola.put(raiz)

solucion:Agente = None
print('buscando solucion ...')
while not cola.empty():
    estadoActual:Agente = cola.get()
    if estadoActual.esObjetivo(): # control si es objetivo
        solucion = estadoActual
        print('solucion encontrada ...')
        break
    nuevosEstados = mn.ejecutarMovimientos(mn.generarHijos(estadoActual, 4))
    for nuevo in nuevosEstados:
        cola.put(nuevo)
        
mapaVacio = mn.dibujarMapaVacio(len(mapa), len(mapa[0]))
mn.dibujarRutaSolucion(solucion, mapaVacio)
solucion.mostrarcaminoRecorrido()