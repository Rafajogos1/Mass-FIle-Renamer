import os

def clear_console(): #Cleans the console
    if os.name == 'nt': # For Windows
        _ = os.system('cls')
    else: # For Mac and Linux
        _ = os.system('clear')

def get_path(): #Asks user for the path to work with
    while True:
        path = input("Please input the directory that you want to work with:\n")

        if os.path.exists(path):
            clear_console()
            print('\033[32m' + f"Currently working on \"{path}\".\n" + '\033[0m')
            return path
        else:
            clear_console()
            print('\033[91m' + f"The path \"{path}\" does not exist." + '\033[0m')