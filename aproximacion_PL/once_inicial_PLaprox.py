import pulp

def hitting_set_aproximacion_PL(lista_p):
    n = len(lista_p)

    if n == 0:
        return []

    for sublista in lista_p:
        if len(sublista) == 0:
            return None

    unicos = set()

    for l in lista_p:
        for j in l:
            unicos.add(j)

    prob = pulp.LpProblem("Hitting_set_aproximacion_PL", pulp.LpMinimize)

    variables = {}

    for jugador in unicos:
        limpiar_nombre = jugador.replace(" ", "_")

        variables[jugador] = pulp.LpVariable(
            f"y_{limpiar_nombre}",
            lowBound=0,
            upBound=1,
            cat=pulp.LpContinuous
        )

    prob += pulp.lpSum([variables[j] for j in unicos]), "Minimizar_Jugadores_convocados"

    for i, sublista in enumerate(lista_p):
        prob += pulp.lpSum(variables[j] for j in sublista) >= 1, f"Restriccion_Periodista_{i}"

    prob.solve(pulp.PULP_CBC_CMD(msg=False))

    b = None
    for sublista in lista_p:
        if b == None or b < len(sublista):
            b = len(sublista)
    
    convocados = []

    for j in unicos:
        if variables[j].varValue >= 1 / b:
            convocados.append(j)

    return convocados