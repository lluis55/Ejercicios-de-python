print("calculadora.")
num1 = float(input("escribe el primer numero: "))
operacion = input("que operacion quieres hacer? (+, -, *, /): ")
num2 = float(input("escribe el segundo numero: "))

if operacion == '+':
    resultado = num1 + num2
elif operacion == '-':
    resultado = num1 - num2
elif operacion == '*':
    resultado = num1 * num2
elif operacion == '/':
    resultado = num1 / num2
else:
    resultado = "operacion no valida."

print("el resultado es:", resultado)
