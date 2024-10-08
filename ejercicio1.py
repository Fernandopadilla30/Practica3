def es_numero_perfecto(numero):
    # Inicializamos la suma de los divisores propios
    suma_divisores = 0
    
    # Recorremos todos los números desde 1 hasta numero - 1
    for i in range(1, numero):
        if numero % i == 0:
            # Si i es divisor de 'numero', lo sumamos
            suma_divisores += i
    
    # Verificamos si la suma de los divisores es igual al número
    if suma_divisores == numero:
        return f"El número {numero} es perfecto."
    else:
        return f"El número {numero} no es perfecto."

# Ejemplo de uso
print(es_numero_perfecto(6))  # El número 6 es perfecto
print(es_numero_perfecto(28)) # El número 28 es perfecto
print(es_numero_perfecto(12)) # El número 12 no es perfecto
