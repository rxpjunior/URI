n1 = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())
n5 = float(input())
n6 = float(input())
lista = [n1, n2, n3, n4, n5, n6]
contPositivos = 0
for x in lista:
    if x > 0:
        contPositivos += 1

print(f"{contPositivos} valores positivos")

