import math
while True:
    try:
        print("programa para contar en un determinado intervalo")

        rango = (input("ingresa el rango de esta forma (0,0): "))
        conteo = int(input("ingresa el numero incremental para hacer la cueenta (ejemplo: 2 para contar de 2 en 2): "))

        rango = rango.strip("()")
        inicio, fin = map(int, rango.split(","))

        print("\nResultados:")
        for x in range(inicio, fin, conteo):
            print(f"{x}")





    except ValueError:
        print("verifica los valores ingresados e intenta nuevamente")
    repetir = input("volver a ejecutar? (s) u oprime cualquier tecla para salir").strip().lower()
    if repetir != "s":
        print ("cerrando")
        break