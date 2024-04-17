import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import numpy as np

# 分类报告数据
report_data = {
    "precision": [1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00,
                  1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 0.50, 1.00, 1.00,
                  1.00, 1.00, 1.00, 1.00, 0.00, 1.00, 1.00, 1.00, 0.00, 1.00,
                  1.00, 1.00, 1.00, 1.00, 1.00, 0.50, 1.00],
    "recall": [0.50, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00,
               1.00, 1.00, 1.00, 1.00, 1.00, 0.67, 1.00, 1.00, 1.00, 1.00,
               1.00, 1.00, 1.00, 1.00, 0.00, 1.00, 1.00, 1.00, 0.00, 1.00,
               1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00],
    "f1-score": [0.67, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00,
                 1.00, 1.00, 1.00, 1.00, 1.00, 0.80, 1.00, 0.67, 1.00, 1.00,
                 1.00, 1.00, 1.00, 1.00, 0.00, 1.00, 1.00, 1.00, 0.00, 1.00,
                 1.00, 1.00, 1.00, 1.00, 1.00, 0.67, 1.00],
    "support": [2, 1, 3, 1, 1, 2, 2, 4, 4, 3, 1, 2, 4, 3, 3, 6, 2, 2, 3, 2,
                1, 3, 2, 3, 0, 3, 1, 1, 1, 3, 2, 1, 1, 1, 4, 2, 2, 1, 1]
}

# 创建表格
fig, ax = plt.subplots(figsize=(10, 8))
columns = ('precision', 'recall', 'f1-score', 'support')
rows = [str(i) for i in range(1, 38)]

# 创建颜色映射
cmap_blue = LinearSegmentedColormap.from_list('blue_cmap', [(0.85, 0.85, 1), (0.4, 0.4, 1)])  # 浅蓝到深蓝

# 添加表格内容
cell_text = []
for row in range(len(rows)):
    cell_text.append([report_data[column][row] for column in columns])

# 添加表格
table = ax.table(cellText=cell_text, rowLabels=rows, colLabels=columns, loc='center')

# 设置单元格颜色
for i in range(len(rows)):
    for j in range(len(columns)):
        value = report_data[columns[j]][i]
        if columns[j] != 'support':
            table[(i+1, j)].set_facecolor(cmap_blue(value))

# 设置表格样式
# table.auto_set_column_width(col=list(range(len(columns))))  # 自动调整列宽
table.auto_set_column_width(6)  # 自动调整列宽
table.set_fontsize(10)
# 设置字体居中
for key, cell in table.get_celld().items():
    cell.set_text_props(fontproperties='Arial', fontsize=12, ha='center', va='center')


# 隐藏坐标轴
ax.axis('off')

plt.show()
