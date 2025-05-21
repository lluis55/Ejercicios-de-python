temperatura = float(input("Ingrese temperatura"))
escala = input("es farenheight (F) o es celcius (C)?: ").lower()

if escala == "f":
    celcius = (temperatura - 32)* 5/9
    print(celcius)
elif escala == "c":
    farenheit = temperatura * 1.8 + 32
    print(farenheit)
else: 
    print("escala incorrecta")