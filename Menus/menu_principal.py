from Examen.Ejemplos.Ejercicio_1 import ejercicio_1
from Examen.Ejemplos.Ejercicio_2 import ejercicio_2
from Examen.Ejercicios.Ejercicio_3 import ejercicio_3

def menu_principal():
    while True:
        print("Menu principal")
        print("1.- Ejercicio 1")
        print("2.- Ejercicio 2")
        print("3.- Ejercicio 3")
        print("4.- Salir")

        Op = int(input("Elija opción: "))
        match(Op):
            case 1:
                ejercicio_1()
            case 2:
                ejercicio_2()
            case 3:
                ejercicio_3()
            case 4:
                break
            case _:
                print("Opción no válida")
