#Escribe una funcion que calcule el factorial de un numero entero de forma iterativa

def calcular_factorial():
    while True:
        try:
            numero=int(input("Ingresar numero: "))
            if numero>=0:
                break
            else:
                print("Ingresar numero positivo")
        except ValueError:
            print("Error, ingresar numero entero")
    new_numero = numero
    if numero==0 or numero==1:
        print(f"Factorial de {numero} es 1")
    else:
        acumulado=1
        while numero>1:
            acumulado=acumulado*(numero)
            numero-=1
        print(f"Factorial de {new_numero} es {acumulado}")
    
calcular_factorial() 