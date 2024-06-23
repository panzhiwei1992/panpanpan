import matplotlib.pyplot as plt
import pandas as pd

# 创建一个样本数据集，包含1990年至2023年的美国平均房价
years = list(range(1990, 2024))

# 样本数据：假设一个一般的上升趋势，带有一些波动
house_prices = [
    122000, 125000, 128000, 130000, 133000, 135000, 138000, 142000, 145000, 148000,
    153000, 158000, 163000, 168000, 173000, 180000, 187000, 195000, 203000, 210000,
    217000, 225000, 233000, 240000, 247000, 255000, 260000, 265000, 270000, 275000,
    280000, 285000, 290000, 295000, 300000, 305000, 310000, 315000
]

# 确保两个数组的长度一致
min_length = min(len(years), len(house_prices))
years = years[:min_length]
house_prices = house_prices[:min_length]

# 创建一个数据框
data = pd.DataFrame({
    '年份': years,
    '平均房价': house_prices
})

# 绘制数据
plt.figure(figsize=(12, 6))
plt.plot(data['年份'], data['平均房价'], marker='o', linestyle='-', color='b')
plt.title('1990-2023年美国平均房价')
plt.xlabel('年份')
plt.ylabel('平均房价（美元）')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

# 显示图表
plt.show()
