def get_formatted_location(city, country, population=""):
    if population:
        formatted_location = city + ', ' + country + ' - population ' + population
    else:
        formatted_location = city + ', ' + country
    return formatted_location.title()