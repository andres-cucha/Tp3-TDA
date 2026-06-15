import random 
from parsing import parsing

SEED = 12345
INICIO = 10
FIN = 100000
random.seed(SEED)
JUGADORES = [
    "Dibu Martinez", "Rulli", "Armani", 
    "Molina", "Montiel", "Cuti Romero", "Otamendi", "Pezzella", "Licha Martinez", "Tagliafico", "Acuña",
    "De Paul", "Paredes", "Enzo Fernandez", "Mac Allister", "Lo Celso", "Palacios", "Guido Rodriguez",
    "Messi", "Di Maria", "Lautaro Martinez", "Julian Alvarez", "Nico Gonzalez", "Garnacho", "Dybala", "Correa"
]
VOLUMEN = 300

def escribir_archivo(nombre_archivo, lista_periodistas):
    with open(nombre_archivo, 'w', encoding="utf-8") as f:
        for l in lista_periodistas:
            f.write(",".join(l) + "\n")


def generar_archivos(tam):

    
    listas = [["Messi", random.choice(JUGADORES), random.choice(JUGADORES)] for _ in range(tam)]
    escribir_archivo("archivos/caso_messi.txt", listas)


    caso_no_hay_sol = []
    for i in range(tam):
        caso_no_hay_sol.append([f"jugador1_{i}", f"jugador2_{i}"]) #Generamos jugadores unicos para que no se repitan
    escribir_archivo("archivos/no_hay_sol.txt", caso_no_hay_sol)


   
    greedy = []
    for i in range(tam - 2):
        greedy.append(["Roncaglia", random.choice(JUGADORES)])
    
    mitad = len(greedy) // 2
    for i in range(len(greedy)):
        if i < mitad:
            greedy[i].append("Dibu Martinez")
        
        else:
            greedy[i].append("Cuti Romero")

    greedy.append(["Dibu Martinez", "Armani"])
    greedy.append(["Cuti Romero", "Pezzella"])
    escribir_archivo("archivos/greedy.txt", greedy)


   
    densidad_alta = [random.sample(JUGADORES, 15) for _ in range(tam)]
    escribir_archivo("archivos/densidad_alta.txt", densidad_alta)

    mit = tam // 2
    imposible = [random.sample(JUGADORES, 3) for _ in range(mit)]
    imposible.append([])
    imposible.extend([random.sample(JUGADORES, 3) for _ in range(tam - mit - 1)])
    escribir_archivo("archivos/imposible.txt", imposible)

    
    
  

    archivo_volumen = [random.sample(JUGADORES, random.randint(3, 7)) for _ in range(tam)]
    escribir_archivo(f"archivos/volumen.txt", archivo_volumen)

def generar_datos(tamaño, tipo):

    generar_archivos(tamaño)
    rutas = {
        "Messi": "archivos/caso_messi.txt",
        "No hay Sol": "archivos/no_hay_sol.txt",
        "Greedy": "archivos/greedy.txt",
        "Densidad Alta": "archivos/densidad_alta.txt",
        "Imposible": "archivos/imposible.txt",
        "Volumen": "archivos/volumen.txt"
    }
    return parsing(rutas[tipo])
