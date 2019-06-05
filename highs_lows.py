import csv
from datetime import datetime
from matplotlib import pyplot as plt

# 从文件中获取日期最高气温、最低气温
filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [],[],[]
    # 此处的row从第二行开始起，因为前面next(reader)已经读取了第一行文本
    # 阅读器对象reader从其停留的地方继续往下读取CSV文件
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], '%Y-%m-%d')
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            lows.append(low)
            dates.append(current_date)
            highs.append(high)
# 根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))

# alpha表示折线颜色的透明度 alpha=0表示完全透明，alpha=1表示完全不透明
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
# facecolor指定填充区域的颜色
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# 设置图形的格式
plt.title("Daily high and low temperatures-2014\nDeath Valley, CA", fontsize=24)
plt.xlabel('', fontsize=16)

# 绘制斜的日期标签，以免他们彼此重叠
fig.autofmt_xdate()
plt.ylabel("Temperature(F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)


plt.show()
