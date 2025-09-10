import random

# --- Parámetros de la simulación ---
GRID_SIZE = 5
NUM_FRUITS = 8

# Crear el huerto
def crear_huerto():
    grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    ocupados = set()

    while len(ocupados) < NUM_FRUITS:
        x, y = random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1)
        if (x, y) not in ocupados:
            ocupados.add((x, y))
            grid[x][y] = random.randint(1, 9)  # Nivel de madurez

    return grid


# Mostrar huerto
def mostrar_huerto(grid, agente_pos):
    for i in range(GRID_SIZE):
        fila = ""
        for j in range(GRID_SIZE):
            if (i, j) == agente_pos:
                fila += " A "
            elif grid[i][j] > 0:
                fila += f" {grid[i][j]} "
            else:
                fila += " . "
        print(fila)
    print()

# Calcular utilidad: fruta más madura y cercana
def calcular_utilidad(fruta_madurez, distancia):
    if fruta_madurez > 3:
        utilidad = fruta_madurez/(distancia+1)
    else:
        utilidad = 0
    return utilidad


# Encontrar fruta con mayor utilidad
def mejor_objetivo(grid, agente_pos):
    mejor = None
    mejor_utilidad = -1

    ax, ay = agente_pos
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if grid[i][j] > 0:
                distancia = abs(ax - i) + abs(ay - j)
                utilidad = calcular_utilidad(grid[i][j], distancia)
                if utilidad == 0:
                    break
                if utilidad > mejor_utilidad:
                    mejor_utilidad = utilidad
                    mejor = (i, j)
    return mejor

# Mover agente un paso hacia el objetivo
def mover_hacia(agente_pos, objetivo):
    ax, ay = agente_pos
    ox, oy = objetivo

    if ax < ox:
        ax += 1
    elif ax > ox:
        ax -= 1
    elif ay < oy:
        ay += 1
    elif ay > oy:
        ay -= 1
    return (ax, ay)

# --- Simulación ---
def simular():
    huerto = crear_huerto()
    agente_pos = (0, 0)

    while True:
        mostrar_huerto(huerto, agente_pos)
        objetivo = mejor_objetivo(huerto, agente_pos)
        if not objetivo:
            print("Se recolectaron todas las frutas listas para cosecha")
            break

        if agente_pos == objetivo:
            print(f"Recolectando fruta en {objetivo} (madurez {huerto[objetivo[0]][objetivo[1]]})")
            huerto[objetivo[0]][objetivo[1]] = 0  # Recoge fruta
        else:
            agente_pos = mover_hacia(agente_pos, objetivo)

# Ejecutar
simular()

