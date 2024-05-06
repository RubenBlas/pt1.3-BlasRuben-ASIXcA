import os
import crazy_words

# Convertir cada palabra en una "paraules_boges" usando la función desordenar_texto de crazy_words
def procesar_texto(texto):
    palabras_boges = [crazy_words.desordenar_texto(texto)]
    return palabras_boges

#Encargado de la lectura y escritura de archivos
def procesar_archivos_entrada_salida(directorio_entrada, directorio_salida):
    archivos_entrada = [archivo for archivo in os.listdir(directorio_entrada) if archivo.endswith('.txt')]

    for archivo in archivos_entrada:
        ruta_archivo_entrada = os.path.join(directorio_entrada, archivo)
        with open(ruta_archivo_entrada, 'r') as f:
            contenido = f.read()

        palabras_boges = procesar_texto(contenido)
        print(f"Palabras boges para el archivo {archivo}: {palabras_boges}")  # Imprimir para diagnóstico

        nombre_archivo_salida = archivo.replace('.txt', '_boges.txt')
        ruta_archivo_salida = os.path.join(directorio_salida, nombre_archivo_salida)

        with open(ruta_archivo_salida, 'w') as f:
            for palabra in palabras_boges:
                f.write(palabra)
