import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

scores = [88, 92, 76, 61, 59, 95, 83, 70, 45, 100, 120]
total = 0
for score in scores:
    total += score  # 已替换为标准的4个英文空格

mean = total / len(scores)

# 计算方差和
variance_sum = 0
for score in scores:
    variance_sum += (score - mean) ** 2 

# 计算方差
variance = variance_sum / len(scores)

# 优化体验：先打印计算结果，防止被 plt.show() 的画图弹窗阻塞
print("mean:", mean)
print("variance:", variance)
print("max:", max(scores))
print("min:", min(scores))

# 绘制直方图
plt.hist(scores, bins=5, edgecolor='black')
plt.title("Scores")
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.grid()
output_path = r"D:\AAAA_airoadmap\week_01\scores_histogram.png"
plt.savefig(output_path)
print("saved:", output_path)
