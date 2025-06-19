import random
while True:
    try:
            pisos = int(input("ingresa el numero de plantas que tiene el edificio, contando desde el primero en orden ascendente (los sotanos y plantas bajas cuentan como un numero positivo)"))
            

            if pisos < 1 or pisos > 400:
                print("debe haber al menos un piso y no mas de 400 y no se permiten sotanos")
            else:
                elevador = random.randint(1, pisos)
                miPiso = random.randint(1, pisos) 

            print(f"el Elevador esta en el piso {elevador}")
            print(f"tu te encuentras en el piso {miPiso}")

            if elevador < miPiso:
                print("el elevador esta subiendo por ti")
            elif elevador > miPiso:
                print ("el elvador esta bajando por ti")
            else: 
                print ("el elevador ya esta en tu piso, abriendo puertas")
            print("el elevador ya llego, adelante")

            destino = int(input("a que piso quieres ir? "))
            if destino > pisos or destino < 1:
                print("ese piso no existe")
            elif destino == miPiso:
                print("ya estas en este piso, abriendo puertas")
            elif destino > miPiso:
                print(f"estas subiendo al piso {destino}" )
                print("has llegado, cerrando las puertas")
            else:
                print(f"estas bajando al piso {destino}")
                print("has llegado, cerrando puertas")



    except ValueError:
            print("ingresa correctamente los datos solicitados")
    repetir = input("usar otra vez el elevador (s) u oprime cualquier tecla para salir").strip().lower()
    if repetir != "s":
        print ("cerrando")
        break
