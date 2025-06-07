def convertirDivisas():
    import math
    print("Conversor de Pesos a Dólares y Dólares a Pesos")

    while True:
        try:
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
                continue

            redondear = input("Quieres redondear el resultado? (S/N)").lower()
            if redondear == "s":
                tipoRedondeo = input ("Redondear hacia Arriba (a) o Abajo (b)? ")
                print (f" Resultado redondeado: {round(resultado)}")
                if tipoRedondeo == "a":
                    print(f"Resultado redondeado hacia arriba: {math.ceil(resultado)}")
                elif tipoRedondeo == "b":
                    print(f"Resultado redondeado hacia abajo: {math.floor(resultado)}")
                else:
                    print("Opción de redondeo no valida")
            else:   
                print("No se redondeara el resultado")    

        except ValueError:
            print("Error en la seleccion de numeros, escoje unicamente 1 o 2")
        
        except ZeroDivisionError:
            print("no se puede dividir entre cero, ingresa otro valor")


convertirDivisas()