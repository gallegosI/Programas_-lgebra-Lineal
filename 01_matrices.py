#================================
#   Jimenez Gallegos Ivan
#================================
#   Algebra lineal
#   Matematica Algoritmica
#   ESFM-IPN    febrero-2025
#================================

#   Matrices

class Matriz:
    # Constructor de la clase Matriz. Inicializa una matriz de tamaño filas x columnas con ceros.
    def __init__(self, filas, columnas, nombre):
        self.filas = filas
        self.columnas = columnas
        self.nombre = nombre
        self.matriz = [[0 for _ in range(columnas)] for _ in range(filas)]

    # Método para representar la matriz como una cadena de texto.
    def __str__(self):
        return f'Matriz {self.nombre}:\n' + '\n'.join([' '.join(map(str, fila)) for fila in self.matriz])

    # Método para llenar la matriz con valores ingresados por el usuario.
    def llenar_matriz(self):
        print(f'\nLlenando la matriz {self.nombre}:')
        for i in range(self.filas):
            for j in range(self.columnas):
                self.matriz[i][j] = int(input(f'Ingrese el elemento [{i+1},{j+1}]: '))

    # Método para sumar dos matrices. Solo se pueden sumar si tienen las mismas dimensiones.
    def suma(self, otra_matriz):
        if self.filas != otra_matriz.filas or self.columnas != otra_matriz.columnas:
            raise ValueError("Las matrices deben tener las mismas dimensiones para sumarse.")
        
        resultado = Matriz(self.filas, self.columnas, f'({self.nombre}+{otra_matriz.nombre})')
        for i in range(self.filas):
            for j in range(self.columnas):
                resultado.matriz[i][j] = self.matriz[i][j] + otra_matriz.matriz[i][j]
        return resultado

    # Método para restar dos matrices. Solo se pueden restar si tienen las mismas dimensiones.
    def resta(self, otra_matriz):
        if self.filas != otra_matriz.filas or self.columnas != otra_matriz.columnas:
            raise ValueError("Las matrices deben tener las mismas dimensiones para restarse.")
        
        resultado = Matriz(self.filas, self.columnas, f'({self.nombre}-{otra_matriz.nombre})')
        for i in range(self.filas):
            for j in range(self.columnas):
                resultado.matriz[i][j] = self.matriz[i][j] - otra_matriz.matriz[i][j]
        return resultado

    # Método para multiplicar dos matrices. La cantidad de columnas de la primera debe coincidir con la cantidad de filas de la segunda.
    def multiplicacion(self, otra_matriz):
        if self.columnas != otra_matriz.filas:
            raise ValueError("El número de columnas de la primera matriz debe ser igual al número de filas de la segunda matriz.")
        
        resultado = Matriz(self.filas, otra_matriz.columnas, f'({self.nombre}*{otra_matriz.nombre})')
        for i in range(self.filas):
            for j in range(otra_matriz.columnas):
                for k in range(self.columnas):
                    resultado.matriz[i][j] += self.matriz[i][k] * otra_matriz.matriz[k][j]
        return resultado

# Función para mostrar todas las matrices almacenadas.
def mostrar_matrices(matrices):
    print("\nMatrices disponibles:")
    for nombre, matriz in matrices.items():
        print(matriz)

# Función principal que maneja el menú de opciones.
def main():
    matrices = {}  # Diccionario para almacenar las matrices creadas.
    letra = 'A'    # Nombre inicial de las matrices.

    while True:
        print("\n--- Menú ---")
        print("1. Ingresar una nueva matriz")
        print("2. Realizar operaciones con matrices")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            # Creación de una nueva matriz.
            filas = int(input(f"Ingrese el número de filas para la matriz {letra}: "))
            columnas = int(input(f"Ingrese el número de columnas para la matriz {letra}: "))
            matriz = Matriz(filas, columnas, letra)
            matriz.llenar_matriz()
            matrices[letra] = matriz
            letra = chr(ord(letra) + 1)  # Se avanza a la siguiente letra del abecedario.

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

            if operacion in ['1', '2', '3', '4']:
                matriz1 = input("Ingrese el nombre de la primera matriz (ej. A): ").upper()
                matriz2 = input("Ingrese el nombre de la segunda matriz (ej. B): ").upper()
                
                if operacion == '4':
                    matriz3 = input("Ingrese el nombre de la tercera matriz (ej. C): ").upper()
                
                try:
                    if operacion == '1':
                        resultado = matrices[matriz1].suma(matrices[matriz2])
                    elif operacion == '2':
                        resultado = matrices[matriz1].resta(matrices[matriz2])
                    elif operacion == '3':
                        resultado = matrices[matriz1].multiplicacion(matrices[matriz2])
                    elif operacion == '4':
                        suma = matrices[matriz1].suma(matrices[matriz2])
                        resultado = matrices[matriz3].multiplicacion(suma)
                        print("\nResultado de C*(A+B):")
                    
                    print("\nResultado:")
                    print(resultado)
                except KeyError:
                    print("Error: Una de las matrices no existe.")
                except ValueError as e:
                    print(e)

            else:
                print("Opción no válida.")

        elif opcion == '3':
            # Salida del programa.
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

# Punto de entrada del programa.
if __name__ == "__main__":
    main()

