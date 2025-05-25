import argparse
import random
from collections import deque

def generar(gran_total, longitud):
    max_value = 10 ** longitud - 1
    numeros = []
    rangos = deque()
    rangos.append((0, max_value))

    while len(numeros) < gran_total and rangos:
        ini, fin = rangos.popleft()

        if ini >= fin:
            continue

        nuevo = random.randint(ini + 1, fin - 1) if fin - ini > 1 else ini
        if nuevo not in numeros:
            numeros.append(nuevo)

        rangos.append((ini, nuevo))
        rangos.append((nuevo, fin))

    return numeros[:gran_total]

def generar_con_seed(gran_total, longitud, semilla_deseada):
    intentos = 0
    max_intentos = 1000  # Protección

    while intentos < max_intentos:
        resultado = generar(gran_total, longitud)
        if semilla_deseada in resultado:
            print(f"intentos realizados {intentos}")
            return resultado
        intentos += 1

    raise Exception(f"No se pudo generar una lista que contenga el número {semilla_deseada} después de {max_intentos} intentos.")

def main():
    parser = argparse.ArgumentParser(description='Generador jerárquico de números aleatorios.')
    parser.add_argument('-q', '--quantity', type=int, default=10, help='Cantidad de números a generar')
    parser.add_argument('-l', '--length', type=int, default=4, help='Longitud (ancho) de cada número. Ej: 3 → 000-999')
    parser.add_argument('-s', '--seedvalue', type=int, help='Número obligatorio que debe aparecer en el resultado')

    args = parser.parse_args()

    max_valor = 10 ** args.length
    if args.quantity > max_valor:
        parser.error(f"El valor de -q no puede ser mayor a {max_valor} para l={args.length}.")

    if args.seedvalue is not None and not (0 <= args.seedvalue < max_valor):
        parser.error(f"El valor de -s debe estar entre 0 y {max_valor - 1} para l={args.length}.")

    if args.seedvalue is not None:
        resultado = generar_con_seed(args.quantity, args.length, args.seedvalue)
    else:
        resultado = generar(args.quantity, args.length)

    for i, n in enumerate(resultado, start=1):
        print(f"n{i:02} = {n:0{args.length}d}")

if __name__ == '__main__':
    main()