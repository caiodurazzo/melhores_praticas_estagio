import os
import pandas as pd
import geopandas as gpd
from config import get_data_path


def load_csv(filename:str, **read_kwargs)->pd.DataFrame:
    """
    Loads a CSV file into a pandas DataFrame.
    
    :param filename: Name of the CSV file to load.
    :return: DataFrame containing the data from the CSV file.
    """

    if not filename.endswith('.csv'):
        raise ValueError("Filename must end with '.csv'")

    data_path = get_data_path(filename)
    return pd.read_csv(data_path, **read_kwargs)


def load_shapefile(filename:str, **read_kwargs)->gpd.GeoDataFrame:
    """
    Loads a shapefile into a GeoDataFrame.
    
    :param filename: Name of the shapefile to load.
    :return: GeoDataFrame containing the data from the shapefile.
    """

    if not filename.endswith('.shp'):
        raise ValueError("Filename must end with '.shp'")

    data_path = get_data_path(filename)
    
    gdf = gpd.read_file(data_path, **read_kwargs)
    if not isinstance(gdf, gpd.GeoDataFrame):
        raise ValueError("Loaded data is not a GeoDataFrame")
    return gdf