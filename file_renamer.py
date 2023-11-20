from prefix import prefix_mode, prefix_mode_substring
from remove import remove_mode
from replace import replace_mode
from suffix import suffix_mode, suffix_mode_substring
from utilities import clear_console, get_path

def main_menu(path): #The main menu.
    while True:
        #Wait for user input
        print("Select mode:")
        print("1 - Replace text in the file name with a new one.")
        print("2 - Add a prefix to all files.")
        print("3 - Add a prefix to files containing certain text.")
        print("4 - Add a suffix to all files.")
        print("5 - Add a suffix to files containing certain text.")
        print("6 - Remove text from the name.")
        print("cd - Change the working path.")
        print("0 - Exit")
        user_input = input("Enter your choice:\n").lower()

        #Choice selection
        if user_input == '1': #Replace substring with a new one.
            clear_console()
            replace_mode(path)
        elif user_input == '2': #Add a prefix to all files.
            clear_console()
            prefix_mode(path)
        elif user_input == '3': #Add a prefix to all files containing a substring.
            clear_console()
            prefix_mode_substring(path)
        elif user_input == '4': #Add a suffix to all files.
            clear_console()
            suffix_mode(path)
        elif user_input == '5': #Add a suffix to all files containing a substring.
            clear_console()
            suffix_mode_substring(path)
        elif user_input == '6': #Remove substring.
            clear_console()
            remove_mode(path)
        elif user_input == 'cd': #Change the working path.
            clear_console()
            path = get_path()
        elif user_input == '0': #Exit the program.
            clear_console()
            print("Goodbye!")
            exit()
        else: #Invalid choice.
            clear_console()
            print("Invalid choice. Please enter a valid option.")

try:
    print('\033[91m' + "It is recommended to have a backup of your files!" + '\033[0m')
    print("Press \"CTRL + C\" at any time to exit the program.\n")
    path = get_path()
    main_menu(path)
except KeyboardInterrupt: #Exit if "CTRL + C" is pressed.
    exit()