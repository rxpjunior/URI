entrada = input()
coord = entrada.split(" ")
x = float(coord[0])
y = float(coord[1])
if x == y == 0:
    print("Origem")
elif x == 0:
    print("Eixo Y")
elif y == 0:
    print("Eixo X")
elif x < 0 and y > 0:
    print("Q2")
elif x > 0 and y > 0:
    print("Q1")
elif x > 0 and y < 0:
    print("Q4")
else:
    print("Q3")
