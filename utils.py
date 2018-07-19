import os
import zipfile
import json
from math import sqrt
from random import sample

# Rename the built-in zip (http://docs.python.org/3/library/functions.html#zip)
_zip = zip

def help_directory(filename):
    """Create a directory called 'dataset' and put the zip file in it."""
    dataset_directory = os.path.join(os.getcwd(), 'dataset')
    if not os.path.exists(dataset_directory):
        os.mkdir(dataset_directory)
        current_directory = os.path.join(os.getcwd(), filename)
        moveto_directory = os.path.join(dataset_directory, filename)
        os.rename(current_directory, moveto_directory)

        """Extract all the files."""
        my_zip = zipfile.ZipFile(moveto_directory, 'r')
        my_zip.extractall(dataset_directory)

def tolist(path):
    """Append directory to a list."""
    with open(path) as file:
        l = []
        for r in file:
            l.append(r)
    return l

def load_file(path):
    """Load the json file."""
    return map(json.loads, tolist(path))

def load_las_vegas_rest(path):
    """Create restaurant objects."""
    with open(path) as file:
        restaurant_data = [json.loads(obj) for obj in file]
    bus_to_rest = {}
    for restaurant in restaurant_data:
        categories = restaurant['categories']
        if restaurant['city'] == 'Las Vegas' and 'Restaurants' in categories:
            name = restaurant['name']
            location = float(restaurant['latitude']), float(restaurant['longitude'])
            stars = restaurant['stars']
            num_reviews = restaurant['review_count']
            business_id = restaurant['business_id']
            restaurant = [name, location, categories, stars, num_reviews]
            bus_to_rest[business_id] = restaurant
    return list(bus_to_rest.values())

def distance(pos1, pos2):
    """Returns the Euclidean distance between pos1 and pos2, which are pairs."""
    return sqrt((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2)

def mean(s):
    """Returns the arithmetic mean of a sequence of numbers s."""
    assert len(s) != 0
    return sum(s) / len(s)

def zip(*sequences):
    """Returns a list of lists, where the i-th list contains the i-th
    element from each of the argument sequences."""
    return list(map(list, _zip(*sequences)))
