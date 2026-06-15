from concurrent.futures import ProcessPoolExecutor, as_completed
import time 
import os

CANTIDAD_EJECUCUCIONES = 10


def tiempo_en_correr(algoritmo, generar_datos, tam, tipo):
    lista_jugadores = generar_datos(tam, tipo)

    hora_inicio = time.time()

    algoritmo(lista_jugadores)

    return time.time() - hora_inicio

def tiempo_algoritmo(algoritmo, tam ,generar_datos, tipo):
    futures = {}
    tiempo_totales = {int(t): 0 for t in tam}

    with ProcessPoolExecutor(max(1, (os.cpu_count() or 0) //4)) as p:
        for t in tam:
            tamaño = int(t)
            for _ in range(CANTIDAD_EJECUCUCIONES):
                futures[p.submit(tiempo_en_correr, algoritmo, generar_datos, tamaño, tipo)] = tamaño

        for f in as_completed(futures):
            result = f.result()
            i = futures[f]
            tiempo_totales[i] += result

    return {s: t / CANTIDAD_EJECUCUCIONES for s, t in tiempo_totales.items()}