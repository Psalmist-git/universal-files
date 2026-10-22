from pygal_maps_world.i18n import COUNTRIES


def get_country_code(country_name):
    """Return the Pygal two-letter country code."""

    for code, name in COUNTRIES.items():
        if name.lower() == country_name.lower():
            return code

    special_cases = {
        'United States': 'us',
        'United States of America': 'us',
        'China': 'cn',
        'Germany': 'de',
        'Japan': 'jp',
        'India': 'in',
        'United Kingdom': 'gb',
        'France': 'fr',
        'Brazil': 'br',
        'Italy': 'it',
        'Canada': 'ca',
        'Russia': 'ru',
        'South Korea': 'kr',
        'North Korea': 'kp',
        'Iran': 'ir',
        'Vietnam': 'vn',
        'Turkey': 'tr',
        'Egypt': 'eg',
        'Yemen, Rep.': 'ye',
    }

    return special_cases.get(country_name)