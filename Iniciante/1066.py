contPares = 0
contImpares = 0
contPositivos = 0
contNegativos = 0
for x in range(5):
    aux = int(input())
    if aux > 0:
        contPositivos += 1
    if aux < 0:
        contNegativos += 1
    if aux % 2 == 0:
        contPares += 1
    if aux % 2 != 0:
        contImpares += 1

print(f"{contPares} valor(es) par(es)")
print(f"{contImpares} valor(es) impar(es)")
print(f"{contPositivos} valor(es) positivo(s)")
print(f"{contNegativos} valor(es) negativo(s)")