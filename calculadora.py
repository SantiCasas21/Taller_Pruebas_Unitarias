import math

# Menu de la calculadora
# Esta calculadora permite realizar operaciones matemáticas avanzadas
def menu():
    print("\nCalculadora Interactiva")
    print("a. Seno")
    print("b. Coseno")
    print("c. Tangente")
    print("d. Inverso de Seno")
    print("e. Inverso de Coseno")
    print("f. Inverso de Tangente")
    print("g. x elevado a la y")
    print("h. Logaritmo base 10")
    print("i. Logaritmo Natural")
    print("j. Raíz Cuadrada")
    print("k. Raíz Enésima")
    print("l. Factorial de un número")
    print("m. 1/x")
    print("n. Pi")
    print("o. Seno hiperbólico")
    print("p. Coseno hiperbólico")
    print("q. Tangente hiperbólica")
    print("r. n C r")
    print("s. Salir")

def calculadora():
    while True:
        menu()
        opcion = input("Seleccione una opción: ").lower()

        # Validación de la opción
        # Se realiza un switch-case para determinar la opción seleccionada

        match opcion:
            case 'a':
                x = float(input("Ingrese el valor en radianes: "))
                print("El resultado es:", seno(x))
            case 'b':
                x = float(input("Ingrese el valor en radianes: "))
                print("El resultado es:", coseno(x))
            case 'c':
                x = float(input("Ingrese el valor en radianes: "))
                print("El resultado es:", tangente(x))
            case 'd':
                x = float(input("Ingrese el valor (entre -1 y 1): "))
                print("El resultado es:", inverso_seno(x))
            case 'e':
                x = float(input("Ingrese el valor (entre -1 y 1): "))
                print("El resultado es:", inverso_coseno(x))
            case 'f':
                x = float(input("Ingrese el valor: "))
                print("Inverso de Tangente:", inverso_tangente(x))
            case 'g':
                x = float(input("Ingrese la base: "))
                y = float(input("Ingrese el exponente: "))
                print("Resultado:", potencia(x, y))
            case 'h':
                x = float(input("Ingrese el número: "))
                print("Logaritmo base 10:", log_base10(x))
            case 'i':
                x = float(input("Ingrese el número: "))
                print("Logaritmo Natural:", log_natural(x))
            case 'j':
                x = float(input("Ingrese el número: "))
                print("Raíz Cuadrada:", raiz_cuadrada(x))
            case 'k':
                x = float(input("Ingrese el número: "))
                n = float(input("Ingrese el índice de la raíz: "))
                print("Raíz Enésima:", raiz_enesima(x, n))
            case 'l':
                x = int(input("Ingrese un número entero: "))
                print("Factorial:", factorial(x))
            case 'm':
                x = float(input("Ingrese el número: "))
                print("Inverso:", inverso(x))
            case 'n':
                print("Pi:", pi())
            case 'o':
                x = float(input("Ingrese el valor: "))
                print("Seno hiperbólico:", seno_hiperbolico(x))
            case 'p':
                x = float(input("Ingrese el valor: "))
                print("Coseno hiperbólico:", coseno_hiperbolico(x))
            case 'q':
                x = float(input("Ingrese el valor: "))
                print("Tangente hiperbólica:", tangente_hiperbolica(x))
            case 'r':
                n = int(input("Ingrese el valor de n: "))
                r = int(input("Ingrese el valor de r: "))
                print("Combinatoria:", combinatoria(n, r))
            case 's':
                print("Saliendo de la calculadora...")
                break
            case _:
                print("Opción no válida. Intente de nuevo.")

# Funciones matemáticas
# Estas funciones realizan operaciones matemáticas específicas

# Seno
def seno(x):
    return math.sin(x)

# Coseno
def coseno(x):
    return math.cos(x)

# Tangente
def tangente(x):
    return math.tan(x)

# Seno Inverso
def inverso_seno(x):
    if -1 <= x <= 1:
        return math.asin(x)
    else:
        raise ValueError("El valor debe estar entre -1 y 1")

# Coseno Inverso
def inverso_coseno(x):
    if -1 <= x <= 1:
        return math.acos(x)
    else:
        raise ValueError("El valor debe estar entre -1 y 1")

# Tangente Inverso
def inverso_tangente(x):
    return math.atan(x)

# Potencia
def potencia(x, y):
    return math.pow(x, y)

# Logaritmo base 10
def log_base10(x):
    if x <= 0:
        raise ValueError("El número debe ser mayor que cero")
    return math.log10(x)

# Logaritmo natural
def log_natural(x):
    if x <= 0:
        raise ValueError("El número debe ser mayor que cero")
    return math.log(x)

# Raíz cuadrada
def raiz_cuadrada(x):
    if x < 0:
        raise ValueError("No se puede calcular la raíz cuadrada de un número negativo")
    return math.sqrt(x)

# Raíz enésima
def raiz_enesima(x, n):
    if n == 0:
        raise ValueError("El índice de la raíz no puede ser cero")
    return x ** (1 / n)

# Factorial
def factorial(x):
    if x < 0:
        raise ValueError("No se puede calcular el factorial de un número negativo")
    return math.factorial(x)

# Inverso
def inverso(x):
    if x == 0:
        raise ValueError("No se puede dividir entre cero")
    return 1 / x

# Pi
def pi():
    return math.pi

# Seno hiperbólico
def seno_hiperbolico(x):
    return math.sinh(x)

# Coseno hiperbólico
def coseno_hiperbolico(x):
    return math.cosh(x)

# Tangente hiperbólica
def tangente_hiperbolica(x):
    return math.tanh(x)

# Combinatoria
def combinatoria(n, r):
    if n < r:
        raise ValueError("n debe ser mayor o igual a r")
    return math.comb(n, r)

if __name__ == "__main__":
    calculadora()
    

