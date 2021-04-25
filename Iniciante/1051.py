entrada = float(input())
if entrada < 2000:
    print("Isento")
elif entrada < 3000:
    print(f"R$ {((entrada - 2000) * 8/100):.2f}")
elif entrada < 4500:
    print(f"R$ {((entrada - 2000) * 18/100):.2f}")
else:
    print(f"R$ {((entrada - 2000) * 28/100):.2f}")
