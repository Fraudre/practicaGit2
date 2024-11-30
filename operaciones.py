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
   
    # Convierte los números a positivos para manejar todos los casos
    negativo = False
    if a < 0 and b < 0:
        a, b = -a, -b
    elif a < 0 or b < 0:
        negativo = True
        a, b = abs(a), abs(b)

    resultado = 0
    for _ in range(int(b)):  # Suma `a`, `b` veces
        resultado += a

    # Si uno de los números era negativo, el resultado será negativo
    return -resultado if negativo else resultado
