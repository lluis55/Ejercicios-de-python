import math

def convertirDivisas():
    print("conversor de pesos a dolares y dolares a pesos")

    while True:
        try:
            tipo_de_cambio = float(input("ingresa el tipo de cambio actual del dolar en pesos (MXN): "))

            print("opciones:")
            print("1. convertir de pesos a dolares")
            print("2. convertir de dolares a pesos")
            opcion = input("selecciona una opcion (1 o 2): ")

            if opcion == "1":
                pesos = float(input("ingresa tu monto en pesos (MXN): "))
                resultado = pesos / tipo_de_cambio
                unidad = "dolares"
               
        
            elif opcion == "2":
                dolares = float(input("ingresa tu monto en dolares (USD): "))
                resultado = dolares * tipo_de_cambio
                unidad = "pesos"
                
        
            else:
                print("opcion no valida")
                continue

            print(f"equivale a {resultado:.2f} {unidad}")
            if resultado.is_integer():
                print("el resultado es entero, no se requiere redondeo")
            else:
                redondear = input("quieres redondear el resultado? (s/n): ").lower()
                if redondear == "s":
                    tipoRedondeo = input("redondear hacia arriba (a) o abajo (b): ").lower()

                    print(f"resultado redondeado (normal): {round(resultado)} {unidad}")
                    if tipoRedondeo == "a":
                        print(f"resultado redondeado hacia arriba: {math.ceil(resultado)} {unidad}")
                    elif tipoRedondeo == "b":
                        print(f"resultado redondeado hacia abajo: {math.floor(resultado)} {unidad}")
                    else:
                        print("opcion de redondeo no valida")
                else:   
                    print("no se redondeara el resultado")    

        except ValueError:
            print("error en la seleccion de numeros, escoge unicamente 1 o 2")

        except ZeroDivisionError:
            print("no se puede dividir entre cero, ingresa otro valor")

        continuar = input("quieres hacer otra conversion? (s/n): ").lower()
        if continuar != "s":
            print("gracias por usar el conversor. hasta luego")
            break

convertirDivisas()
