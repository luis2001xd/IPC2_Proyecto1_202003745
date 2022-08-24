from colorama import Fore

def menu():
    opcion=""
    while opcion!=8:
        print(Fore.YELLOW+"------------Bienvenido usuario ♣--------------")
        print()
        print(Fore.CYAN+"------------Menú---------------")
        print()
        print(Fore.CYAN+"1. Cargar Archivo")
        print(Fore.CYAN+"2.Salir")
        print()
        x=int(input())
        if x==1:
            print("hola")





menu()