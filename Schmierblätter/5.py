from load_data import load_data


def help(all_data):
    """Prints a list of available commands.###################"""
    print("Available commands:")
    print("1. 'show countries' - Prints list of all countries of the ships without duplicates in alphabetical order.")
    print("2. 'top countries' - Prints a list of top countries with the most ships.")
    command = input('Enter a command:')
    commands = {
        'help': help,
        'show countries': show_countries,
        'top countries': top_countries,
    }
    requires_all_data = ['show countries', 'top countries']
    if command in commands:
        if command in requires_all_data:
            commands[command](all_data)
        else:
            commands[command]()


def count_search_type_appearences(all_data, search_type):
    """Returns a dictionary that lists the search type from all_data and the value is the amount of appearences."""
    list_of_ships = all_data['data']
    count_countrys = {}
    for ship in list_of_ships:
        if ship[search_type] not in count_countrys:
            count_countrys[ship[search_type]] = 1
        else:
            count_countrys[ship[search_type]] += 1
    return count_countrys


def show_countries(all_data):
    """Loop through count_countrys to get all countrys into a list, then sort them and print"""
    count_countrys = count_search_type_appearences(all_data, 'COUNTRY')
    list_of_countrys = []
    for ship in count_countrys:
        list_of_countrys.append(ship)
    list_of_countrys.sort()
    for country in list_of_countrys:
        print(country)


def get_input_top_countries():
    while True:
        try:
            count_top = int(input('Enter a number to set the count of the top country:'))
            return count_top
        except ValueError:
            print('Please enter a number and not letters')


def print_top_search_type():


def top_countries(all_data):
    """Create loop through old dict and get the highest counted countrys into a new dict."""
    count_top = get_input_top_countries()
    count_countrys = count_search_type_appearences(all_data, 'COUNTRY')
    dict_of_top_countrys = {}
    for _ in range(count_top):
        biggest_amount = 0
        biggest_country = None
        for country, amount in count_countrys.items():
            if amount >= biggest_amount:
                biggest_amount = amount
                biggest_country = country
        dict_of_top_countrys[biggest_country] = biggest_amount
        del count_countrys[
            biggest_country]  # Delete country from old dict, so we can search for the next country with most appearences.
    for country, amount in dict_of_top_countrys.items():
        print(f'{country}: {amount}')


def ships_by_type(all_data):
    count_ship_types = count_search_type_appearences(all_data, 'TYPE_SUMMARY')


def search_ship():
    pass
    # SHIPNAME


def speed_histogram():
    pass


def main():
    all_data = load_data()
    # while True:
    #    help(all_data)
    print(ships_by_type(all_data))


if __name__ == "__main__":
    main()

# FINISH, dann kuck ob du es noch implementieren kannst, dass wenn man top_countries 5
# eingibt nicht erst dein aufruf für eine weitere zahl kommt sondern direkt die verarbeitung