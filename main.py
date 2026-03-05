from utils.load_data import load_costs, load_heuristics
from algorithms.bfs import bfs
from algorithms.dfs import dfs

costos = load_costs('./data/funcion_de_costo.xlsx')
solucion = dfs(costos, "Warm-up activities", "Stretching")

if solucion:
    print('camino encontrado')
    print(solucion.path())
    print('Acciones:')
    print(solucion.solution())
else:
    print('No hay solución')

