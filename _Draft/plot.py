import numpy as np
import matplotlib.pyplot as plt

f, ax = plt.subplots(1, figsize = (10, 5), dpi = 120)

t = np.arange(0., 10., 0.02)
color = ['r-','g-','b-','y-']

line1, = plt.plot(t, (t/10),          '#FC533C', label=r'$y =  \frac{x}{x \cdot max}$',                 linewidth=2.0)
line2, = plt.plot(t, (t/10)**(1.0/2), '#2E9ECB', label=r'$y = (\frac{x}{x \cdot max}) ^ \frac{1}{2}$', linewidth=2.0)
line3, = plt.plot(t, (t/10)**(1.0/3), '#DFAC5A', label=r'$y = (\frac{x}{x \cdot max}) ^ \frac{1}{3}$', linewidth=2.0)
line4, = plt.plot(t, (t/10)**(1.0/4), '#1CA429', label=r'$y = (\frac{x}{x \cdot max}) ^ \frac{1}{4}$', linewidth=2.0)

plt.xticks(np.arange(min(t), max(t)+1, 10.0), ['0', r'$x \cdot max$'], fontsize=14)
plt.yticks(np.arange(0, 1.1, 0.1), fontsize=14)

ax.set_xlim(xmin=0)
ax.set_ylim(ymin=0)

plt.xlabel('original fitness score', fontsize=15)
plt.ylabel('normalized fitness score', fontsize=15)

plt.legend(handles=[line1, line2, line3, line4], fontsize=18, loc=4)

plt.show()