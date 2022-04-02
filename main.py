import json

parts = []

with open('particulas.json', 'r') as file:
    particulas = json.load(file)
    # print(particulas)

    for particula in particulas:
        part = {
            'id': particula['id'],
            'origen_x': particula['origen']['x']*5,
            'origen_y': particula['origen']['y']*5,
            'destino_x': particula['destino']['x']*5,
            'destino_y': particula['destino']['y']*5,
            'velocidad': particula['velocidad'],
            'red': particula['color']['red'],
            'green': particula['color']['green'],
            'blue': particula['color']['blue']
        }
        parts.append(part)
# print(parts)
with open('particulas_01.json', 'w') as file:
    json.dump(parts, file, indent=4)