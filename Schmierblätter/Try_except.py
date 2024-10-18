command_input = 'Hello my guest'

splitted_command = command_input.split()
print(splitted_command)
if len(splitted_command) == 0:
    print("No command entered.")


# Extrahiere den Befehl (erste Teile) und ggf. Argumente (restliche Teile)
base_command = ' '.join(splitted_command[:2])  # Erster und zweiter Teil des Befehls
args = splitted_command[2:]  # Alle weiteren Teile als Argumente
print(splitted_command)
print(base_command)
print(args)
