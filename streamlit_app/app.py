import streamlit as st
from etl import load_data
import geopandas as gpd
import pandas as pd
from config import STREAMLIT_SHP
import os
import pydeck as pdk



SCALLING_FACTOR = {

}

@st.cache_data
def load_gdf_data(ano:int, STREAMLIT_SHP=STREAMLIT_SHP) -> gpd.GeoDataFrame:
    """Load data from the ETL module."""

    STREAMLIT_SHP = STREAMLIT_SHP.format(ano=ano)
    if not os.path.exists(STREAMLIT_SHP):
        gdf = load_data(ano)
        gdf.to_file(STREAMLIT_SHP)
    else:
        gdf = gpd.read_file(STREAMLIT_SHP)
    gdf = gdf.to_crs(epsg=4326)
    
    return gdf

def format_data(gdf:gpd.GeoDataFrame, ano:int, programa:str) -> pd.DataFrame:
    """Format the GeoDataFrame for display."""

    gdf = gdf[gdf["descricao programa"] == programa]

    gdf["coordinates"] = gdf["geometry"].apply(lambda geom: list(geom.exterior.coords))

    col_valores = f'valor {ano}'

    scaling_factor = SCALLING_FACTOR.get(programa, 1*10**-4)

    data = pd.DataFrame({
        "coordinates": gdf["coordinates"],
        "height": gdf[col_valores] * scaling_factor,
        "tooltip" : gdf["sg_subpref"],
    })

    return data

st.title("Caio vai arrumar isso aqui para ficar legal")
st.subheader(f"Um subtitulo interessante")

ANO = start_time = st.slider(
    "Selecione o ano",
    value=2024,
    min_value=2022,
    max_value=2025,
    step=1
)


gdf = load_gdf_data(ANO)


PROGRAMA = st.selectbox(
    "Selecione o programa",
    gdf["descricao programa"].unique()
    )

data: pd.DataFrame = format_data(gdf, ANO, PROGRAMA)


# Layer com extrusão
polygon_layer = pdk.Layer(
    "PolygonLayer",
    data=data,
    get_polygon="coordinates",
    get_fill_color="[255, 165, 0, 120]",
    get_elevation="height",
    elevation_scale=10,
    extruded=True,
    pickable=True
)

# Tooltip
tooltip = {
    "html": "<b>Subprefeitura:</b> {tooltip}",
    "style": {"backgroundColor": "white", "color": "black"}
}

# ViewState
view_state = pdk.ViewState(
    longitude=gdf.geometry.centroid.x.mean(),
    latitude=gdf.geometry.centroid.y.mean(),
    zoom=12,
    pitch=45
)

# ViewState
view_state = pdk.ViewState(
    longitude=gdf.geometry.centroid.x.mean(),
    latitude=gdf.geometry.centroid.y.mean(),
    zoom=9,
    pitch=45
)


# Renderiza o mapa
st.pydeck_chart(pdk.Deck(
    layers=[polygon_layer],
    initial_view_state=view_state,
    tooltip=tooltip
))