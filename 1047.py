entrada = input()
aux = entrada.split(" ")
hInicio = int(aux[0])
mInicio = int(aux[1])
hFim = int(aux[2])
mFim = int(aux[3])

# Calculo das horas
if hInicio < hFim:
    hora = hFim - hInicio
if hFim == (hInicio + 1) and mInicio > mFim: # Contempla casos onde jogos duraram apenas minutos e horas diferentes
    hora = 0 
elif hFim == hInicio and mInicio > mFim:
    hora = 23
elif hInicio == hFim:
    hora = 24
else:
    hora = (hFim + 12) - (hInicio - 12)

# Calculo dos minutos
if mFim > mInicio:
    minuto = mFim - mInicio
elif mFim == mInicio:
    minuto = 0
else:
    minuto = 60 - mInicio + mFim

print(f"O JOGO DUROU {hora} HORA(S) e {minuto} MINUTO(S)")
