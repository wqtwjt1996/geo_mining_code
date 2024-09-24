import geopandas as gpd

original_shp_file_path = '/Users/wangqitong/学习资料/Fall2024_Geo_Transfer/Jul2024_QGIS/Co/bbox_v1_Co.shp'
output_shp_file_path = '/Users/wangqitong/学习资料/Fall2024_Geo_Transfer/Sep2024_QGIS_Country_Split/Co/bbox_v1_Co_DRC.shp'  #
id_list = ['2010', '2020', '2030', '2040', '2050']

def filter_geodataframe_by_id_pattern(original_gdf, output_path, id_list):
    mask = original_gdf['id'].astype(str).str.startswith(tuple(id_list))
    filtered_gdf = original_gdf[mask]
    filtered_gdf.to_file(output_path)
    return filtered_gdf

# Usage
original_gdf = gpd.read_file(original_shp_file_path)
new_gdf = filter_geodataframe_by_id_pattern(original_gdf, output_shp_file_path, id_list)
print(new_gdf)

