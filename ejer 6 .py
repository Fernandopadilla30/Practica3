from statistics import mean, median, multimode

def calcular_estadisticas(numeros):
    media_valor = mean(numeros)
    mediana_valor = median(numeros)
    moda_valor = multimode(numeros)
    
    if len(moda_valor) == 1:
        moda_valor = moda_valor[0]  
    
    return {
        "media": media_valor,
        "mediana": mediana_valor,
        "moda": moda_valor
    }

numeros = [1, 2, 2, 3, 4, 4, 4, 5, 5, 6]
resultado = calcular_estadisticas(numeros)
print(resultado)
