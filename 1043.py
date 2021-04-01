entrada = input()
aux = entrada.split(" ")
a = float(aux[0])
b = float(aux[1])
c = float(aux[2])
if a + b > c and a + c > b and b + c > a:
    perimetro = a + b + c
    print(f"Perimetro = {perimetro:.1f}")
else:
    area = (((a + b) * c) / 2)
    print(f"Area = {area:.1f}")
