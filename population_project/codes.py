from pygal_maps_world.i18n import COUNTRIES

def get_country_code(country_name):
    """Return the Pygal country code for a country name."""

    for code, name in COUNTRIES.items():
        if name == country_name:
            return code

    # Handle country names that differ between datasets.
    if country_name == 'Yemen, Rep.':
        return 'ye'
    elif country_name == 'Congo, Dem. Rep.':
        return 'cd'
    elif country_name == 'Congo, Rep.':
        return 'cg'
    elif country_name == 'Egypt, Arab Rep.':
        return 'eg'
    elif country_name == 'Iran, Islamic Rep.':
        return 'ir'
    elif country_name == 'Korea, Dem. People\'s Rep.':
        return 'kp'
    elif country_name == 'Korea, Rep.':
        return 'kr'
    elif country_name == 'Kyrgyz Republic':
        return 'kg'
    elif country_name == 'Lao PDR':
        return 'la'
    elif country_name == 'Slovak Republic':
        return 'sk'
    elif country_name == 'Venezuela, RB':
        return 've'
    elif country_name == 'Vietnam':
        return 'vn'
    elif country_name == 'Tanzania':
        return 'tz'
    elif country_name == 'Gambia, The':
        return 'gm'

    return None


print(get_country_code('Andorra'))
print(get_country_code('United Arab Emirates'))
print(get_country_code('Afghanistan'))
