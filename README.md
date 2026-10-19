# Proyecto 1: Algoritmo de Dijkstra

Programación 3 — Implementación en Python 3 del algoritmo de Dijkstra para encontrar la ruta más corta en un grafo ponderado, usando Programación Orientada a Objetos.

## Estructura (POO)

| Clase | Responsabilidad |
|-------|-----------------|
| `Nodo` | Representa un nodo (ciudad, estación, router) y guarda sus vecinos con el peso de cada conexión. |
| `Grafo` | Guarda los nodos en una lista de adyacencia, agrega conexiones ponderadas y contiene el método `dijkstra(inicio, destino)`. |

## Cómo funciona el algoritmo

El método `dijkstra` usa tres estructuras de seguimiento:

- **distancias**: el menor costo conocido desde el origen hasta cada nodo.
- **anteriores**: el nodo previo de cada uno, para reconstruir el camino.
- **visitados**: los nodos cuyo costo ya es definitivo.

Y repite cuatro pasos:

1. **Inicializar**: el origen en 0 y los demás en infinito.
2. **Seleccionar**: el nodo no visitado con la menor distancia acumulada.
3. **Relajar**: actualizar el costo de sus vecinos si el nuevo camino es estrictamente más corto.
4. **Marcar**: agregar el nodo a visitados.

Al final, el camino se reconstruye recorriendo la tabla `anteriores` desde el destino hasta el origen.

## Cómo ejecutar

```bash
python dijkstra.py
```

El programa primero resuelve el ejemplo visto en clase y después pide un origen y un destino en la red de transporte.

## Ejemplo de salida

```
=== Ejemplo de clase ===
Ruta más corta de A a D: A -> C -> D
Distancia/costo total: 4

=== Red de transporte ===
Nodo origen: A
Nodo destino: F
Ruta más corta de A a F: A -> C -> B -> D -> E -> F
Distancia/costo total: 13
```

## Requisitos

- Python 3.x (sin librerías externas)
