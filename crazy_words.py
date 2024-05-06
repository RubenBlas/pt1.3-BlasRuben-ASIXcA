import random

#Encargado de marear el interior de cada palabra
def desordenar_secuencia(alfabeticos, inicio, fin):
    alfabeticos_a_desordenar = alfabeticos[inicio + 1 : fin - 1]
    random.shuffle(alfabeticos_a_desordenar)
    alfabeticos[inicio + 1 : fin - 1] = alfabeticos_a_desordenar

#Encargado de dividir el texto en caracteres especiales y no especiales manteniendo su posicion en una tabla
def desordenar_texto(texto):
    caracteres_alfabeticos = []
    caracteres_especiales = []

    contador_alfabeticos = 0
    contador_especiales = 0

    for i in range(len(texto)):
        if texto[i].isalpha():
            caracteres_alfabeticos.append(texto[i])
            caracteres_especiales.append("")
            contador_alfabeticos += 1
            contador_especiales = 0  # Reiniciar contador de caracteres especiales

        else:
            if contador_especiales == 0 and contador_alfabeticos > 3:
                desordenar_secuencia(caracteres_alfabeticos, i - contador_alfabeticos, i)

            caracteres_alfabeticos.append("")
            caracteres_especiales.append(texto[i])
            contador_especiales += 1
            contador_alfabeticos = 0  # Reiniciar contador de caracteres alfabéticos


    texto_desordenado = ''.join([a + b for a, b in zip(caracteres_alfabeticos, caracteres_especiales)])
    print(caracteres_alfabeticos)
    print(caracteres_especiales)

    return texto_desordenado
