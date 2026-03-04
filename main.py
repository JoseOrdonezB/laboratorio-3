from utils.load_data import load_costs, load_heuristics

heuristica = load_heuristics('./data/heuristica.xlsx')
costos = load_costs('./data/funcion_de_costo.xlsx')

print(heuristica)
print(costos)