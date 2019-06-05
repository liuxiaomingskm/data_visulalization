import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]
# "s" = 点的大小,将参数c设置成了一个u值列表，并使用参数cmap告诉pyplot使用哪个颜色进行映射
plt.scatter(x_values, y_values, c = y_values, cmap = plt.cm.Reds, edgecolors = "none", s = 40)

# 设置图表标题并给坐标轴加上标签
plt.title("Square Numbers", fontsize = 24)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Square of Values", fontsize = 14)

# 设置刻度标记的大小
plt.tick_params (axis = "both", which = "major", labelsize = 14)

# 设置每个坐标轴的取值范围
plt.axis([0, 1100, 0 , 1100000])
plt.savefig('square_plot.png', bbox_inches = "tight")

