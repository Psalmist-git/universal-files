import json
from pygal_maps_world.maps import World
from codes import get_country_code

# Load the population data.
with open('population_data.json', encoding='utf-8') as f:
    pop_data = json.load(f)

# Build a dictionary of population data.
cc_populations = {}

for pop_dict in pop_data:
    if str(pop_dict.get('Year')) == '2010':
        country = pop_dict.get('Country Name')
        value = pop_dict.get('Value')

        if country and value not in (None, ''):
            try:
                population = int(float(value))
            except (ValueError, TypeError):
                continue

            code = get_country_code(country)

            if code:
                cc_populations[code] = population

# Create the world map.
wm = World()
wm.title = 'World Population in 2010, by Country'
wm.add('2010', cc_populations)

# Save the map.
wm.render_to_file('world_population.svg')

print(f'World population map saved with {len(cc_populations)} countries.')
print('Output file: world_population.svg')