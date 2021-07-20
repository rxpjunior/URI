"""
Leia um valor inteiro N que é a quantidade de casos de teste que vem a seguir. Cada caso de teste consiste de dois inteiros X e Y. Você deve apresentar a soma de todos os ímpares existentes entre X e Y.

Entrada
A primeira linha de entrada é um inteiro N que é a quantidade de casos de teste que vem a seguir. Cada caso de teste consiste em uma linha contendo dois inteiros X e Y.

Saída
Imprima a soma de todos valores ímpares entre X e Y.

"""

nCasos = int(input())
for x in range(nCasos):
    aux = input()
    entrada = aux.split(" ")
    if len(entrada) == 2:
        n1 = int(entrada[0])
        n2 = int(entrada[1])
    else:
        n1 = n2 = int(entrada[0])
    if n1 <= n2:
        soma = 0
        for x in range((n1+1), n2):
            if x % 2 !=0:
                soma = soma + x
    else:
        soma = 0
        for x in range((n2+1), n1):
            if x % 2 !=0:
                soma = soma + x

    print(soma)
