import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib as npl
from datetime import datetime
import seaborn as sns
from matplotlib.colors import Normalize
import matplotlib.cm as cm

# -------------------------------------------1 pic--------------------------------------------

x1 = [1, 5, 10, 15, 20]
y1 = [1, 7, 4, 5, 11]

x2 = [1, 5, 10, 15, 20]
y2 = [4, 3, 1, 8, 12]

plt.figure(figsize=(8, 5))

plt.plot(x1, y1, marker="o", linestyle="-", label="line 1", color="red")
plt.plot(x2, y2, marker="o", linestyle="-.", label="line 2", color="green")

plt.legend()

plt.show()

# --------------------------------2 pic-----------------------------------


# верхний
x1 = [1, 2, 3, 4, 5]
y1 = [1, 7, 6, 3, 5]

# нижний левый
x2 = [1, 2, 3, 4, 5]
y2 = [9, 4, 2, 4, 9]

# нижний правый
x3 = [1, 2, 3, 4, 5]
y3 = [-7, -4, 2, -4, -7]

fig = plt.figure(figsize=(12, 4))

ax1 = plt.subplot2grid((2, 2), (0, 0), colspan=2)
ax2 = plt.subplot2grid((2, 2), (1, 0), colspan=1)
ax3 = plt.subplot2grid((2, 2), (1, 1), colspan=1)

ax1.plot(x1, y1)
ax2.plot(x2, y2)
ax3.plot(x3, y3)

plt.show()


# ------------------------3 pic--------------------------------------------------


x = np.arange(-5, 6, 1)
y = x**2
fig, ax = plt.subplots()

ax.plot(x, y)

arrow_x = 0
arrow_y = 0

ax.annotate(
    "min",
    xy=(arrow_x, arrow_y),
    xytext=(arrow_x, arrow_y + 10),
    arrowprops=dict(
        facecolor="green",
        edgecolor="black",
        width=5,
        headwidth=10,
    ),
    ha="right",
)

plt.show()


# ----------------------------4 pic----------------------------------------


data = np.random.rand(7, 7) * 10
norm = Normalize(vmin=0, vmax=10)

fig, ax = plt.subplots()
im = ax.imshow(data, cmap="viridis", origin="lower", extent=[0, 7, 0, 7], norm=norm)
cbar = fig.colorbar(im)

plt.show()


# -----------------------------5 pic---------------------------------------------------


x = np.linspace(0, 5, 500)
y = np.cos(np.pi * x)

fig, ax = plt.subplots()
ax.plot(x, y, color="red")
for i in range(5):
    ax.fill_between(x, y, where=((x >= i) & (x <= i + 1)), color="blue")

plt.show()


# ------------------------------------------6 pic--------------------------------------------------------

x = np.linspace(0, 5, 500)
y = np.cos(np.pi * x)

fig, ax = plt.subplots()
y_masked = np.ma.masked_where(y < -0.5, y)

ax.plot(x, y_masked, color="blue")
ax.set_ylim(-1.1, 1.1)

plt.show()


# --------------------------------------------7 pic----------------------------------------------------------

x = [0, 1, 2, 3, 4, 5, 6]
y = [0, 1, 2, 3, 4, 5, 6]

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

axes[0].step(x, y, where="pre", marker="o", color='green')
axes[0].set_xticks(x)
axes[0].set_yticks(y)

axes[1].step(x, y, where="post", marker="o", color='green')
axes[1].set_xticks(x)
axes[1].set_yticks(y)

axes[2].step(x, y, where="mid", marker="o", color='green')
axes[2].set_xticks(x)
axes[2].set_yticks(y)

for ax in axes:
    ax.grid(True)

plt.show()



#----------------------------------------------------8 pic---------------------------------------------------------------------------


x = np.linspace(0, 15, 10)
y_blue = np.zeros_like(x)  
y_orange = np.zeros_like(x)
y_green = np.zeros_like(x) 

y_blue[x <= 10] = 5 * np.sin(np.pi * x[x <= 10] / 10) 
y_orange[x <= 10] = 15 * np.sin(np.pi * x[x <= 10] / 10)
y_green[x <= 15] = 25 * np.sin(np.pi * x[x <= 15] / 15)

fig, ax = plt.subplots()

ax.fill_between(x, 0, y_green, color='green', label='y3') 
ax.fill_between(x, 0, y_orange, color='orange', label='y2')
ax.fill_between(x, 0, y_blue, color='blue', label='y1') 

ax.set_xlim(0, 10)
ax.set_ylim(0, 26)
ax.legend()

plt.show()


#-------------------------------------------------9 pic-----------------------------------------------------------------------------------


labels = ['Ford', 'Toyota', 'BMW', 'AUDI', 'Jaguar']
sizes = [20, 10, 30, 15, 25]
colors = ['blue', 'orange', 'green', 'red', 'purple']
explode = (0, 0, 0.1, 0, 0)

fig, ax = plt.subplots()

ax.pie(
    sizes,
    explode=explode,
    labels=labels,
    colors=colors,
)

ax.axis('equal')

plt.show()


#----------------------------------10 pic---------------------------------------------------


labels = ['Ford', 'Toyota', 'BMW', 'AUDI', 'Jaguar']
sizes = [20, 10, 30, 15, 25]
colors = ['blue', 'orange', 'green', 'red', 'purple']

fig, ax = plt.subplots()

ax.pie(
    sizes,
    labels=labels,
    colors=colors,
)

centre_circle = plt.Circle((0, 0), 0.5, fc='white')
fig.gca().add_artist(centre_circle)

ax.axis('equal')
plt.show()