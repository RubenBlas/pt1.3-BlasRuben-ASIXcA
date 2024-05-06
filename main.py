import time
import data_source

def main():
    inicio = time.time()

    data_source.procesar_archivos_entrada_salida("./entrada", "./salida")

    fin = time.time()
    tiempo_transcurrido = fin - inicio

    print(f"Proceso completado. Tiempo transcurrido: {tiempo_transcurrido:.2f} segundos.")

if __name__ == "__main__":
    main()
