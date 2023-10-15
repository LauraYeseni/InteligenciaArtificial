from collections import deque
import copy

# Se define el estado inicial y el estado objetivo del rompecabezas
ESTADO_INICIAL = [[7, 2, 4], [5, 0, 6], [8, 3, 1]]
ESTADO_OBJETIVO = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

# Función para verificar si dos estados son iguales
def estados_iguales(estado1, estado2):
    return all(estado1[i][j] == estado2[i][j] for i in range(3) for j in range(3))

# Función para obtener los movimientos posibles a partir de un estado
def obtener_movimientos_posibles(estado):
    posicion_cero = None
    for i in range(3):
        for j in range(3):
            if estado[i][j] == 0:
                posicion_cero = (i, j)
                break
    movimientos = []
    DIRECCIONES = [(1, 0, "derecha"), (-1, 0, "izquierda"), (0, 1, "abajo"), (0, -1, "arriba")]

    for direccion in DIRECCIONES:
        nueva_i, nueva_j, direccion_texto = posicion_cero[0] + direccion[0], posicion_cero[1] + direccion[1], direccion[2]
        if 0 <= nueva_i < 3 and 0 <= nueva_j < 3:
            nuevo_estado = copy.deepcopy(estado)
            nuevo_estado[posicion_cero[0]][posicion_cero[1]] = estado[nueva_i][nueva_j]
            nuevo_estado[nueva_i][nueva_j] = 0
            movimientos.append((nuevo_estado, (posicion_cero, (nueva_i, nueva_j), direccion_texto)))

    return movimientos

# Función para resolver
def resolver_rompecabezas(estado_inicial, estado_objetivo):
    cola = deque([(estado_inicial, [], 0)])  # Se crea una cola con (Estado inicial, camino recorrido y costo)
    visitados = set()

    while cola:
        estado_actual, camino, costo = cola.popleft()

        if estados_iguales(estado_actual, estado_objetivo):  # Comprueba si el estado actual es igual al objetivo
            return camino, costo

        visitados.add(tuple(map(tuple, estado_actual)))  

        for siguiente_estado, coordenadas in obtener_movimientos_posibles(estado_actual):
            if tuple(map(tuple, siguiente_estado)) not in visitados:
                nueva_camino = camino + [(coordenadas, siguiente_estado)]
                cola.append((siguiente_estado, nueva_camino, costo + 1))  # Aumenta el costo


camino_solucion, costo = resolver_rompecabezas(ESTADO_INICIAL, ESTADO_OBJETIVO)

# Imprime la matriz y los movimientos detallados en cada paso
for i, (coordenadas, estado) in enumerate(camino_solucion):
    movimiento = estado[coordenadas[0][0]][coordenadas[0][1]]
    desde = coordenadas[0]
    a = coordenadas[1]
    direccion = coordenadas[2]
    print(f"Paso {i} (Mover {movimiento} desde {desde} a {a} ({direccion})):")
    for fila in estado:
        print(fila)
    print()

# Imprime el número total de movimientos
print(f"Número total de movimientos: {costo}")

