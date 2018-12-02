import os
import pathlib


def working_dir():
    return os.getcwd()


def make_a_folder(folder_to_make):
    pathlib.Path(folder_to_make).mkdir(parents=True, exist_ok=True)


def make_sub_folders(parent_folder, num_sub_folders):
    for x in range(1, num_sub_folders):
        pathlib.Path(parent_folder + '/' + '{:02d}'.format(x)).mkdir(parents=True, exist_ok=True)
