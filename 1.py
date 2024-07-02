import matplotlib.pyplot as plt
import numpy as np
import random
from matplotlib.patches import Polygon

# 定义正方形区域的大小
region_size = 10

# 定义晶粒的数量
num_grains = 30

# 生成随机晶粒的顶点
def random_polygon(center_x, center_y, num_sides, radius_range):
    angles = np.linspace(0, 2 * np.pi, num_sides, endpoint=False)
    radii = np.random.uniform(*radius_range, size=num_sides)
    x = center_x + radii * np.cos(angles)
    y = center_y + radii * np.sin(angles)
    return np.column_stack((x, y))

# 初始化随机晶粒
grains = []
for _ in range(num_grains):
    center_x = random.uniform(0, region_size)
    center_y = random.uniform(0, region_size)
    num_sides = random.randint(3, 8)  # 随机选择3到8个边的多边形
    radius_range = (0.5, 1.5)  # 随机半径范围
    polygon = random_polygon(center_x, center_y, num_sides, radius_range)
    grains.append(polygon)

# 创建绘图
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(0, region_size)
ax.set_ylim(0, region_size)

# 绘制晶粒
for grain in grains:
    polygon = Polygon(grain, edgecolor='black', facecolor='none')
    ax.add_patch(polygon)

# 显示绘图
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Random Grains in a Square Region')
plt.grid(True)
plt.show()