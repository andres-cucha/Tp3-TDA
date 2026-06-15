import pulp 

def hitting_set(lista_p):
    n = len(lista_p)

    if n == 0:
        return []
    
    unicos = set()
    for l in lista_p:
        for j in l:
            unicos.add(j)

    prob = pulp.LpProblem("Hitting_set", pulp.LpMinimize)

    variables = {}

    for jugador in unicos:
        limpiar_nombre = jugador.replace(" ", "_")
    
        variables[jugador] = pulp.LpVariable(f"y_{limpiar_nombre}", cat=pulp.LpBinary)
    
    prob += pulp.lpSum([variables[j] for j in unicos]), "Minimizar_Jugadores_convocados"

    for i, sublista in enumerate(lista_p):
        prob += pulp.lpSum(variables[j] for j in sublista) >= 1, f"Restriccion_Periodista_{i}"

    prob.solve(pulp.PULP_CBC_CMD(msg=False))

    convocados = [j for j in unicos if variables[j].varValue == 1.0]

    return convocados
    