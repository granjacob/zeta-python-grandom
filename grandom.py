import argparse
import random
from collections import deque

def generar(gran_total, longitud):
    max_value = 10 ** longitud - 1
    numeros = []
    rangos = deque()
    rangos.append((0, max_value))  # Rango inicial

    while len(numeros) < gran_total and rangos:
        ini, fin = rangos.popleft()

        if ini >= fin:
            continue

        # Elegir número aleatorio dentro del rango válido
        nuevo = random.randint(ini + 1, fin - 1) if fin - ini > 1 else ini
        numeros.append(nuevo)

        # Agregar nuevos sub-rangos
        rangos.append((ini, nuevo))
        rangos.append((nuevo, fin))

    return numeros[:gran_total], longitud

def main():
    parser = argparse.ArgumentParser(description='Generador jerárquico de números aleatorios.')
    parser.add_argument('-q', '--quantity', type=int, default=10, help='Cantidad de números a generar')
    parser.add_argument('-l', '--length', type=int, default=4, help='Longitud (ancho) de cada número. Ej: 3 → 000-999')

    args = parser.parse_args()
    resultado, longitud = generar(args.quantity, args.length)

    for i, n in enumerate(resultado, start=1):
        print(f"n{i:02} = {n:0{longitud}d}")

if __name__ == '__main__':
    main()