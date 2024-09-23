import geopandas as gpd
import random
from shapely.geometry import box

# 示例用法
shp_file = '/Users/wangqitong/学习资料/Fall2024_Geo_Transfer/Sep2024_QGIS_Country_Split/Co/bbox_v1_Co_DRC_rec.shp'
num_negatives = 5  # 生成的负样本数量
output_file = ('/Users/wangqitong/学习资料/Fall2024_Geo_Transfer/'
               'Sep2024_QGIS_Country_Split/Co/bbox_v1_Co_DRC_rec_neg') + str(num_negatives) + '.shp'

def generate_negative_bboxes(shp_file, num_negatives, output_file):
    # 读取正样本的bbox
    gdf = gpd.read_file(shp_file)

    # 提取正样本的边界框
    positive_bboxes = [row.geometry.bounds for row in gdf.itertuples()]
    # print(positive_bboxes[0][0])
    # exit(2)

    negative_bboxes = []

    # 随机生成负样本bbox，直到达到所需数量
    while len(negative_bboxes) < num_negatives:
        # 随机选择 bbox 的坐标
        min_x = random.uniform(positive_bboxes[0][0]-0.1, positive_bboxes[0][0]+0.1)  # 根据需要调整范围
        min_y = random.uniform(positive_bboxes[0][1]-0.1, positive_bboxes[0][1]+0.1)  # 根据需要调整范围
        width = random.uniform(0.01, 0.1)  # 随机宽度
        height = random.uniform(0.01, 0.1)  # 随机高度

        # 创建负样本bbox
        neg_bbox = box(min_x, min_y, min_x + width, min_y + height)

        # 检查是否与正样本重叠
        if not any(neg_bbox.intersects(box(*pb)) for pb in positive_bboxes):
            negative_bboxes.append(neg_bbox)

    # 创建新的 GeoDataFrame 存储负样本
    neg_gdf = gpd.GeoDataFrame(geometry=negative_bboxes, crs=gdf.crs)

    # 保存到新的 shp 文件
    neg_gdf.to_file(output_file)


generate_negative_bboxes(shp_file, num_negatives, output_file)
