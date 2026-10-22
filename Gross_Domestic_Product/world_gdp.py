import json
import pygal

from country_codes import get_country_code


# Load the GDP data.
with open('gdp.json', encoding='utf-8') as file:
    gdp_data = json.load(file)

# Convert GDP records into a dictionary.
country_gdp = {}

for record in gdp_data:
    country_name = record['country']
    gdp = record['gdp_billions']

    # Convert the country name into a Pygal two-letter code.
    country_code = get_country_code(country_name)

    if country_code is None:
        print(f"Country code not found for: {country_name}")
        continue

    country_gdp[country_code] = gdp

# Create the world map.
world_map = pygal.maps.world.World()
world_map.title = 'Gross Domestic Product by Country (GDP in Billions)'
world_map.add('GDP (billions)', country_gdp)

# Save the map.
world_map.render_to_file('world_gdp.svg')

print(f'Countries plotted: {len(country_gdp)}')
print('Map saved as world_gdp.svg')
