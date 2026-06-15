                   
def ya_no_mejora(mejor_sol, actual):
    if len(actual) >= len(mejor_sol):
        return True
    
    return False


def esta_cubierto(lista, j_agregados):
    for j in lista:

        if j in j_agregados:
            return True
        
    return False

def __once_inicial(lista_p, j_agregados, mejor_sol, camino_actual, idx):
    if (mejor_sol[0] is not None) and (ya_no_mejora(mejor_sol[0], camino_actual)):
        return 
    
    if idx == len(lista_p):
        mejor_sol[0] = camino_actual.copy()
        return
    
    if esta_cubierto(lista_p[idx], j_agregados):
        __once_inicial(lista_p, j_agregados, mejor_sol, camino_actual, idx + 1)

    else:
        for jugador in lista_p[idx]:

            j_agregados.add(jugador)
            camino_actual.append(jugador)
            
            __once_inicial(lista_p, j_agregados, mejor_sol, camino_actual, idx + 1)

            j_agregados.remove(jugador)
            camino_actual.pop()
           



def once_inicial(lista_periodistas):
    j_agregados = set()
    camino_actual = []
    idx = 0
    mejor_sol = [None]

    __once_inicial(lista_periodistas, j_agregados, mejor_sol, camino_actual, idx)

    return tuple(mejor_sol[0])