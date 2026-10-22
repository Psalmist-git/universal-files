import json
from pathlib import Path
from pygal_maps_world.maps import World
from codes import get_country_code
from pygal.style import RotateStyle

# Load the population data.
with open('population_data.json', encoding='utf-8') as f:
    pop_data = json.load(f)

# Build a dictionary of population data for 2010.
cc_populations = {}

for pop_dict in pop_data:
    if str(pop_dict.get('Year')) == '2025':
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

# Group countries into three population levels.
cc_pops_1 = {}
cc_pops_2 = {}
cc_pops_3 = {}

for cc, pop in cc_populations.items():
    if pop < 10_000_000:
        cc_pops_1[cc] = pop
    elif pop < 1_000_000_000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

wm_style = RotateStyle('#336699')
wm = World(style=wm_style)

# Display the number of countries in each group.
print('Countries with fewer than 10 million people:', len(cc_pops_1))
print('Countries with 10 million to under 1 billion people:', len(cc_pops_2))
print('Countries with 1 billion or more people:', len(cc_pops_3))

# Create the world map.
wm = World()
wm.title = 'World Population in 2025, by Country'

wm.add('0–10 million', cc_pops_1)
wm.add('10 million–under 1 billion', cc_pops_2)
wm.add('1 billion or more', cc_pops_3)

# Save the map.
wm.render_to_file('world_population.svg')

print('Map saved as world_population.svg')