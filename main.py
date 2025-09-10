import random

# --- Parámetros de la simulación ---
GRID_SIZE = 5 # Tamaño del lado del huerto (cuadrado)
NUM_FRUITS = 8 # Número de frutas que aparecerán en el campo de cosecha

# Crear el huerto
def crear_huerto():
    grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)] # Crea el huerto vacío
    ocupados = set() # Colección con las celdas ya ocupadas

    while len(ocupados) < NUM_FRUITS:
        x, y = random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1)
        if (x, y) not in ocupados:
            ocupados.add((x, y))
            grid[x][y] = random.randint(1, 9)  # Representa una fruta en el huerto por su nivel de madurez (del 1 al 9)

    return grid


# Mostrar huerto
def mostrar_huerto(grid, agente_pos):
    for i in range(GRID_SIZE):
        fila = ""
        for j in range(GRID_SIZE):
            if (i, j) == agente_pos: # Muestra la posición del agente con una "A"
                fila += " A "
            elif grid[i][j] > 0: # Muestra la fruta por su nivel de madurez
                fila += f" {grid[i][j]} "
            else: # Muestra las celdas vacías con un "."
                fila += " . "
        print(fila)
    print()

# Calcular utilidad: fruta más madura y cercana
def calcular_utilidad(fruta_madurez, distancia):
    if fruta_madurez > 3: # Si la fruta está lo suficientemente madura (nivel > 3), calcula su utilidad
        utilidad = fruta_madurez/(distancia+1)
    else: # Si la fruta no está lo suficientemente madura deja su utilidad al mínimo
        utilidad = 0
    return utilidad


# Encontrar fruta con mayor utilidad
def mejor_objetivo(grid, agente_pos):
    mejor = None
    mejor_utilidad = -1

    ax, ay = agente_pos
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if grid[i][j] > 0: # Si la celda tiene fruta, pasa a calcular el mejor objetivo
                distancia = abs(ax - i) + abs(ay - j) # Distancia del agente a la fruta
                utilidad = calcular_utilidad(grid[i][j], distancia) # Calcula la utilidad
                if utilidad == 0: # Si la utilidad es 0 (fruta muy inmadura) se pasa a evaluar la siguiente celda
                    break
                if utilidad > mejor_utilidad: # Si la utilidad es la mejor hasta el momento, se guarda su valor y su posicion
                    mejor_utilidad = utilidad
                    mejor = (i, j)
    return mejor

# Mover agente un paso hacia el objetivo
def mover_hacia(agente_pos, objetivo):
    ax, ay = agente_pos # Posición del agente
    ox, oy = objetivo # Posición del objetivo

    # Mueve al agente una celda a la vez, comparando la posicion del agente con la del objetivo
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
    huerto = crear_huerto() # Crea el huerto
    agente_pos = (0, 0) # Inicializa en la esquina superior izquierda al agente

    while True:
        mostrar_huerto(huerto, agente_pos) #Muestra al huerto
        objetivo = mejor_objetivo(huerto, agente_pos) # Determina el objetivo en base a su utilidad
        if not objetivo: # Si en la función la variable "mejor" es igual a "None"
            print("Se recolectaron todas las frutas listas para cosecha")
            break

        if agente_pos == objetivo: # Si el agente esta en la celda objetivo, recolecta la fruta
            print(f"Recolectando fruta en {objetivo} (madurez {huerto[objetivo[0]][objetivo[1]]})")
            huerto[objetivo[0]][objetivo[1]] = 0  # Recoge fruta
        else:
            agente_pos = mover_hacia(agente_pos, objetivo)

# Ejecutar
simular()

