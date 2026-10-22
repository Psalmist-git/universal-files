from pygal_maps_world.maps import World

# Create the world map.
wm = World()
wm.title = 'Regions of America, Africa, and Asia'

# North America.
wm.add('North America', [
    'ca', 'us', 'mx'
])

# Central America.
wm.add('Central America', [
    'bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'
])

# South America.
wm.add('South America', [
    'ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf',
    'gy', 'pe', 'py', 'sr', 'uy', 've'
])

# Western Africa.
wm.add('Western Africa', [
    'bj', 'bf', 'cv', 'ci', 'gm', 'gh', 'gn',
    'gw', 'lr', 'ml', 'mr', 'ne', 'ng', 'sn',
    'sl', 'tg'
])

# Eastern Africa.
wm.add('Eastern Africa', [
    'bi', 'km', 'dj', 'er', 'et', 'ke', 'mg',
    'mw', 'mu', 'mz', 'rw', 'sc', 'so', 'ss',
    'tz', 'ug'
])

# Southern Africa.
wm.add('Southern Africa', [
    'bw', 'ls', 'na', 'za', 'sz', 'zm', 'zw'
])

# Asia.
wm.add('Asia', [
    'af', 'am', 'az', 'bh', 'bd', 'bt', 'bn',
    'kh', 'cn', 'cy', 'ge', 'in', 'id', 'ir',
    'iq', 'il', 'jp', 'jo', 'kz', 'kw', 'kg',
    'la', 'lb', 'my', 'mv', 'mn', 'mm', 'np',
    'kp', 'om', 'pk', 'ps', 'ph', 'qa', 'sa',
    'sg', 'kr', 'lk', 'sy', 'tw', 'tj', 'th',
    'tl', 'tr', 'tm', 'ae', 'uz', 'vn', 'ye'
])

# Save the map.
wm.render_to_file('world_regions.svg')

print('Combined world regions map saved as world_regions.svg')