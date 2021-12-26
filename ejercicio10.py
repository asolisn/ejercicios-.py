N=1
con=0
suma=0
while N != 0 :
    N=int(input("ingrese el numero:"))
    suma += N
    con += 1
if con == 0:
    print("no digito ningun numero")
else:
    promedio= suma/con
    print("el promedio de esta serie es:{}".format(promedio))

 