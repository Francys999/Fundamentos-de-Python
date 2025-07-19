user_option = input("piedra, papel o tijera: ").lower()
computer_option = "piedra"

if user_option == computer_option:
    print("Empate")    
elif user_option == "papel":
    print("Ganaste")
elif user_option == "tijera":
    print("Perdiste")
else:
    print("Opción no válida, por favor elige piedra, papel o tijera.")    