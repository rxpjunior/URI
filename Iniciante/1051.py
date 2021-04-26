entrada = float(input())
imposto = 0
if entrada > 4500:
    faixa28 = entrada - 4500
    entrada = entrada - faixa28
    imposto = imposto + (faixa28 * 28 / 100)
if entrada > 3000:
    faixa18 = entrada - 3000
    entrada = entrada - faixa18
    imposto = imposto + (faixa18 * 18 / 100)
if entrada > 2000:
    faixa8 = entrada - 2000
    entrada = entrada - faixa8
    imposto = imposto + (faixa8 * 8 / 100)
    print(f"R$ {imposto:.2f}")

else:
    print("Isento")
