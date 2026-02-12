def ejercicio_3():
    import math
    P = float(input("Ingresa tu peso (Kg): "))
    E = float(input("Ingresa tu estatura (Mts): "))

    IMC = P/(math.pow(E,2))

    if IMC <18.5:
        print(f"Tu IMC es {IMC}, tu nivel de peso es bajo")
    elif 18.5<= IMC <25:
        print(f"Tu IMC es {IMC}, tu nivel de peso es normal")
    elif 25<= IMC <30:
        print(f"Tu IMC es {IMC}, tu nivel de peso es de sobrepeso")
    else:
        print(f"Tu IMC es {IMC}, tu nivel de peso es de obesidad")