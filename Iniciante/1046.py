entrada = input()
aux = entrada.split(" ")
inicio = int(aux[0])
fim = int(aux[1])
if inicio < fim:
    tempo = fim - inicio
elif inicio == fim:
    tempo = 24
else:
    tempo = (fim + 12) - (inicio - 12)
print(f"O JOGO DUROU {tempo} HORA(S)")
