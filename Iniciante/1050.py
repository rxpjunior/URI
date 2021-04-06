entrada = int(input())
lista = [61, 'Brasilia', 71, 'Salvador', 11, 'Sao Paulo', 21, 'Rio de Janeiro', 32, 'Juiz de Fora', 19, 'Campinas', 27, 'Vitoria', 31, 'Belo Horizonte']
tamanho = len(lista)
for x in range(0, tamanho):
    if lista[x] == entrada:
        print(lista[x+1])
        break
else:
    print("DDD nao cadastrado")
