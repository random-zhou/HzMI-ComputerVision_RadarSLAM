# HzMI-ComputerVision_RadarSLAM
- 赫兹矩阵创新实验室视觉与雷达建模相关

![alt text](<HzMI logo.jpg>)

## 视觉数据集分类处理算法系列
YOLOv5自动标注使用说明书(点击下方)
>[Auto_label](Auto_label/Auto_labelimg.md)
- 以下皆为子功能脚本

|document                        |Code.py                                                        |info                                                                           |
|--------------------------------|---------------------------------------------------------------|---------------------------------------------------------------------------------|
|alignment.py                    |[alignment.py](Auto_label/alignment.py)                        |确保图片文件和标签文件一一对应,并删除多余文件                                          |                                               
|change_class.py                |[change_class.py](Auto_label/change_class.py )                  |指定目录下修改所有 .txt 文件中的类名                                                   |                                    
|change_name.py                  |[change_name.py](Auto_label/change_name.py)                    |更改指定目录下所有图片文件和它们对应的标签文件的名称，并在文件名前添加一个指定的类名或标志位。  |                                    
|compound.py                     |[compound.py](Auto_label/compound.py)                          |将指定输入目录下所有子目录中的文件复制到一个指定的输出路径。                               |                                    
|Disorderly_order.py             |[Disorderly_order.py](Disorderly_order.py)                     |将指定目录下的图片文件和对应的标签文件重命名为随机生成的UUID（通用唯一识别码）               |                                    
|integration.py                  |[integration.py](Auto_label/integration.py)                    |将指定源文件夹中的所有文件复制到目标文件夹。                                              |
|more_pircture.py                |[more_pircture.py](Auto_label/more_pircture.py)                |图像处理脚本-翻转,放缩,旋转,平移,剪切,调节亮度,调节对比度,调节饱和度,调节色调,高斯滤波,指数滤波,中值滤波,对数滤波 |                                 
|split.py                        |[split.py](Auto_label/split.py)                                |数据集分割                                                                              |
