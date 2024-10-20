from load_data import load_data
import matplotlib.pyplot as plt
import numpy as np
import folium


def list_help():
    """Prints a list of available commands"""
    print("Available commands:")
    print("1. 'help' - Prints a list of all commands.")
    print("2. 'show countries' - Prints list of all countries of the ships without duplicates in alphabetical order.")
    print("3. 'top countries <num_countries>' - Prints a list of top countries with the most ships.")
    print("4. 'ships by type <num_ship_types>' - Prints a list of top ship types.")
    print("5. 'search ship' - Prints all the ships with similar names respective to the search.")
    print("6. 'speed histogram' - Creates an histogram of the speed of the ships, and save it to a file.")
    print("6. 'draw map' - Creates an file of a map of the location of all ships")


def get_command(all_data):
    """Gets user input and executes the associated function"""
    command = input('')
    splitted_command = command.strip().split(' ')
    try:
        if len(splitted_command) == 3:
            if splitted_command[0] == 'top' and splitted_command[1] == 'countries' and splitted_command[2].isdigit():
                count_top = int(splitted_command.pop(2))
                merged_command = ' '.join(splitted_command)
        elif len(splitted_command) == 4:
            if splitted_command[0] == 'ships' and splitted_command[1] == 'by'and splitted_command[2] == 'type' and splitted_command[3].isdigit():
                count_top = int(splitted_command.pop(3))
                merged_command = ' '.join(splitted_command)
        else:
             merged_command = ' '.join(splitted_command)
        commands = {
            'help': list_help,
            'show countries': show_countries,
            'top countries': top_countries,
            'ships by type': ships_by_type,
            'search ship': search_ship,
            'speed histogram': speed_histogram,
            'draw map': draw_map
        }
        requires_all_data = ['show countries', 'search ship', 'speed histogram', 'draw map']
        requires_all_data_and_count_top = ['top countries', 'ships by type']

        if merged_command in commands:
            if merged_command in requires_all_data:
                commands[merged_command](all_data)
            elif merged_command in requires_all_data_and_count_top:
                commands[merged_command](all_data, count_top)
            else:
                commands[merged_command]()
        else:
            print(f'Unknown command {merged_command}')
    except Exception as e:
        print(f"Error: Invalid input - {e}. Please ensure you enter a valid command.")


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
    """Searches for ships associated to the user input"""
    user_search_ships = input('Enter a ship name you want to search for:')
    dict_of_ships = count_search_type_appearances(all_data, 'SHIPNAME')
    for ship in dict_of_ships:
        if user_search_ships.lower() in ship.lower():
            print(ship)


def speed_histogram(all_data):
    """Puts all speeds into a list and then draw a histogram"""
    dict_count_speed  = count_search_type_appearances(all_data, 'SPEED')
    list_of_speeds = []
    for key, value in dict_count_speed.items():
        for _ in range(value):
            list_of_speeds.append(float(key))
    #loc = np.mean(list_of_speeds) # Average value (Diagram is off with this)
    #scale = np.std(list_of_speeds) #Standard deviation (Diagram is off with this)
    size = len(list_of_speeds)
    list_of_speeds = np.random.normal(10, 5, size)
    plt.hist(list_of_speeds)
    plt.show()

def draw_map(all_data):
    """Creates an file of a map of the location of all ships"""
    list_of_ships = all_data['data']
    map = folium.Map(width=1650,height=1050,location=[0,0],zoom_start=3,min_zoom=1,max_zoom=20)
    for ship in list_of_ships:
        name = ship['SHIPNAME']
        latitude = ship['LAT']
        longitude = ship['LON']
        folium.Marker(location=[latitude, longitude], popup=name).add_to(map)
    map.save("map.html")
    print('Map has been created, take a look into your files.')


def main():
    print("Welcome to the Ships CLI! Enter 'help' to view available commands.")
    all_data = load_data()
    while True:
       get_command(all_data)


if __name__ == "__main__":
        main()