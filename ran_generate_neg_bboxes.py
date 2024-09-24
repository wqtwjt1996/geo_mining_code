import geopandas as gpd
import random
from shapely.geometry import box

shp_file = '/Users/wangqitong/学习资料/Fall2024_Geo_Transfer/Sep2024_QGIS_Country_Split/Co/bbox_v1_Co_DRC_rec.shp'
num_negatives = 5 
output_file = ('/Users/wangqitong/学习资料/Fall2024_Geo_Transfer/'
               'Sep2024_QGIS_Country_Split/Co/bbox_v1_Co_DRC_rec_neg') + str(num_negatives) + '.shp'
min_ran_box_hw = 0.01
max_ran_box_hw = 0.1

def generate_negative_bboxes(shp_file, num_negatives, output_file):
    gdf = gpd.read_file(shp_file)

    positive_bboxes = [row.geometry.bounds for row in gdf.itertuples()]

    negative_bboxes = []

    while len(negative_bboxes) < num_negatives:
        min_x = random.uniform(positive_bboxes[0][0]-0.1, positive_bboxes[0][0]+0.1)
        min_y = random.uniform(positive_bboxes[0][1]-0.1, positive_bboxes[0][1]+0.1) 
        width = random.uniform(min_ran_box_hw, max_ran_box_hw) 
        height = random.uniform(min_ran_box_hw, max_ran_box_hw) 

        neg_bbox = box(min_x, min_y, min_x + width, min_y + height)

        if not any(neg_bbox.intersects(box(*pb)) for pb in positive_bboxes):
            negative_bboxes.append(neg_bbox)

    neg_gdf = gpd.GeoDataFrame(geometry=negative_bboxes, crs=gdf.crs)

    neg_gdf.to_file(output_file)


generate_negative_bboxes(shp_file, num_negatives, output_file)
