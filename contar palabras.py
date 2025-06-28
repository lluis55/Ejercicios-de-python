def contar (texto):
    palabras = texto.split()
    if len(palabras) == 0:
        raise ValueError ("no hay ninguina palabra para contar")
    return len(palabras)



print("contador de palabras y letras")

while True:
    texto = input("ingresa tu texto para contar las palabras que tiene: ")
    try:
        numPalabras = contar(texto)
        contador = 0
        for caracter in texto:
            if caracter.isalpha():
                contador += 1
        print("numero de palabras :", numPalabras)
        print("numero de letras: ", contador)


    except ValueError:
        print("ingresa al menos una palabra")
    repetir = input("volver a ejecutar? (s) u oprime cualquier tecla para salir").strip().lower()
    if repetir != "s":
        print ("cerrando")
        break