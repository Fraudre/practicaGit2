from operaciones import sumar, restar, multiplicar, dividir, factorial_recursivo

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
        print("6 - Calcular el factorial de un número (recursivo)")  # Opción con número repetido
       
        opcion = input("Introduce una opción: ")

        if opcion == "1":
            try:
                a, b = pedir_valores()
                resultado = sumar(a, b)
                print(f"El resultado de la suma es: {resultado}")
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == "2":
            try:
                a, b = pedir_valores()
                resultado = restar(a, b)
                print(f"El resultado de la resta es: {resultado}")
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == "3":
            try:
                a, b = pedir_valores()
                resultado = multiplicar(a, b)
                print(f"El resultado de la multiplicación es: {resultado}")
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == "4":
            try:
                a, b = pedir_valores()
                resultado = dividir(a, b)
                print(f"El resultado de la división es: {resultado}")
            except ZeroDivisionError:
                print("Error: No se puede dividir entre cero.")
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == "6":
            # Calcular el factorial de un número recursivamente
            try:
                n = int(input("Introduce un número entero no negativo: "))
                resultado = factorial_recursivo(n)
                print(f"El factorial de {n} es: {resultado}")
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == "5":
            print("Saliendo del programa. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción entre 1 y 6.")
