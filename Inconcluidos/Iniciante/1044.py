entrada = input()
aux = entrada.split(" ")
if int(aux[0]) % int(aux[1]) == 0 or int(aux[1]) % int(aux[0]) == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")
