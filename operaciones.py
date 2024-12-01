<<<<<<< HEAD

=======
>>>>>>> f527361d08d930595bb32a4f6b566f1eceb9ff4c
def validar_numeros(a, b):
    """
    Valida que ambos parámetros sean de tipo int o float.
    Lanza un ValueError si no son válidos.
    """
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise ValueError("Ambos parámetros deben ser de tipo int o float.")

def sumar(a, b):
    """
    Suma dos valores después de validar que sean números válidos.
    """
    validar_numeros(a, b)
    return a + b

def restar(a, b):
    """
    Resta dos valores después de validar que sean números válidos.
    """
    validar_numeros(a, b)
    return a - b

def multiplicar(a, b):
    """
    Multiplica dos valores sin usar el operador "*".
    La multiplicación se implementa como suma repetida.
    """
    validar_numeros(a, b)
<<<<<<< HEAD
    
=======
   
    # Convierte los números a positivos para manejar todos los casos
>>>>>>> f527361d08d930595bb32a4f6b566f1eceb9ff4c
    negativo = False
    if a < 0 and b < 0:
        a, b = -a, -b
    elif a < 0 or b < 0:
        negativo = True
        a, b = abs(a), abs(b)

    resultado = 0
<<<<<<< HEAD
    for _ in range(int(b)):
        resultado += a

    return -resultado if negativo else resultado

def dividir(a, b):
    """
    Divide dos valores sin usar el operador "/".
    Implementa la división como resta iterativa.
    """
    validar_numeros(a, b)
    
    if b == 0:
        raise ZeroDivisionError("No se puede dividir entre cero.")

    negativo = False
    if a < 0 and b < 0:
        a, b = -a, -b
    elif a < 0 or b < 0:
        negativo = True
        a, b = abs(a), abs(b)

    cociente = 0
    while a >= b:
        a -= b
        cociente += 1

    return -cociente if negativo else cociente
=======
    for _ in range(int(b)):  # Suma `a`, `b` veces
        resultado += a

    # Si uno de los números era negativo, el resultado será negativo
    return -resultado if negativo else resultado
>>>>>>> f527361d08d930595bb32a4f6b566f1eceb9ff4c

def factorial_iterativo(n):
    """
    Calcula el factorial de un número de forma iterativa.
    :param n: El número para calcular su factorial (debe ser un entero no negativo).
    :return: El factorial del número.
    :raises ValueError: Si el número no es un entero o es negativo.
    """
    if not isinstance(n, int):
        raise ValueError("El número debe ser un entero.")
    if n < 0:
        raise ValueError("El número no puede ser negativo.")
    
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial
