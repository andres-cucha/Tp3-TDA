from parsing import parsing
from resolucion_pl.pl_hitting_set import hitting_set
import sys

ERROR_PARAMETROS = "parametros mal pasados"

def main_pl():
    
    if len(sys.argv) != 2:
        raise Exception(ERROR_PARAMETROS)
    
    jugadores = parsing(sys.argv[1])

    jugadores_imprescindibles = hitting_set(jugadores)

    if jugadores_imprescindibles is None:
        print(f"No hay combinacion posible")
        return

    print(f"La cantidad de minima de jugadores que no pueden faltar: {len(jugadores_imprescindibles)}")
    print(f"Jugadores: {jugadores_imprescindibles}")

if __name__ == "__main__":
    main_pl()