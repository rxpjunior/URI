"""
Leia um conjunto não determinado de pares de valores M e N (parar quando algum dos valores for menor ou igual a zero). Para cada par lido, mostre a sequência do menor até o maior e a soma dos inteiros consecutivos entre eles (incluindo o N e M).

Entrada
O arquivo de entrada contém um número não determinado de valores M e N. A última linha de entrada vai conter um número nulo ou negativo.

Saída
Para cada dupla de valores, imprima a sequência do menor até o maior e a soma deles, conforme exemplo abaixo.
"""

while(True):
    soma = 0
    sequencia = ""
    entrada = input()
    aux = entrada.split(" ")
    if int(aux[0]) <= 0 or int(aux[1]) <= 0:
        break
    else:
        n1 = int(aux[0])
        n2 = int(aux[1])
        if n1 < n2:
            for x in range(n1, (n2 + 1)):
                soma = soma + x
                sequencia = sequencia + str(x) + " "
            sequencia = sequencia + "Sum="+str(soma)
        else:
            for x in range(n2, (n1 + 1)):
                soma = soma + x
                sequencia = sequencia + str(x) + " "
            sequencia = sequencia + "Sum="+str(soma)
        print(sequencia)


