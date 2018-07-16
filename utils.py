import os
import zipfile

def help_directory(filename):
    # Create a directory called 'dataset' and put the zip file in it.
    dataset_directory = os.path.join(os.getcwd(), 'dataset')
    os.mkdir(dataset_directory)
    current_directory = os.path.join(os.getcwd(), filename)
    moveto_directory = os.path.join(dataset_directory, filename)
    os.rename(current_directory, moveto_directory)

    # Extract all the files.
    my_zip = zipfile.ZipFile(moveto_directory, 'r')
    my_zip.extractall(dataset_directory)
