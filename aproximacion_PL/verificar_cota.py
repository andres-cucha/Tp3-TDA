from parsing import parsing
from resolucion_pl.pl_hitting_set import hitting_set
from aproximacion_PL.once_inicial_PLaprox import hitting_set_aproximacion_PL

ARCHIVOS = [
    "archivos/5.txt",
    "archivos/7.txt",
    "archivos/10_pocos.txt",
    "archivos/10_todos.txt",
    "archivos/10_varios.txt",
    "archivos/15.txt",
    "archivos/20.txt",
    "archivos/50.txt",
    "archivos/75.txt",
    "archivos/100.txt",
    "archivos/200.txt",
    "archivos/caso_messi.txt",
    "archivos/densidad_alta.txt",
    "archivos/greedy.txt",
    "archivos/no_hay_sol.txt",
    "archivos/volumen.txt"
]

def calcular_b(lista_p):
    b = 0

    for sublista in lista_p:
        if len(sublista) > b:
            b = len(sublista)

    return b


def comparar_archivo(ruta):
    lista_p = parsing(ruta)
    optima = hitting_set(lista_p)
    aproximada = hitting_set_aproximacion_PL(lista_p)

    if optima is None or aproximada is None:
        print(f"{ruta}: No hay combinacion posible")
        return

    b = calcular_b(lista_p)
    cant_optima = len(optima)
    cant_aprox = len(aproximada)
    cota = cant_aprox / cant_optima
    cumple = cota <= b

    print("Archivo:", ruta)
    print("OPT:", cant_optima, optima)
    print("APROX:", cant_aprox, aproximada)
    print("b:", b)
    print("APROX / OPT:", cota)
    print("Cumple cota:", cumple)
    print("-" * 50)


def main():
    for archivo in ARCHIVOS:
        comparar_archivo(archivo)


if __name__ == "__main__":
    main()