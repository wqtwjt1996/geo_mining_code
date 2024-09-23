import geopandas as gpd
from shapely.geometry import box

original_shp_file_path = '/Users/wangqitong/学习资料/Fall2024_Geo_Transfer/Sep2024_QGIS_Country_Split/Co/bbox_v1_Co_DRC.shp'
output_shp_file_path = '/Users/wangqitong/学习资料/Fall2024_Geo_Transfer/Sep2024_QGIS_Country_Split/Co/bbox_v1_Co_DRC_rec.shp'


def create_bounding_boxes(original_gdf, output_path):
    # 创建一个列表用于存储边界框
    bounding_boxes_list = []

    # 遍历每个多边形，计算边界框并添加到列表
    for index, row in original_gdf.iterrows():
        # 计算边界框
        minx, miny, maxx, maxy = row['geometry'].bounds
        bbox = box(minx, miny, maxx, maxy)

        # 将边界框添加到列表
        bounding_boxes_list.append({'geometry': bbox})

    # 创建新的 GeoDataFrame
    bounding_boxes = gpd.GeoDataFrame(bounding_boxes_list, crs=original_gdf.crs)

    # 保存新的 GeoDataFrame 为 SHP 文件
    bounding_boxes.to_file(output_path)

# 示例用法
original_gdf = gpd.read_file(original_shp_file_path)
create_bounding_boxes(original_gdf, output_shp_file_path)
