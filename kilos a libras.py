kilo = 2.204 
lb = 0.453592
try:
    opcion = input ("selecciona la conversion Lb-Kg (a) Kg-Lb (b): ").lower()

    if opcion == "a":
        lbtokg = float(input("ingresa el peso en libras: "))
        resultado = lbtokg * lb
        print(f"{lbtokg} libras son {resultado:.2f} Kilos.")
    
    elif opcion == "b":
        kgtolb = float(input("ingresa el peso en kilos: "))
        resultado = kgtolb * kilo
        print(f"{kgtolb} kilos son {resultado:.2f} libras.")
    
    else:
        print("opcion no valida. usa solamente (a) o (b)")
except ValueError:
    print("caracter no valido, ingresa unicamente el valor solicitado")       