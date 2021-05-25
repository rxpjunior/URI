"""
Leia 100 valores inteiros. Apresente então o maior valor lido e a posição dentre os 100 valores lidos.

Entrada
O arquivo de entrada contém 100 números inteiros, positivos e distintos.

Saída
Apresente o maior valor lido e a posição de entrada, conforme exemplo abaixo.

"""
maior = {"numero":-1, "posicao":0}
for x in range(100):
    aux = int(input())
    if aux > maior["numero"]:
        maior["numero"] = aux
        maior["posicao"] = x + 1
print(maior["numero"])
print(maior["posicao"])


