from load_data import load_data


def list_help():
    print("Available commands:")
    print("1. 'help' - Prints a list of all commands.")
    print("2. 'show countries' - Prints list of all countries of the ships without duplicates in alphabetical order.")
    print("3. 'top countries <num_countries>' - Prints a list of top countries with the most ships.")
    print("4. 'ships by type <num_ship_types>' - Prints a list of top ship types.")
    print("5. 'search ship' - Prints all the ships with similar names respective to the search.")

def get_command(all_data):
    """Prints a list of available commands and executes the function for it."""
    command = input('')
    commands = {
        'help': list_help,
        'show countries': show_countries,
        'top countries': top_countries,
        'ships by type' : ships_by_type,
        'search ship' : search_ship
    }
    requires_all_data = ['show countries', 'search ship']


    if command in commands:
        if command in requires_all_data:
            commands[command](all_data)
        else:
            splitted_command = command.split(' ')
            if len(splitted_command) == 3:
                if splitted_command[0] == 'top' and splitted_command[1] == 'countries' and splitted_command[2].isdigit():
                    count_top = splitted_command[2]
                    commands[command](all_data, count_top)
                elif splitted_command[0] == 'ships' and splitted_command[1] == 'by'and splitted_command[2] == 'type' and splitted_command[3].isdigit():
                    count_top = int(splitted_command[3])
                    commands[command](all_data, count_top)
            else:
                commands[command]()
    else:
        print(f'Unknown command {command}')


def count_search_type_appearances(all_data, search_type):
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
    count_countrys = count_search_type_appearances(all_data, 'COUNTRY')
    list_of_countrys = []
    for ship in count_countrys:
        list_of_countrys.append(ship)
    list_of_countrys.sort()
    for country in list_of_countrys:
        print(country)


def print_top_search_type(input_top_length, count_key):
    """Prints the keys and values of a dict in order from biggest value to smallest """
    dict_of_top_key = {}
    for _ in range(input_top_length):
        biggest_value = 0
        biggest_key = None
        for key, value in count_key.items():
            if value >= biggest_value:
                biggest_value = value
                biggest_key = key
        dict_of_top_key[biggest_key] = biggest_value
        del count_key[biggest_key]  # Delete key from old dict, so we can search for the next key with most appearences.
    for i, (key, value) in enumerate(dict_of_top_key.items(), 1):
        print(f'{i}. {key}: {value}')


def top_countries(all_data, count_top):
    """Gets function print_top_search_type to print top countries"""
    count_countrys = count_search_type_appearances(all_data, 'COUNTRY')
    print_top_search_type(count_top, count_countrys)


def ships_by_type(all_data, count_top):
    """Gets function print_top_search_type to print top ships by type"""
    count_ship_types = count_search_type_appearances(all_data, 'TYPE_SUMMARY')
    print_top_search_type(count_top, count_ship_types)


def search_ship(all_data):
    user_search_ships = input('Enter a ship name you want to search for:')
    dict_of_ships = count_search_type_appearances(all_data, 'SHIPNAME')
    list_of_ships = []
    for ship in dict_of_ships:
        if user_search_ships.lower() in ship.lower():
            print(ship)


def speed_histogram():
    pass


def main():
    all_data = load_data()
    while True:
       get_command(all_data)


if __name__ == "__main__":
        main()



#FINISH, dann kuck ob du es noch implementieren kannst, dass wenn man top_countries 5
# eingibt nicht erst dein aufruf für eine weitere zahl kommt sondern direkt die verarbeitung
