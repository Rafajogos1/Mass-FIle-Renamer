from utilities import clear_console
import os

def suffix_add(path_to_files, suffix):
    files = os.listdir(path_to_files) #Get the path to look for files.

    for file_name in files: #Search all the entries inside the path.
        base_name, extension = os.path.splitext(file_name) #Split the name from the extension.
        new_file_name = base_name + suffix + extension #Add the suffix to the file name.
        old_path = os.path.join(path_to_files, file_name) #Make the path with the file prior to renaming.
        new_path = os.path.join(path_to_files, new_file_name) #Make the path with the soon to be renamed file.
        if os.path.exists(new_path): #Check if there is already a file with the same name as the new name and skips it if so.
            print('\033[93m' + f"File '{new_file_name}' already exists. Skipping..." + '\033[0m')
        else: #Rename the file if there aren't conflicting files.
            os.rename(old_path, new_path)

    if not files: #Warn the user that no changes were made.
        print('\033[93m' + "No files were present in the specified directory.\n" + '\033[0m')
    else:
        print('\033[32m' + "Operation completed.\n" + '\033[0m')
    return

def suffix_add_substring(path_to_files, suffix, substring): #Add a suffix to files with a certain substring.
    files = os.listdir(path_to_files) #Get the path to look for files.
    file_num = len(files) #The amount of files in the directory.
    file_count = 0 #A variable to count how many files it encountered whose name wasn't changed.

    for file_name in files: #Search all the entries inside the path.
        if substring in file_name: #Search for the substring in a file's name.
            base_name, extension = os.path.splitext(file_name) #Split the name from the extension.
            new_file_name = base_name + suffix + extension #Add the suffix to the file name.
            old_path = os.path.join(path_to_files, file_name) #Make the path with the file prior to renaming.
            new_path = os.path.join(path_to_files, new_file_name) #Make the path with the soon to be renamed file.
            if os.path.exists(new_path): #Check if there is already a file with the same name as the new name and skips it if so.
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

def suffix_mode(path_to_files): #Add a suffix to all files.
    #Ask for user input
    suffix = input("Please input the text you want to add at the end:\n")
    clear_console()
    suffix_add(path_to_files, suffix)
    return

def suffix_mode_substring(path_to_files): #Add a suffix to all files containing a substring.
    #Ask for user input
    suffix = input("Please input the text you want to add at the end:\n")
    substring = input("Please input the text you want the files you want to rename to contain:\n")
    clear_console()
    suffix_add_substring(path_to_files, suffix, substring)
    return