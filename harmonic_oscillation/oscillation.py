import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 定义物理参数
m = 1.0  # 小球的质量，单位：kg
k = 16.0  # 弹簧的劲度系数，单位：N/m
c = 20 # 阻尼系数，单位：Ns/m
omega_0 = np.sqrt(k/m)  # 未阻尼的自然频率，单位：rad/s
zeta = c / (2*np.sqrt(m*k))  # 阻尼比

# 初始条件
x0 = 1.0  # 初始位移，单位：m
v0 = 0.0  # 初始速度，单位：m/s
x = x0
v = v0

# 时间参数
dt = 0.01  # 时间步长，单位：s
t_max = 5  # 总时间，单位：s
t_values = np.arange(0, t_max, dt)
x_values = []  # 用于存储小球位置的数组
v_values = []  # velocity
a_values = []  # acceleration

# 初始化图形和子图
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6, 6))
ax1.set_xlim(-1, 1)
ax1.set_ylim(-1.5, 1.5)
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_title('Spring-mass')
line, = ax1.plot([], [], 'bo')  # 小球
spring, = ax1.plot([], [], 'r-')  # 弹簧

# 初始化第二个子图
ax2.set_xlim(0, t_max)
ax2.set_ylim(-1.5, 1.5)
ax2.set_xlabel('Time (s)')
ax2.set_ylabel('Y Position')
x_line, = ax2.plot([], [], 'b-')
# x_line.set_label('x')
# v_line, = ax2.plot([], [], 'g--')
# v_line.set_label('v')
# a_line, = ax2.plot([], [], 'r-.')
# a_line.set_label('a')
# ax2.legend()
ax2.grid(True)

# 初始化动画
def init():
    line.set_data([], [])
    spring.set_data([], [])
    x_line.set_data([], [])
    return line, spring, x_line

# 动画更新函数
def animate(i):
    global x, v, x_values
    # 使用阻尼振动的运动方程更新位置和速度
    a = -k*x - c*v
    v = v + a*dt
    x = x + v*dt
    x_values.append(x)  # 记录小球位置
    v_values.append(v/omega_0)
    a_values.append(a/omega_0**2)
    
    # 更新小球的位置
    line.set_data([0], [x])
    
    # 更新弹簧的位置
    spring.set_data([0, 0], [0, x])
    
    # 更新第二个子图
    x_line.set_data(t_values[:i+1], x_values)
    # v_line.set_data(t_values[:i+1], v_values)
    # a_line.set_data(t_values[:i+1], a_values)
    ax2.set_ylim(-1.5, 1.5)
    
    # return line, spring, x_line, v_line, a_line
    return line, spring, x_line

# 创建动画
ani = FuncAnimation(fig, animate, init_func=init, frames=len(t_values), interval=dt*1000, blit=True)

# 存储动画
ani.save('./harmonic_oscillation/overdamped_harmonic_oscillation.mp4', writer='ffmpeg', fps=120)

# 显示动画
plt.show()