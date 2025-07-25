import os


data_folder = '../notebooks/data'


def get_data_path(filename):
    """
    Returns the full path to a data file in the data folder.
    
    :param filename: Name of the file to retrieve.
    :return: Full path to the specified data file.
    """
    path = os.path.abspath(os.path.join(data_folder, filename))

    if not os.path.exists(path):
        raise ValueError(f"File '{filename}' not found in data folder.")
    return path


STREAMLIT_SHP = 'streamlit_data_{ano}.shp'
