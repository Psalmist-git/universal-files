import pygal
from pygal_maps_world.maps import World

# Create a world map.
wm = World()
wm.title = 'Western, Eastern, and Southern Africa'

# Western African countries.
wm.add('Western Africa', [
    'bj',  # Benin
    'bf',  # Burkina Faso
    'cv',  # Cabo Verde
    'ci',  # Côte d'Ivoire
    'gm',  # Gambia
    'gh',  # Ghana
    'gn',  # Guinea
    'gw',  # Guinea-Bissau
    'lr',  # Liberia
    'ml',  # Mali
    'mr',  # Mauritania
    'ne',  # Niger
    'ng',  # Nigeria
    'sn',  # Senegal
    'sl',  # Sierra Leone
    'tg',  # Togo
])

# Eastern African countries.
wm.add('Eastern Africa', [
    'bi',  # Burundi
    'km',  # Comoros
    'dj',  # Djibouti
    'er',  # Eritrea
    'et',  # Ethiopia
    'ke',  # Kenya
    'mg',  # Madagascar
    'mw',  # Malawi
    'mu',  # Mauritius
    'mz',  # Mozambique
    'rw',  # Rwanda
    'sc',  # Seychelles
    'so',  # Somalia
    'ss',  # South Sudan
    'tz',  # Tanzania
    'ug',  # Uganda
    'zm',  # Zambia
    'zw',  # Zimbabwe
])

# Southern African countries.
wm.add('Southern Africa', [
    'bw',  # Botswana
    'ls',  # Lesotho
    'na',  # Namibia
    'za',  # South Africa
    'sz',  # Eswatini
])

# Save the map.
wm.render_to_file('africa.svg')

print('African map saved as africa.svg')