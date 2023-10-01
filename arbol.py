from graphviz import Digraph

# Crear un objeto Digraph
grafo = Digraph()

# Agregar nodos al grafo
grafo.node("A", "Nodo A")
grafo.node("B", "Nodo B")
grafo.node("C", "Nodo C")
grafo.node("C", "Nodo C")
grafo.node("C", "Nodo C")

# Agregar aristas (conexiones) entre nodos
grafo.edge("A", "B")
grafo.edge("A", "C")

# Guardar el grafo en un archivo (opcional)
grafo.render("arbol_busqueda", view=True)

# Ver el grafo en una ventana emergente (si tienes Graphviz instalado)
# grafo.view()

