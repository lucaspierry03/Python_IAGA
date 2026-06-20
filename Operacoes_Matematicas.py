from math import sqrt
n = int(input("n: "))

dobro = 2 * n
triplo = 3 * n
quadrado = n ** 2
cubo = n ** 3
raizQ = n ** (1/2)
raizQuadrada = sqrt(n)

print()
print(f"Sendo n = {n}, tem-se:")
print(f"O dobro de {n} é {dobro}")
print(f"O triplo de {n} é {triplo}")
print(f"O quadrado de {n} é {quadrado}")
print(f"O cubo de {n} é {cubo}")
print(f"A raiz quadrada de {n} é {raizQ:.2f}")
print(f"A raiz quadrada de {n} é {raizQuadrada:.4f}")

