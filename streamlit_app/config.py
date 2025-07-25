import os


data_folder = '../notebooks/data'


def get_data_path(filename):
    """
    Returns the full path to a data file in the data folder.
    
    :param filename: Name of the file to retrieve.
    :return: Full path to the specified data file.
    """
    return os.path.abspath(os.path.join(data_folder, filename))

