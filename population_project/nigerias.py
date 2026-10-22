from pygal_maps_world.maps import World

# Create a world map.
wm = World()
wm.title = 'Regions of Nigeria'

# Highlight Nigeria on the map.
wm.add('Nigeria', ['ng'])

# Save the map.
wm.render_to_file('nigeria.svg')

print('Map saved as nigeria.svg')
