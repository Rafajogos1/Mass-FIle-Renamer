import os

def clear_console(): #Cleans the console
    if os.name == 'nt': # For Windows
        _ = os.system('cls')
    else: # For Mac and Linux
        _ = os.system('clear')