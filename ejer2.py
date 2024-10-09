#desarrolla una funcion en python que invierta una cadena de texto
#by RoyMelvinT
def invertir_cadena(cadena):
    inversa = ""
    for char in cadena:
        inversa = char + inversa
    return inversa
cadena = input("INGRESE UNA CADENA PARA INVERTIR : ")
inversa = invertir_cadena(cadena)
print ("LA CADENA INVERTIDA ES : ", inversa)
        