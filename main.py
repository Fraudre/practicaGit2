from menu import mostrar_menu

def main():
    while True:
        opcion = mostrar_menu()
        if opcion == 5:
            print("Saliendo del programa...")
            break
        elif opcion == 1:
            print("Seleccionaste: Sumar")
        elif opcion == 2:
            print("Seleccionaste: Restar")
        elif opcion == 3:
            print("Seleccionaste: Multiplicar")
        elif opcion == 4:
            print("Seleccionaste: Dividir")

if __name__ == "__main__":
    main()
