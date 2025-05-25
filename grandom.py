import argparse
import random
from collections import deque

def generar(gran_total):
    numeros = []
    rangos = deque()
    rangos.append((0, 9999))  # Rango inicial

    while len(numeros) < gran_total and rangos:
        ini, fin = rangos.popleft()

        if ini >= fin:
            continue

        nuevo = random.randint(ini + 1, fin - 1) if fin - ini > 1 else ini
        numeros.append(nuevo)

        # Añadir nuevos rangos izquierdo y derecho
        rangos.append((ini, nuevo))
        rangos.append((nuevo, fin))

    return numeros[:gran_total]

def main():
    parser = argparse.ArgumentParser(description='Generador jerárquico de números aleatorios.')
    parser.add_argument('-q', '--quantity', type=int, default=10, help='Cantidad de números a generar (ej: 40)')
    args = parser.parse_args()

    resultado = generar(args.quantity)

    for i, n in enumerate(resultado, start=1):
        print(f"n{i:02} = {n:04d}")

if __name__ == '__main__':
    main()
