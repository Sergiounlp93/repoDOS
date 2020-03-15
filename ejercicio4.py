"""Dada la lista de palabras generada en el ejercicio 2,
   arme un string con la frase armada con todas
   ellas separadas por un único espacio en blanco."""


"""
FRASE DE PRUEBA:

Si trabajás mucho con computadoras,
eventualmente encontrarás que te gustaría automatizar alguna tarea.
Por ejemplo, podrías desear realizar una búsqueda y reemplazo en un gran número de archivos de texto,
 o renombrar y reorganizar un montón de archivos con fotos de una manera compleja.
 Tal vez quieras escribir alguna pequeña base de datos personalizada, o una aplicación especializada
 con interfaz gráfica, o un juego simple.
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

nuevaFrase = " ".join(palabras_busqueda)
print(nuevaFrase)
