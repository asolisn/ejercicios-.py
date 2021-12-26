dia=int(input("ingresa el dia: "))
mes=int(input("ingresa el mes: "))
año=int(input("ingresa el año: "))
if (año%400)==0:
    print("la fecha {}{}{} es un año bisiesto".format(dia,mes,año) )
else:
    print("la fecha {}/{}/{} no es un año bisiesto".format(dia,mes,año) )