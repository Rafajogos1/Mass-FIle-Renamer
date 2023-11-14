from prefix import prefix_mode, prefix_mode_substring
from remove import remove_mode
from replace import replace_mode
from suffix import suffix_mode, suffix_mode_substring
from utilities import clear_console

def main_menu(): #The main menu.
    while True:
        folder_to_rename = '.'

        #Wait for user input
        print("Select mode:")
        print("1 - Replace text in the file name with a new one.")
        print("2 - Add a prefix to all files.")
        print("3 - Add a prefix to files containing certain text.")
        print("4 - Add a suffix to all files.")
        print("5 - Add a suffix to files containing certain text.")
        print("6 - Remove text from the name.")
        print("0 - Exit")
        user_input = input("Enter your choice:\n")

        #Choice selection
        if user_input == '1': #Replace substring with a new one.
            clear_console()
            replace_mode(folder_to_rename)
        elif user_input == '2': #Add a prefix to all files.
            clear_console()
            prefix_mode(folder_to_rename)
        elif user_input == '3': #Add a prefix to all files containing a substring.
            clear_console()
            prefix_mode_substring(folder_to_rename)
        elif user_input == '4': #Add a suffix to all files.
            clear_console()
            suffix_mode(folder_to_rename)
        elif user_input == '5': #Add a suffix to all files containing a substring.
            clear_console()
            suffix_mode_substring(folder_to_rename)
        elif user_input == '6': #Remove substring.
            clear_console()
            remove_mode(folder_to_rename)
        elif user_input == '0': #Exit the program.
            clear_console()
            print("Exiting program...")
            exit()
        else: #Invalid choice.
            clear_console()
            print("Invalid choice. Please enter a valid option.")

try:
    print('\033[91m' + "It is recommended to have a backup of your files!" + '\033[0m')
    print("Press \"CTRL + C\" at any time to exit the program.\n")
    main_menu()
except KeyboardInterrupt: #Exit if "CTRL + C" is pressed.
    exit()