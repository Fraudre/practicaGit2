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
        print("7 - Calcular el factorial de un número (recursivo)")  # Cambio de opción al número correcto
        print("8 - Calcular el Fibonacci de un número (iterativo)")
        
        opcion = input("Introduce una opción: ")

        if opcion == "1":
            # Código para la suma
            pass
        elif opcion == "2":
            # Código para la resta
            pass
        elif opcion == "3":
            # Código para la multiplicación
            pass
        elif opcion == "4":
            # Código para la división
            pass
        elif opcion == "7":
            # Código para el factorial recursivo
            pass
        elif opcion == "8":
            # Código para el Fibonacci iterativo
            pass
        elif opcion == "5":
            print("Saliendo del programa. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción entre 1 y 8.")
