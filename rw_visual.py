import matplotlib.pyplot as plt

from random_walk import RandomWalk
# 只要程序处于活动状态， 就不断的模拟随机漫步
times = 0

while True:
    # 创建一个random实例， 并将其包含的点都绘制出来
    rw = RandomWalk(5000)
    rw.fill_walk()

    # 设置绘图窗口的尺寸
    plt.figure(dpi=208, figsize=(10,6))
    point_numbers = list(range(rw.num_points))

    # c的定义如下 值越低，越是淡，每一个值对应每一个点的颜色深度，因为实例的点是从前往后放进
    # list的，所以颜色深度从浅到深正好符合1-5000的列表
    plt.plot(rw.x_values, rw.y_values,linewidth = 4)

    # 突出起点和终点
    plt.scatter(0,0, c ='green', edgecolors='none', s =100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c = 'red', edgecolors='none', s =100)

    # 隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.show()

    keep_running = input("Make another walk?(y/n):")
    if keep_running == 'n':
        break
