print("¡Bienvenido a Piedra, Papel o Tijera!")

nombre = input("Ingresa tu nombre: ")

if nombre.lower() == "salir":
    print("Juego cancelado.")
else:
    jugador = nombre
    jugar = True
    while jugar:
        print("\nElige:")
        print("1. Piedra")
        print("2. Papel")
        print("3. Tijera")

        opcion = input("Tu elección (1-3): ")

        if opcion.lower() == "salir":
            jugar = False
        else:
            if opcion in ["1", "2", "3"]:
                jugada_jugador = int(opcion)

                import random
                jugada_pc = random.randint(1, 3)

                if jugada_jugador == jugada_pc:
                    resultado = "Empate"
                elif (jugada_jugador == 1 and jugada_pc == 3) or \
                     (jugada_jugador == 2 and jugada_pc == 1) or \
                     (jugada_jugador == 3 and jugada_pc == 2):
                    resultado = "Ganaste"
                else:
                    resultado = "Perdiste"

                print(f"\n{resultado}!")
                print(f"PC eligió: {jugada_pc}")

                repetir = input("¿Jugar otra vez? (s/n): ").lower()
                if repetir != "s":
                    jugar = False
            else:
                print("Opción inválida. Intenta de nuevo.")
                continue

print("\n¡Gracias por jugar!")







