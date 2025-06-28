import math
while True:
    try:
        print("Calculadora de funciones cuadraticas")
        print("para resolver operaciones de la forma: ax^2+bx+c")

        a = float(input("ingresa el valor de a: "))
        b = float(input("ingresa el valor de b: "))
        c = float(input("ingresa el valor de c: "))

        rango = (input("ingresa el rango de esta forma (0,0): "))

        rango = rango.strip("()")
        inicio, fin = map(int, rango.split(","))

        print("\nResultados:")
        for x in range(inicio, fin + 1):
            y = a * x**2 + b * x + c
            print(f"x = {x}, f(x) = {y}")






    except ValueError:
        print("verifica los valores ingresados e intenta nuevamente")
    repetir = input("volver a ejecutar? (s) u oprime cualquier tecla para salir").strip().lower()
    if repetir != "s":
        print ("cerrando")
        break
