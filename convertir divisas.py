def convertirDivisas():
    print("Conversor de Pesos a Dólares y Dólares a Pesos")
    
    tipo_de_cambio = float(input("Ingresa el tipo de cambio actual del dolar en Pesos (MNX)"))
    

    #tipo_de_cambio = 20
    print("OPCIONES:")
    print("1. Convertir de Pesos a Dólares")
    print("2. Convertir de Dólares a Pesos")
    opcion = input("Selecciona una opción (1 o 2): ")

    if opcion == "1":
        pesos = input("Ingresa tu monto en Pesos (MXN): ")
        pesos = float(pesos)
        resultado = pesos / tipo_de_cambio
        print(f"Equivale a {resultado:.2f} dólares")
    
    elif opcion == "2":
        dolares = input("Ingresa tu monto en Dólares (USD): ")
        dolares = float(dolares)
        resultado = dolares * tipo_de_cambio
        print(f"Equivale a {resultado:.2f} pesos")
    
    else:
        print("Opción no válida")

    redondear = input("Quieres redondear el resultado? (S/N)").lower()
    if redondear == "s":
     print (f" Resultado redondeado: {round(resultado)}")
    else:
       print("No se redondeo el resultado")

convertirDivisas()
