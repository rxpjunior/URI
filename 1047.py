entrada = input()
aux = entrada.split(" ")
hInicio = int(aux[0])
mInicio = int(aux[1])
hFim = int(aux[2])
mFim = int(aux[3])

# Calculo das horas
if hInicio < hFim:
    hora = hFim - hInicio
elif hInicio == hFim:
    hora = 24
else:
    hora = (hFim + 12) - (hInicio - 12)

# Calculo dos minutos
minuto = 0
# continuar calculo minutos

# Contempla casos onde jogos duraram apenas minutos e horas diferentes
if hFim == (hInicio + 1) and mInicio > mFim:
    hora = 0 

print(f"O JOGO DUROU {hora} HORA(S) e {minuto} MINUTO(S)")
