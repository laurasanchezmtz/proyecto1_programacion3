"""
Proyecto 1: Algoritmo de Dijkstra
Programación 3

Encuentra la ruta más corta entre un nodo origen y un nodo destino
en un grafo ponderado (ej. red de transporte entre estaciones).
"""


class Nodo:
    """Un nodo del grafo (ciudad, estación, router...)."""

    def __init__(self, nombre):
        self.nombre = nombre
        self.vecinos = {}  # {nombre_vecino: peso}

    def __repr__(self):
        return f"Nodo({self.nombre})"


class Grafo:
    """Grafo ponderado no dirigido, representado con lista de adyacencia."""

    def __init__(self):
        self.nodos = {}  # {nombre: Nodo}

    def agregar_nodo(self, nombre):
        if nombre not in self.nodos:
            self.nodos[nombre] = Nodo(nombre)

    def agregar_conexion(self, origen, destino, peso):
        if peso < 0:
            raise ValueError("Dijkstra no funciona con pesos negativos.")
        # Si los nodos no existen todavía, se crean
        self.agregar_nodo(origen)
        self.agregar_nodo(destino)
        # Conexión en ambos sentidos (grafo no dirigido)
        self.nodos[origen].vecinos[destino] = peso
        self.nodos[destino].vecinos[origen] = peso

    def mostrar(self):
        print("Conexiones del grafo:")
        for nombre, nodo in self.nodos.items():
            conexiones = ", ".join(f"{v}({p})" for v, p in nodo.vecinos.items())
            print(f"  {nombre} -> {conexiones}")

    def dijkstra(self, inicio, destino):
        """Regresa (distancia_total, camino) del nodo inicio al nodo destino."""
        if inicio not in self.nodos or destino not in self.nodos:
            raise KeyError("El nodo origen o destino no existe en el grafo.")

        distancias = {}
        anteriores = {}
        visitados = set()

        # PASO 1 - Inicializar: origen en 0 y los demás en infinito
        for nombre in self.nodos:
            distancias[nombre] = float("inf")
            anteriores[nombre] = None
        distancias[inicio] = 0

        while len(visitados) < len(self.nodos):
            # PASO 2 - Seleccionar: el nodo no visitado con menor distancia
            nodo_actual = None
            menor_distancia = float("inf")
            for nombre in self.nodos:
                if nombre not in visitados and distancias[nombre] < menor_distancia:
                    menor_distancia = distancias[nombre]
                    nodo_actual = nombre

            # Si no quedan nodos alcanzables, terminamos
            if nodo_actual is None:
                break

            # Si llegamos al destino, ya tenemos su distancia mínima
            if nodo_actual == destino:
                break

            # PASO 4 - Marcar como visitado
            visitados.add(nodo_actual)

            # PASO 3 - Relajar: actualizar el costo de los vecinos
            for vecino, peso in self.nodos[nodo_actual].vecinos.items():
                nueva_distancia = distancias[nodo_actual] + peso
                # Solo se actualiza si el nuevo camino es estrictamente más corto
                if nueva_distancia < distancias[vecino]:
                    distancias[vecino] = nueva_distancia
                    anteriores[vecino] = nodo_actual

        # Si el destino quedó en infinito, no hay camino
        if distancias[destino] == float("inf"):
            return float("inf"), []

        # Reconstruir el camino usando la tabla de anteriores
        camino = []
        actual = destino
        while actual is not None:
            camino.append(actual)
            actual = anteriores[actual]
        camino.reverse()

        return distancias[destino], camino


def mostrar_resultado(grafo, inicio, destino):
    try:
        distancia, camino = grafo.dijkstra(inicio, destino)
    except KeyError as error:
        print(f"Error: {error}")
        return

    if not camino:
        print(f"No existe camino de {inicio} a {destino}.")
    else:
        print(f"Ruta más corta de {inicio} a {destino}: {' -> '.join(camino)}")
        print(f"Distancia/costo total: {distancia}")


def ejemplo_de_clase():
    """Grafo visto en la presentación: el camino óptimo de A a D es A -> C -> D = 4."""
    grafo = Grafo()
    grafo.agregar_conexion("A", "B", 10)
    grafo.agregar_conexion("A", "C", 2)
    grafo.agregar_conexion("B", "D", 1)
    grafo.agregar_conexion("C", "D", 2)
    return grafo


def red_de_transporte():
    """Red de transporte más grande (pesos en minutos entre estaciones)."""
    grafo = Grafo()
    grafo.agregar_conexion("A", "B", 4)
    grafo.agregar_conexion("A", "C", 2)
    grafo.agregar_conexion("B", "C", 1)
    grafo.agregar_conexion("B", "D", 5)
    grafo.agregar_conexion("C", "D", 8)
    grafo.agregar_conexion("C", "E", 10)
    grafo.agregar_conexion("D", "E", 2)
    grafo.agregar_conexion("D", "F", 6)
    grafo.agregar_conexion("E", "F", 3)
    return grafo


def main():
    print("=== Ejemplo de clase ===")
    grafo1 = ejemplo_de_clase()
    grafo1.mostrar()
    mostrar_resultado(grafo1, "A", "D")

    print("\n=== Red de transporte ===")
    grafo2 = red_de_transporte()
    grafo2.mostrar()
    print("Nodos disponibles:", ", ".join(grafo2.nodos))
    inicio = input("Nodo origen: ").strip().upper()
    destino = input("Nodo destino: ").strip().upper()
    mostrar_resultado(grafo2, inicio, destino)


if __name__ == "__main__":
    main()
