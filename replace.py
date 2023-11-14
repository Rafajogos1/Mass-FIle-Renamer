from utilities import clear_console
import os

def string_replace(path_to_files, old_substring, new_substring): #The renaming function of the "Replace Mode".
    files = os.listdir(path_to_files) #Get the path to look for files.
    file_num = len(files) #The amount of files in the directory.
    file_count = 0 #A variable to count how many files it encountered whose name wasn't changed.

    for file_name in files: #Search all the entries inside the path.
        if old_substring in file_name: #Search for the old substring in a file's name.
            new_file_name = file_name.replace(old_substring, new_substring) #Create the new name by replacing the old substring with the new one.
            old_path = os.path.join(path_to_files, file_name) #Make the path with the file prior to renaming.
            new_path = os.path.join(path_to_files, new_file_name) #Make the path with the soon to be renamed file.
            if os.path.exists(new_path): #Check if there is already a file with the same name as the new name and skips it if so.
                print(f"File '{new_file_name}' already exists. Skipping...")
            else: #Rename the file if there aren't conflicting files.
                os.rename(old_path, new_path)
        else: #Count one file whose name wasn't changed.
            file_count += 1

    if file_count == file_num: #Warn the user that no changes were made.
        print("No file containing the provided text was found.\n")
    else:
        print("Operation completed.\n")
    return

def replace_mode(path_to_files): #Replace substring with a new one.
    #Ask for user input
    old_text = input("Please input the text you want to replace:\n")
    new_text = input("\nPlease input the text you want to replace the old text with:\n")
    clear_console()
    string_replace(path_to_files, old_text, new_text)
    return