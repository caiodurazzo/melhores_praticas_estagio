import pandas as pd
import geopandas as gpd
from utils import get_data_path, load_csv, load_shapefile


class DataLoader:

    def load_data(self):

        df_ppa = load_csv('ppa_reg.csv')
        gdf=load_shapefile('subprefs/subprefs.shp')[['nm_subpref', 'sg_subpref', 'geometry']]
        return df_ppa, gdf

    def agrupar_por_subprefeitura(self, df_ppa:pd.DataFrame, ano:int) -> pd.DataFrame:
    
        col_valor = f"valor {ano}"
        group_columns = [
            'descricao programa',
            "descricao prefeitura regional"
        ]
        columns = group_columns + [col_valor]
        df_ppa = df_ppa[columns].copy()

        df_ppa = df_ppa.groupby(group_columns)[col_valor].sum().reset_index()

        return df_ppa


    def merge_com_subs(self, df_ppa:pd.DataFrame, gdf:gpd.GeoDataFrame) -> gpd.GeoDataFrame:
        """
        Merges the PPA DataFrame with the GeoDataFrame of subprefectures.
        
        :param df_ppa: DataFrame containing PPA data.
        :param gdf: GeoDataFrame of subprefectures.
        :return: Merged GeoDataFrame.
        """

        gdf_mapa = gdf.merge(df_ppa, 
                                    how = "left", 
                                    left_on = "nm_subpref", 
                                    right_on = "descricao prefeitura regional")
        
        return gdf_mapa
    
    def pipeline(self):

        df_ppa, gdf = self.load_data()
        merged = self.agrupar_por_subprefeitura(df_ppa, 2024)
        gdf_mapa = self.merge_com_subs(merged, gdf)
        
        return gdf_mapa
    
    def __call__(self) -> gpd.GeoDataFrame:
        return self.pipeline()
    

load_data = DataLoader()