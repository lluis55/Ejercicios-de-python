

while True:
    try:
        print("calculadora de precios")
        costo1 = float(input("ingresa el costo del producto 1: "))
        cantidad1 = float(input("ingresa el numero de unidades del producto 1: "))

        costo2 = float(input("ingresa el costo del producto 2: "))
        cantidad2 = float(input("ingresa el numero de unidades del producto 2: "))

        costoreal1 = costo1 / cantidad1
        costoreal2 = costo2 / cantidad2

        print(f"el costo unitario del producto 1 es de {costoreal1}")
        print(f"el costo unitario del producto 2 es de {costoreal2}")

        if costoreal1 < costoreal2:
            print("el producto 1 tiene mejor relacion calidad-precio")
        elif costoreal2 < costoreal1:
            print("el producto 2 tiene mejor relacion calidad-precio")
        else:
            print("hubo un error, revisa los datos ingresados por favor")
    except ValueError:
            print("ingresa unicamente numeros para calcular los precios de los productos")
    repetir = input("usar otra vez el calculo de precios (s) u oprime cualquier tecla para salir").strip().lower()
    if repetir != "s":
        print ("cerrando")
        break