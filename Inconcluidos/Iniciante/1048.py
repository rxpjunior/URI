entrada = float(input())
if entrada <= 400:
    percentual = 15
    aux = 15 / 100
    reajuste = (entrada * aux)
    novoSalario = entrada + reajuste
elif entrada <= 800:
    percentual = 12
    aux = 12 / 100
    reajuste = (entrada * aux)
    novoSalario = entrada + reajuste
elif entrada <= 1200:
    percentual = 10
    aux = 10 / 100
    reajuste = (entrada * aux)
    novoSalario = entrada + reajuste
elif entrada <= 2000:
    percentual = 7
    aux = 7 / 100
    reajuste = (entrada * aux)
    novoSalario = entrada + reajuste
else:
    percentual = 4
    aux = 4 / 100
    reajuste = (entrada * aux)
    novoSalario = entrada + reajuste

print(f"Novo salario: {novoSalario:.2f}")
print(f"Reajuste ganho: {reajuste:.2f}")
print(f"Em percentual: {percentual} %")
