x = 0.0
while x <= 2:
    for z in range(3):
        if x.is_integer():
            aux1 = int(x)
            aux2 = int(x+z+1)
            print(f'X={aux1} J={aux2}')
        else:
            print(f'X={x:.1f} J={x+z+1:.1f}')
    x += 0.2

       
