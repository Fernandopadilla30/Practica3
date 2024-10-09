#desarrolla una funcion en python que invierta una cadena de texto
#by RoyMelvinT
nombre = input("ESCRIBA LA PALABRA QUE DESEA INVERTIR :")
longitud = len(nombre)-1
letra = ""
while longitud>=0:
    letra = letra + nombre[longitud]
    longitud = longitud -1
print(f"LA PALABRA: {nombre} INVERTIDO ES : {letra}")
