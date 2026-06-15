

def parsing(archivo):

    with open(archivo) as f:

        jugadores = []

        for linea in f:

            sin_espacios = linea.strip()

            if not sin_espacios:
                continue
            
            jugadores.append(sin_espacios.split(","))
        
        return jugadores
