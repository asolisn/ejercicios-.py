def contraseña(n,n1):
    n=int(input("ingrese una contraseña que tenga más de 10 digitos: "))
    digitos=len(str(n))
    if digitos >= 10:
        print("la contraseña es segura")
    else:
        print("la contraseña no es segura")
        return n
    n1=int(input("ingrese la contraseña: "))
    if n1==n:
        print("la contraseña es correcta ")
    
contraseña(0,0)
        