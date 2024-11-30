from operaciones import sumar, restar, multiplicar, dividir

def pedir_valores():
    """
    Solicita dos valores al usuario y los convierte a float.
    Devuelve una tupla con los dos valores.
    Si hay un error de conversión, lanza una excepción.
    """
    try:
        a = float(input("Introduce el primer valor: "))
        b = float(input("Introduce el segundo valor: "))
        return a, b
    except ValueError:
        raise ValueError("Ambos valores deben ser números válidos (int o float).")

def mostrar_menu():
    """
    Muestra un menú al usuario, pide una opción y realiza la operación correspondiente.
    """
    while True:
        print("\nMenú de Operaciones:")
        print("1 - Sumar")
        print("2 - Restar")
        print("3 - Multiplicar")
        print("4 - Dividir")
        print("5 - Salir")
       
        opcion = input("Introduce una opción: ")

        if opcion == "1":
            # Llamar a la función sumar
            try:
                a, b = pedir_valores()
                resultado = sumar(a, b)
                print(f"El resultado de la suma es: {resultado}")
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == "2":
            # Llamar a la función restar
            try:
                a, b = pedir_valores()
                resultado = restar(a, b)
                print(f"El resultado de la resta es: {resultado}")
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == "3":
            # Llamar a la función multiplicar
            try:
                a, b = pedir_valores()
                resultado = multiplicar(a, b)
                print(f"El resultado de la multiplicación es: {resultado}")
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == "4":
            # Llamar a la función dividir
            try:
                a, b = pedir_valores()
                resultado = dividir(a, b)
                print(f"El resultado de la división es: {resultado}")
            except ZeroDivisionError as e:
                print(f"Error: {e}")
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == "5":
            print("Saliendo del programa. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción entre 1 y 5.")
