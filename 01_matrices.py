#================================
#   Jimenez Gallegos Ivan
#================================
#   Algebra lineal
#   Matematica Algoritmica
#   ESFM-IPN    febrero-2025
#================================

#   Matrices

class Matriz:
    def __init__(self, filas, columnas, nombre):
        self.filas = filas
        self.columnas = columnas
        self.nombre = nombre
        self.matriz = [[0 for _ in range(columnas)] for _ in range(filas)]

    def __str__(self):
        return f'Matriz {self.nombre}:\n' + '\n'.join([' '.join(map(str, fila)) for fila in self.matriz])

    def llenar_matriz(self):
        print(f'\nLlenando la matriz {self.nombre}:')
        for i in range(self.filas):
            for j in range(self.columnas):
                self.matriz[i][j] = int(input(f'Ingrese el elemento [{i+1},{j+1}]: '))

    def suma(self, otra_matriz):
        if self.filas != otra_matriz.filas or self.columnas != otra_matriz.columnas:
            raise ValueError("Las matrices deben tener las mismas dimensiones para sumarse.")

        resultado = Matriz(self.filas, self.columnas, f'({self.nombre}+{otra_matriz.nombre})')
        for i in range(self.filas):
            for j in range(self.columnas):
                resultado.matriz[i][j] = self.matriz[i][j] + otra_matriz.matriz[i][j]
        return resultado

    def resta(self, otra_matriz):
        if self.filas != otra_matriz.filas or self.columnas != otra_matriz.columnas:
            raise ValueError("Las matrices deben tener las mismas dimensiones para restarse.")

        resultado = Matriz(self.filas, self.columnas, f'({self.nombre}-{otra_matriz.nombre})')
        for i in range(self.filas):
            for j in range(self.columnas):
                resultado.matriz[i][j] = self.matriz[i][j] - otra_matriz.matriz[i][j]
        return resultado

    def multiplicacion(self, otra_matriz):
        if self.columnas != otra_matriz.filas:
            raise ValueError("El número de columnas de la primera matriz debe ser igual al número de filas de la segunda matriz.")

        resultado = Matriz(self.filas, otra_matriz.columnas, f'({self.nombre}*{otra_matriz.nombre})')
        for i in range(self.filas):
            for j in range(otra_matriz.columnas):
                for k in range(self.columnas):
                    resultado.matriz[i][j] += self.matriz[i][k] * otra_matriz.matriz[k][j]
        return resultado

# Función para mostrar las matrices disponibles
def mostrar_matrices(matrices):
    print("\nMatrices disponibles:")
    for nombre, matriz in matrices.items():
        print(matriz)

# Función principal
def main():
    matrices = {}  # Diccionario para almacenar las matrices
    letra = 'A'    # Letra inicial para nombrar las matrices

    while True:
        print("\n--- Menú ---")
        print("1. Ingresar una nueva matriz")
        print("2. Realizar operaciones con matrices")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            # Ingresar una nueva matriz
            filas = int(input(f"Ingrese el número de filas para la matriz {letra}: "))
            columnas = int(input(f"Ingrese el número de columnas para la matriz {letra}: "))
            matriz = Matriz(filas, columnas, letra)
            matriz.llenar_matriz()
            matrices[letra] = matriz
            letra = chr(ord(letra) + 1)  # Avanzar a la siguiente letra del abecedario

        elif opcion == '2':
            if len(matrices) < 2:
                print("Necesitas al menos dos matrices para realizar operaciones.")
                continue

            mostrar_matrices(matrices)
            print("\nOperaciones disponibles:")
            print("1. Sumar dos matrices")
            print("2. Restar dos matrices")
            print("3. Multiplicar dos matrices")
            print("4. Sumar dos matrices y multiplicar el resultado por una tercera")
            operacion = input("Seleccione una operación: ")

            if operacion == '1':
                # Sumar dos matrices
                matriz1 = input("Ingrese el nombre de la primera matriz (ej. A): ").upper()
                matriz2 = input("Ingrese el nombre de la segunda matriz (ej. B): ").upper()
                try:
                    resultado = matrices[matriz1].suma(matrices[matriz2])
                    print("\nResultado de la suma:")
                    print(resultado)
                except KeyError:
                    print("Error: Una de las matrices no existe.")
                except ValueError as e:
                    print(e)

            elif operacion == '2':
                # Restar dos matrices
                matriz1 = input("Ingrese el nombre de la primera matriz (ej. A): ").upper()
                matriz2 = input("Ingrese el nombre de la segunda matriz (ej. B): ").upper()
                try:
                    resultado = matrices[matriz1].resta(matrices[matriz2])
                    print("\nResultado de la resta:")
                    print(resultado)
                except KeyError:
                    print("Error: Una de las matrices no existe.")
                except ValueError as e:
                    print(e)

            elif operacion == '3':
                # Multiplicar dos matrices
                matriz1 = input("Ingrese el nombre de la primera matriz (ej. A): ").upper()
                matriz2 = input("Ingrese el nombre de la segunda matriz (ej. B): ").upper()
                try:
                    resultado = matrices[matriz1].multiplicacion(matrices[matriz2])
                    print("\nResultado de la multiplicación:")
                    print(resultado)
                except KeyError:
                    print("Error: Una de las matrices no existe.")
                except ValueError as e:
                    print(e)

            elif operacion == '4':
                # Sumar dos matrices y multiplicar el resultado por una tercera
                matriz1 = input("Ingrese el nombre de la primera matriz (ej. A): ").upper()
                matriz2 = input("Ingrese el nombre de la segunda matriz (ej. B): ").upper()
                matriz3 = input("Ingrese el nombre de la tercera matriz (ej. C): ").upper()
                try:
                    suma = matrices[matriz1].suma(matrices[matriz2])
                    resultado = matrices[matriz3].multiplicacion(suma)
                    print("\nResultado de C*(A+B):")
                    print(resultado)
                except KeyError:
                    print("Error: Una de las matrices no existe.")
                except ValueError as e:
                    print(e)

            else:
                print("Opción no válida.")

        elif opcion == '3':
            # Salir del programa
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    main()
