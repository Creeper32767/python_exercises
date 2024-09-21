import json
import os
from shutil import copy
from sys import stdout

# global variables
minecraft_directory = os.path.abspath(input("[initalization] Please enter the full path of '.minecraft' directory: "))
indexes_path = os.path.join(minecraft_directory, "assets\\indexes")
assets_path = os.path.join(minecraft_directory, "assets\\objects")
direction_path = os.path.join(minecraft_directory, f"minecraft_assets\\")


def chooser(choices: list):
    """
    universal method to select one element in a list.

    Args:
        choices (list): alternative elements

    Returns:
        Any: one element of the choices
    """

    print("Here are several items to choose.")
    for item in choices:
        print(f"[{choices.index(item)}] {item}")

    choice = input("[chooser] Enter the order to choose one: ")
    try:
        return choices[int(choice)]
    except IndexError:
        return None


# processing part
index_file = chooser(os.listdir(indexes_path))
index_file = os.path.join(indexes_path, index_file)

with open(index_file) as f:
    objects = json.load(f)["objects"]
    count = 0

    for key1 in objects:
        if type(objects[key1]) == dict:
            # key1 -> relative file path
            # two values: hash and file_size(B)
            hash = objects[key1]["hash"]
            file_size = objects[key1]["size"]

            original_path = os.path.join(assets_path, f"{hash[:2]}\\{hash}")
            correct_path = os.path.abspath(os.path.join(direction_path, key1))
            # make directories if they don't exist
            if not os.path.exists(os.path.dirname(correct_path)):
                os.makedirs(os.path.dirname(correct_path))

            # copy and check file size
            try:
                copy(original_path, correct_path)
                size = os.path.getsize(correct_path)
                if size == file_size:
                    # count how many files have been copied
                    count += 1
                    stdout.flush()
                    stdout.write(f'\r[info] Successfully copied {str(count).ljust(9, " ")} files.')
                else:
                    print(f"\033[31m[warn] The file should take up {file_size}B, but we found that it takes up {size}B actually.\033[0m")

            # if original_path and correct_path are same 
            except shutil.SameFileError: 
                print("\033[31m[error] Source and destination represents the same file.\033[0m") 
            # if there is any permission problem 
            except PermissionError: 
                print("\033[31m[error] Permission denied.\033[0m") 
            # for other errors 
            except: 
                print("\033[31m[error] Error occurred while copying files.\033[0m")

# open the folder
os.system(f"explorer.exe {direction_path}")
input("Finished. Press 'Enter' to exit.")
