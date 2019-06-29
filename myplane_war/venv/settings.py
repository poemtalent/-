import os
class GameForm:
    """
    设置游戏窗口的宽和高
    """
    WIDTH = 400
    HEIGHT = 600
FPS = 30

# 定义颜色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# 获取各种文件路径
project_folder = os.path.dirname(__file__)
image_folder = os.path.join(project_folder, 'plane/images')
sound_folder = os.path.join(project_folder, 'plane/sound')