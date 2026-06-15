import unittest
import os 

from parsing import parsing
from once_inicial import once_inicial
from resolucion_pl.pl_hitting_set import hitting_set
from mediciones.generar_datos import generar_archivos

DIR_ACTUAL = os.getcwd()
DIR_ARCHIVOS = DIR_ACTUAL + "/archivos/"

class TestingHittingSet(unittest.TestCase):

    def es_valida(self, solucion, datos):
        set_sol = set(solucion)

        for periodista in datos:
            if not set_sol.intersection(periodista):
                return False
            
            return True
        
    def test_generados(self):
        archivos = [
            "caso_messi.txt",
            "no_hay_sol.txt",
            "greedy.txt",
            "densidad_alta.txt",
            "imposible.txt"
        ]
        generar_archivos(20)

        for nombre in archivos:

            with self.subTest(archivo=nombre):
                ruta = DIR_ARCHIVOS + nombre

                datos = parsing(ruta)

                if not datos:
                    continue

                sol_backtracking = once_inicial(datos)
                sol_pl = hitting_set(datos)

                if sol_pl is None or sol_pl == []:
                    self.assertTrue(sol_backtracking is None or sol_backtracking == [], f"BT encontro solucino en {nombre} pero Pl dice que es imposible")
                    continue

                self.assertEqual(len(sol_backtracking), len(sol_pl),
                                 f"Solucion en {nombre}:\nBT dio: {len(sol_backtracking)}\nPL dio: {len(sol_pl)}")
                
                self.assertTrue(self.es_valida(sol_backtracking, datos))


if __name__ == "__main__":
    unittest.main()