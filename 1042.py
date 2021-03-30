entrada = input()
vetEntrada = entrada.split(" ")
vetInteiros = []
for x in vetEntrada:
    vetInteiros.append(int(x))
vetInteiros.sort()
for x in vetInteiros:
    print(x)
print()
for x in vetEntrada:
    print(x)

