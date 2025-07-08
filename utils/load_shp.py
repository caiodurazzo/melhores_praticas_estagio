import os
import geopandas as gpd
from config import data_folder

def load_shp(folder_name: str, 
             file_name: str = "data.shp", 
             **read_kwargs) -> gpd.GeoDataFrame:
    """
    
    Carrega um .shp de uma subfolder dentro da data_folder

    Args:
        folder_name (str): nome da subfolder dentro da data_folder em que o .shp esta salvo
        file_name (str, opcional): nome do .shp
        **read_kwargs: palavras-chave adicionais passadas para geopandas.read_file()
    
    Retorna:
        gpd.GeoDataFrame: geodataframe carregado
    
    """

    file_path = os.path.join(data_folder, folder_name, file_name)

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"O .shp {file_name} não existe em {os.path.join(data_folder, folder_name)}")
    
    return gpd.read_file(file_path, **read_kwargs)