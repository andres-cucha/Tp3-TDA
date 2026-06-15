from matplotlib import pyplot as plt
import seaborn as sns 
import numpy as np
import scipy as sp
from once_inicial import once_inicial
from mediciones.mediciones import tiempo_algoritmo
from mediciones.generar_datos import generar_datos

EXPONENTE_DOS = 2
CASOS = [
    "Messi",
    "No hay Sol",
    "Greedy",
    "Densidad Alta",
    "Imposible",
    "Volumen"
]
VOLUMEN = 300

def graficar_medicion(tipo):
    print("Iniciando...")

    if tipo == "Volumen":
        x = np.linspace(10,VOLUMEN, 10).astype(int)
    
    elif tipo == "No hay Sol":
        x = np.linspace(10, 20, 10).astype(int)

    else:
        x = np.linspace(10, 70, 10).astype(int)
    
    resultados = tiempo_algoritmo(once_inicial, x, generar_datos, tipo)

    #f = lambda x, v1, v2, v3: v1 * ( x ** EXPONENTE_DOS ) + v2 * x + v3
    #p_optimos, _ = sp.optimize.curve_fit(f, x,[resultados[i] for i in x])
    
    #error_cuadratico = np.sum((p_optimos[0] * ( x ** EXPONENTE_DOS ) + p_optimos[1] * x + p_optimos[2]  - [resultados[i] for i in x])**2)

    #print(f"El error cuadratico es de: {error_cuadratico}")

    ax: plt.Axes
    _, ax = plt.subplots()
    ax.plot(x, [resultados[int(i)] for i in x], marker='o', label="Medición")
    #ax.plot(x, [p_optimos[0]* ( n ** EXPONENTE_DOS) + p_optimos[1] * n + p_optimos[2] for n in x], 'r--', label="Ajuste")
    ax.set_title(f"Tiempo de medicion - Caso: {tipo}")
    ax.set_xlabel("Cantidad elementos en el Array")
    ax.set_ylabel("Tiempo de ejecución (s)")
    ax.legend()
    ax.grid()
    plt.show()

if __name__ == "__main__":
    graficar_medicion("No hay Sol")