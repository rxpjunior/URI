for x in range(3):
    print(x)

if 10 == type(int):
    print("int")
    print(type(int))
else:
    print("nao")
    print(type(int))


f = 1.23

print(f.is_integer())
# False

f_i = 100.0
s = f_i.is_integer()
print(s)
# True