t1 = input()
t2 = input()
t3 = input()

lista = [
    {'aguia':['carnivoro', 'ave', 'vertebrado']},
    {'pomba':['onivoro', 'ave', 'vertebrado']},
    {'homem':['onivoro', 'mamifero', 'vertebrado']},
    {'vaca':['herbivoro', 'mamifero', 'vertebrado']},
    {'pulga':['hematofago', 'inseto', 'invertebrado']},
    {'lagarta':['herbivoro', 'inseto', 'invertebrado']},
    {'sanguessuga':['hematofago', 'anelideo', 'invertebrado']},
    {'minhoca':['onivoro', 'anelideo', 'invertebrado']}
]

for x in lista:
    y = list(*x.values())
    if t1 in y and t2 in y and t3 in y:
        z = str(*x.keys())
        print(z)
