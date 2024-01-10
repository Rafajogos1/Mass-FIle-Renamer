from utilities import clear_console
import os

def string_replace(path_to_files, old_substring, new_substring): #The renaming function of the "Replace Mode".
    files = os.listdir(path_to_files) #Get the path to look for files.
    file_num = len(files) #The amount of files in the directory.
    file_count = 0 #A variable to count how many files it encountered whose name wasn't changed.

    for file_name in files: #Search all the entries inside the path.
        if old_substring in file_name: #Search for the old substring in a file's name.
            base_name, extension = os.path.splitext(file_name) #Split the name from the extension.
            new_file_name = base_name.replace(old_substring, new_substring) + extension #Create the new name by replacing the old substring with the new one.
            old_path = os.path.join(path_to_files, file_name) #Make the path with the file prior to renaming.
            new_path = os.path.join(path_to_files, new_file_name) #Make the path with the soon to be renamed file.
            if old_substring == extension: #Check if the user tried to change the extension and warn them that it is not possible.
                print('\033[91m' + "The file extension cannot be altered.\n" + \
                      "If a text matching the extension is found before the extension itself it will still be replaced." + '\033[0m')
            elif os.path.exists(new_path): #Check if there is already a file with the same name as the new name and skips it if so.
                print('\033[93m' + f"File '{new_file_name}' already exists. Skipping..." + '\033[0m')
            else: #Rename the file if there aren't conflicting files.
                os.rename(old_path, new_path)
        else: #Count one file whose name wasn't changed.
            file_count += 1

    if file_count == file_num: #Warn the user that no changes were made.
        print('\033[93m' + "No file containing the provided text was found.\n" + '\033[0m')
    else:
        print('\033[32m' + "Operation completed.\n" + '\033[0m')
    return

def replace_mode(path_to_files): #Replace substring with a new one.
    #Ask for user input
    old_text = input("Please input the text you want to replace:\n")
    new_text = input("\nPlease input the text you want to replace the old text with:\n")
    clear_console()
    string_replace(path_to_files, old_text, new_text)
    return