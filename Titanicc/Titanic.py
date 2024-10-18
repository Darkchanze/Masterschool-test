from load_data import load_data
import matplotlib

def help(all_data):
    """Prints a list of available commands and executes the function for it."""
    print("Available commands:")
    print("1. 'help' - Prints a list of all commands.")
    print("2. 'show countries' - Prints list of all countries of the ships without duplicates in alphabetical order.")
    print("3. 'top countries' - Prints a list of top countries with the most ships.")
    print("4. 'ships by type' - Prints a list of top ship types.")
    print("5. 'search ship' - Prints all the ships with similar names respective to the search.")

    command = input('Enter a command:')
    commands = {
        'help': help,
        'show countries': show_countries,
        'top countries': top_countries,
        'ships by type' : ships_by_type,
        'search ship' : search_ship
    }

    if command in commands:
        commands[command](all_data)


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


def get_input_top_countries(topic):
    """Returns the length of the top list input from the user and handels exceptions"""
    while True:
        try:
            count_top = int(input(f'Enter a number to set the count of the top {topic}:'))
            return count_top
        except ValueError:
            print('Please enter a number and not letters')


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


def top_countries(all_data):
    """Gets function print_top_search_type to print top countries"""
    count_top = get_input_top_countries('countrys')
    count_countrys = count_search_type_appearances(all_data, 'COUNTRY')
    print_top_search_type(count_top, count_countrys)


def ships_by_type(all_data):
    """Gets function print_top_search_type to print top ships by type"""
    count_top = get_input_top_countries('ship types')
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
    #while True:
     #   help(all_data)
    if __name__ == '__main__':
        if __name__ == '__main__':
            matplotlib.main()


if __name__ == "__main__":
        main()



#FINISH, dann kuck ob du es noch implementieren kannst, dass wenn man top_countries 5
# eingibt nicht erst dein aufruf für eine weitere zahl kommt sondern direkt die verarbeitung
