import json  # 导入json模块，用于读写JSON文件
import os  # 导入os模块，用于处理文件和目录
import argparse  # 导入argparse模块，用于解析命令行参数
from tqdm import tqdm  # 导入tqdm模块，用于显示进度条

# 定义一个函数，用于将JSON格式的标注文件转换为TXT格式
def convert_label_json(json_dir, save_dir, classes):
    # 获取指定目录下的所有文件
    json_paths = os.listdir(json_dir)
    # 将传入的classes字符串以逗号分隔，转换为列表
    classes = classes.split(',')

    # 遍历所有文件
    for json_path in tqdm(json_paths):
        # 构建完整的文件路径
        path = os.path.join(json_dir, json_path)
        # 打开并读取JSON文件
        with open(path,'r') as load_f:
            json_dict = json.load(load_f)
        # 从JSON文件中获取图片的高度和宽度
        h, w = json_dict['imageHeight'], json_dict['imageWidth']

        # 构建输出TXT文件的路径
        txt_path = os.path.join(save_dir, json_path.replace('json', 'txt'))
        # 打开TXT文件准备写入
        txt_file = open(txt_path,'w')

        # 遍历JSON文件中的所有形状（标注）
        for shape_dict in json_dict['shapes']:
            # 获取形状的标签
            label = shape_dict['label']
            # 获取标签在classes列表中的索引
            label_index = classes.index(label)
            # 获取形状的点
            points = shape_dict['points']

            # 初始化一个列表，用于存储归一化的点坐标
            points_nor_list = []

            # 遍历形状的所有点，将坐标归一化
            for point in points:
                points_nor_list.append(point[0]/ w)  # 归一化x坐标
                points_nor_list.append(point[1]/ h)  # 归一化y坐标
            # 将归一化的点坐标转换为字符串列表
            points_nor_list = list(map(lambda x: str(x), points_nor_list))
            # 将点坐标列表转换为字符串，点之间用空格分隔
            points_nor_str = ' '.join(points_nor_list)

            # 构建标签行字符串
            label_str = str(label_index) + ' ' + points_nor_str + '\n'
            # 将标签行写入TXT文件
            txt_file.writelines(label_str)

# 主函数入口
if __name__ == "__main__":
    # 创建一个ArgumentParser对象，用于解析命令行参数
    parser = argparse.ArgumentParser(description='json convert to txt params')
    # 添加参数'--json-dir'，指定JSON文件的目录
    parser.add_argument('--json-dir', type=str, default='json_dir', help='json path dir')
    # 添加参数'--save-dir'，指定保存TXT文件的目录
    parser.add_argument('--save-dir', type=str, default='txt_dir', help='txt save dir')
    # 添加参数'--classes'，指定类别列表
    parser.add_argument('--classes', type=str, default='A,B,C.....', help='classes')
    # 解析命令行参数
    args = parser.parse_args()
    # 获取命令行参数指定的值
    json_dir = args.json_dir
    save_dir = args.save_dir
    classes = args.classes
    # 调用convert_label_json函数进行转换
    convert_label_json(json_dir, save_dir, classes)