#Desarrolla una función que sume los dígitos de un número de manera recursiva hasta obtener un solo dígito
def suma_digitos(num):
    if num < 10:
        return num
    else:
        suma = sum(int(digito) for digito in str(num))
        print(f"La suma de digitos es: {suma}")
        return suma_digitos(suma)
    
num=int(input("Ingresa un numero entero positivo de 2 digitos o más: "))
resultado= suma_digitos(num)
print(f"El resultado de la suma total de digitos del {num} es: {resultado}")
    