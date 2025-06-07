n1 = input("ingresa numero 1: ")
n2 = input("ingresa numero 2: ")


n1 = int(n1)
n2 = int(n2)

suma = (n1 + n2)
resta = n1 - n2
multiplicacion = n1 * n2
division = n1 / n2

mensaje = f""" 
para los numeros {n1} y {n2}, 
resultado suma es {suma}.
resultado resta es {resta}.
resultado multiplicacion es {multiplicacion}.
resultado division es {division}."""


print (mensaje)