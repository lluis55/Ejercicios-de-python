def contar (texto):
    palabras = texto.split()
    if len(palabras) == 0:
        raise ValueError ("no hay ninguina palabra para contar")
    return len(palabras)

print("contador de palabras")
texto = input("ingresa tu texto para contar las palabras que tiene: ")
try:
    numPalabras = contar(texto)
    print("numero de palabras :", numPalabras)
except ValueError:
    print("ingresa al menos una palabra")