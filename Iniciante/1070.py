"""
Leia um valor inteiro X. Em seguida apresente os 6 valores ímpares consecutivos a partir de X, um valor por linha, inclusive o X ser for o caso.

Entrada
A entrada será um valor inteiro positivo.

Saída
A saída será uma sequência de seis números ímpares.
"""
aux = int(input())
cont = 0
while True:
    if not aux % 2 == 0:
        print(aux)
        cont += 1
        aux += 1
    else:
        aux += 1
    if cont == 6:
        break


    