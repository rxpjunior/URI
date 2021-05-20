"""
Leia 2 valores inteiros X e Y. A seguir, calcule e mostre a soma dos números impares entre eles.

Entrada
O arquivo de entrada contém dois valores inteiros.

Saída
O programa deve imprimir um valor inteiro. Este valor é a soma dos valores ímpares que estão entre os valores fornecidos na entrada que deverá caber em um inteiro.

"""

num1 = int(input())
num2 = int(input())

if num2 < num1:
    inicio = num2
    fim = num1
else:
    inicio = num1
    fim = num2

soma = 0
for x in range(inicio+1, fim):
    if x % 2 != 0:
        soma += x

print(soma)


