def mostrar_menu():
    print("Selecciona una opción:")
    print("1 - Sumar")
    print("2 - Restar")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Salir")
    
    while True:
        try:
            opcion = int(input("Introduce el número de la opción: "))
            if 1 <= opcion <= 5:
                return opcion
            else:
                print("Por favor, selecciona un número entre 1 y 5.")
        except ValueError:
            print("Entrada no válida. Introduce un número.")
