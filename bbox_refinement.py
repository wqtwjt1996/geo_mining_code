import geopandas as gpd
from shapely.geometry import box

original_shp_file_path = '/Users/wangqitong/学习资料/Fall2024_Geo_Transfer/Sep2024_QGIS_Country_Split/Co/bbox_v1_Co_DRC.shp'
output_shp_file_path = '/Users/wangqitong/学习资料/Fall2024_Geo_Transfer/Sep2024_QGIS_Country_Split/Co/bbox_v1_Co_DRC_rec.shp'


def create_bounding_boxes(original_gdf, output_path):
    bounding_boxes_list = []

    for index, row in original_gdf.iterrows():
        minx, miny, maxx, maxy = row['geometry'].bounds
        bbox = box(minx, miny, maxx, maxy)

        bounding_boxes_list.append({'geometry': bbox})

    bounding_boxes = gpd.GeoDataFrame(bounding_boxes_list, crs=original_gdf.crs)
    bounding_boxes.to_file(output_path)

original_gdf = gpd.read_file(original_shp_file_path)
create_bounding_boxes(original_gdf, output_shp_file_path)
