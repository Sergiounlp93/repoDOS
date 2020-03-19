"""Dada una frase y un string ingresados por teclado (en ese orden),
genere una lista de palabras (separadas por ' '),
y sobre ella, informe la cantidad de palabras en las que se encuentra el string.
No importan las mayúsculas y minúsculas.
Nota: este ejercicio se deberá resolver en el curso online y
probar su ejecución con casos provistos en el mismo
"""

#interfaz con el usuario
print("introdusca un texto")
texto = input()
print("introdusca una palabra a buscar")
busqueda = input()

#conversion al mismo formato
texto=texto.lower()
busqueda=busqueda.lower()

#armando una lista de palabras
palabras_texto = texto.split(' ')

#buscando la palabra entre los elementos de la lista
palabras_busqueda = [s for s in palabras_texto if busqueda in s]
cant=len(palabras_busqueda)
"""
UNA FORMA ES ASI
print("Se encontro las siguientes ocurrencias"+ str(palabras_busqueda))
print("la cantidad de veces que se encontro la palabra es "+ str(len(palabras_busqueda)) )
"""
#La otra forma es asi
print(f"Ocurrencias en contradas: {palabras_busqueda}")
print(f"cantidad encontrada {cant}")
