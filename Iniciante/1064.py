elementos = []
for x in range(0,6):
    aux = float(input())
    elementos.append(aux)

def verificaPositivo(numero):
    if numero > 0:
        return True
    else:
        return False

contPositivos = 0
somaPositivos = 0

for x in elementos:
    if verificaPositivo(x):
        contPositivos += 1
        somaPositivos += float(x)
media = somaPositivos / contPositivos

print(f"{contPositivos} valores positivos")
print(f"{media:.1f}")
