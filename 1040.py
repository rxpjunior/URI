entrada = input()
aux = entrada.split(" ")
somatorio  = 0
somatorio += float(aux[0]) * 2
somatorio += float(aux[1]) * 3
somatorio += float(aux[2]) * 4
somatorio += float(aux[3]) * 1
media = somatorio / 10 
print(f"Media: {media:.1f}")
if media >= 7:
    print("Aluno aprovado.")
elif media < 4.9:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    aux2 = float(input())
    print(f"Nota do exame: {aux2:.1f}")
    media = (media + aux2) / 2
    if media >= 5:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print(f"Media final: {media:.1f}")
