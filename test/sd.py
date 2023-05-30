import matplotlib.pyplot as plt

# 设置字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 绘制时序图
fig, ax = plt.subplots()

# 设置标题和坐标轴标签
ax.set(title='小餐厅库存管理时序图', xlabel='时间', ylabel='动作')

# 添加箭头和文本
ax.arrow(0, 0, 0, 1, head_width=0.05, head_length=0.1, length_includes_head=True)
ax.text(0, 0.9, '点击购买商品')

ax.arrow(1, 1, 0, 1, head_width=0.05, head_length=0.1, length_includes_head=True)
ax.text(1, 1.9, '发送更新库存请求')

ax.arrow(2, 2, 0, 1, head_width=0.05, head_length=0.1, length_includes_head=True)
ax.text(2, 2.9, '扫描商品条码')

ax.arrow(3, 3, 0, 1, head_width=0.05, head_length=0.1, length_includes_head=True)
ax.text(3, 3.9, '发送更新库存请求')

ax.arrow(4, 4, 0, 1, head_width=0.05, head_length=0.1, length_includes_head=True)
ax.text(4, 4.9, '更新库存信息')

# 显示图形
plt.show()
