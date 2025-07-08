import os
import geopandas as gpd
from config import data_folder

def save_shp(gdf: gpd.GeoDataFrame, folder_name: str):
    """
    
    Salva um geodataframe como .shp na data_folder

    Args:
        gdf: geodataframe a ser salvo
        folder_name: nome da subfolder (dentro da data_folder) para salvar o .shp
    
    """
    
    save_path = os.path.join(data_folder, folder_name)

    if not os.path.exists(save_path):
        os.makedirs(save_path)

        file_path = os.path.join(save_path, "data.shp")

        gdf.to_file(file_path)

        print(f"Shapefile salvo em {file_path}")