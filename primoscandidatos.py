def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def primos_complejos(rango=20):
    encontrados = set()
    for a in range(1, rango + 1):
        for b in range(1, rango + 1):
            norma = a*a + b*b
            if es_primo(norma):
                encontrados.add((a, b, norma))
    return encontrados

# Ejecutar el programa
for a, b, p in sorted(primos_complejos(30), key=lambda x: x[2]):
    print(f"{a} + {b}i  ->  norma = {p}  (primo)")
