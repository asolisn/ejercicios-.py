hora=int(input("ingrese las horas: "))
minutos=int(input("ingrese los minutos: "))
segh=hora*(3600/1)
segm=minutos*(60/1)
segt=segh+segm
print("Los segundos en total son: {} ".format(segt))