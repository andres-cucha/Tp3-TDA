def greedy_hitting_set(A, subconjuntos):
    C = set()
    no_cubiertos = []

    for B in subconjuntos:
        no_cubiertos.append(B)

    while len(no_cubiertos) > 0:
        mejor_elemento = None
        mejor_cantidad = -1

        for elemento in A:
            cantidad = 0

            for B in no_cubiertos:
                if elemento in B:
                    cantidad += 1

            if cantidad > mejor_cantidad:
                mejor_cantidad = cantidad
                mejor_elemento = elemento

        C.add(mejor_elemento)

        nuevos_no_cubiertos = []

        for B in no_cubiertos:
            if mejor_elemento not in B:
                nuevos_no_cubiertos.append(B)

        no_cubiertos = nuevos_no_cubiertos

    return C


def greedy_para_medicion(subconjuntos):
    A = set()

    for B in subconjuntos:
        if len(B) == 0:
            return None

        for elemento in B:
            A.add(elemento)

    return greedy_hitting_set(A, subconjuntos)

