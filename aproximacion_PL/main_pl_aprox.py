from parsing import parsing
from aproximacion_PL.once_inicial_PLaprox import hitting_set_aproximacion_PL
import sys

ERROR_PARAMETROS = "parametros mal pasados"

def main_pl_aprox():
    
    if len(sys.argv) != 2:
        raise Exception(ERROR_PARAMETROS)
    
    jugadores = parsing(sys.argv[1])

    jugadores_imprescindibles = hitting_set_aproximacion_PL(jugadores)

    if jugadores_imprescindibles is None:
        print(f"No hay combinacion posible")
        return

    print(f"La cantidad de jugadores que no pueden faltar: {len(jugadores_imprescindibles)}")
    print(f"Jugadores: {jugadores_imprescindibles}")

if __name__ == "__main__":
    main_pl_aprox()