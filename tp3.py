import sys
import parsing
import once_inicial

ERROR_PARAMETROS = "parametros mal pasados"

def main():
    
    if len(sys.argv) != 2:
        raise Exception(ERROR_PARAMETROS)
    
    jugadores = parsing.parsing(sys.argv[1])

    jugadores_imprescindibles = once_inicial.once_inicial(jugadores)

    if jugadores_imprescindibles is None:
        print(f"No hay combinacion posible")
        return

    print(f"La cantidad de minima de jugadores que no pueden faltar: {len(jugadores_imprescindibles)}")
    print(f"Jugadores: {jugadores_imprescindibles}")

    
if __name__ == "__main__":
    main()