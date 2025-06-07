import math

def es_primo(n):
    """Verifica si un número n es primo."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    limite = int(math.isqrt(n)) + 1
    for i in range(3, limite, 2):
        if n % i == 0:
            return False
    return True

def buscar_primos_complejos_grandes(desde=10**12, max_a=3000, max_b=3000, limite=10):
    """Busca números primos que puedan escribirse como a² + b² y que sean mayores que 'desde'."""
    encontrados = []
    contador = 0

    for a in range(1, max_a):
        for b in range(1, max_b):
            norma = a*a + b*b
            if norma <= desde:
                continue
            if es_primo(norma):
                encontrados.append((a, b, norma))
                print(f"🎯 {a} + {b}i → norma = {norma}  (¡primo #{len(encontrados)}!)")
                if len(encontrados) >= limite:
                    return encontrados
        # Muestra progreso básico cada 100 pasos de 'a'
        if a % 100 == 0:
            print(f"Progreso: a = {a} / {max_a}")
    
    return encontrados

# Ejecutar la búsqueda
resultados = buscar_primos_complejos_grandes(desde=10*9, max_a=50000, max_b=50000, limite=30)


# Mostrar resumen final
print("\n=== Primos encontrados ===")
for a, b, p in resultados:
    print(f"{a} + {b}i  → norma = {p}")
