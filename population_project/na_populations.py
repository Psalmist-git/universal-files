from pygal_maps_world.maps import World

# Create a world map.
wm = World()
wm.title = 'Population of Countries Across the World'

# Africa: Nigeria, Egypt, and South Africa.
wm.add('Africa', {
    'ng': 237500000,
    'eg': 118400000,
    'za': 64700000,
})

# Asia: India, China, and Japan.
wm.add('Asia', {
    'in': 1450000000,
    'cn': 1410000000,
    'jp': 123000000,
})

# Europe: United Kingdom, France, and Germany.
wm.add('Europe', {
    'gb': 69500000,
    'fr': 66600000,
    'de': 84000000,
})

# North America: United States, Mexico, and Canada.
wm.add('North America', {
    'us': 347000000,
    'mx': 132000000,
    'ca': 41300000,
})

# South America: Brazil, Colombia, and Argentina.
wm.add('South America', {
    'br': 213000000,
    'co': 53300000,
    'ar': 45800000,
})

# Oceania: Australia, Papua New Guinea, and New Zealand.
wm.add('Oceania', {
    'au': 27100000,
    'pg': 11000000,
    'nz': 5300000,
})

# Save the map.
wm.render_to_file('world_populations.svg')

print('World population map saved as world_populations.svg')