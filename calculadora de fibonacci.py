def fibonacciPosicion():
    x = 0
    y = 1
    try:
        Nmaximo = int(input("ingresa el numero en la secuencia que quieres saber (solo el numero entero que represente la pocicion): "))

        for i in range(Nmaximo):
            x, y = y, x + y
        print(f"la \033[32mposicion {Nmaximo}\033[0m en la secuencia de fibonacci corresponde al numero \033[32m{x}\033[0m")
            
    except ValueError:
        print("Ingresa solo numeros enteros")

def fibonacciProximidad():
    X = 0
    Y = 1
    try:
        Nmaximo = int(input("ingresa un numero para saber cual es el numero de fibonacci mas proximo: "))
        while Y < Nmaximo:

            
            X, Y = Y, X + Y

        print (f" El numero de fibonacci mas proximo a llegar o ser \033[32m{Nmaximo}\033[0m es: \033[32m{X}\033[0m")
    except ValueError:
        print("solo ingresa numeros enteros")


while True:

    print ("\033[32mCalculadora de numeros de fibonacci\033[0m")
    print ("\033[33m1.\033[0m buscar un numero en una pocicion especifica de la secuencia")
    print ("\033[33m2.\033[0m buscar el numero de fibonacci mas proximo sin pasarse")

    opcion = input("selecciona \033[33m1\033[0m o \033[33m2\033[0m: ")

    if opcion == "1":
        fibonacciPosicion()
    elif opcion == "2":
        fibonacciProximidad()
    else:
        print ("solo ingresa opcion 1 o 2 ")


    while True:
        continuar = input("quieres hacer otra operacion? (s/n): ").lower()

        if continuar == 's':
            break
        elif continuar == 'n':
            print("\033[32mGracias por usar la calculadora, saliendo...\033[0m")
            exit()
        else:
            print("solo escribe s para continuar o n para salir.")

