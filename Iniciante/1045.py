entrada = input()
lista = entrada.split(" ")
tamanho = len(lista)

for x in range(1, tamanho):
    for y in range(tamanho - 1):
        if float(lista[y]) > float(lista[y+1]):
            aux = float(lista[y])
            lista[y] = float(lista[y + 1])
            lista[y + 1] = aux

a = float(lista[2])
b = float(lista[1])
c = float(lista[0])

if a >= (b + c):
    print("NAO FORMA TRIANGULO")
else:
    if a**2 == (b**2) + (c**2):
        print("TRIANGULO RETANGULO")
    if a**2 > (b**2) + (c**2):
        print("TRIANGULO OBTUSANGULO")
    if a**2 < (b**2) + (c**2):
        print("TRIANGULO ACUTANGULO")
    if a == b and b == c and c == a:
        print("TRIANGULO EQUILATERO")
    if a == b and b != c or a == c and b != c or c == b and b != a:
        print("TRIANGULO ISOSCELES")
