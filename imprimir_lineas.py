def imprimirLineas(archivo, pares_o_impares):
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            lineas = f.readlines()

        total_lineas = len(lineas)
        caracteres_desplegados = 0

        print("Resultado:")
        for i, linea in enumerate(lineas, start=1):
            if (pares_o_impares == "pares" and i % 2 == 0) or (pares_o_impares == "impares" and i % 2 != 0):
                linea = linea.strip()  # Elimina espacios en blanco al inicio y final
                print(f'"{linea}" - {len(linea)} caracteres')
                caracteres_desplegados += len(linea)

        print(f"El archivo tiene {total_lineas} lineas")
        print(f"Fueron desplegados {caracteres_desplegados} caracteres")

    except FileNotFoundError:
        print(f"Error: El archivo '{archivo}' no existe.")
    except Exception as e:
        print(f"Error: {e}")


def main():
    archivo = input("Nombre del archivo: ")
    pares_o_impares = input("Pares o impares: ").strip().lower()

    if pares_o_impares not in ["pares", "impares"]:
        print("Error: Debes ingresar 'pares' o 'impares'.")
        return

    imprimirLineas(archivo, pares_o_impares)


# Llamada a la subrutina principal
if __name__ == "__main__":
    main()