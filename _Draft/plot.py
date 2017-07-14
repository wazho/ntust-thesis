import numpy as np
import matplotlib.pyplot as plt

f, ax = plt.subplots(1, figsize = (10, 5), dpi = 120)

x = np.arange(0., 10., 0.02)

# (x/x.max)**(1/c)
line1, = plt.plot(x, (x/10),          '#FC533C', label=r'$y_{1} =  \frac{x}{x \cdot max}$',                linewidth=2.0)
line2, = plt.plot(x, (x/10)**(1.0/2), '#2E9ECB', label=r'$y_{2} = (\frac{x}{x \cdot max}) ^ \frac{1}{2}$', linewidth=2.0)
line3, = plt.plot(x, (x/10)**(1.0/3), '#DFAC5A', label=r'$y_{3} = (\frac{x}{x \cdot max}) ^ \frac{1}{3}$', linewidth=2.0)
line4, = plt.plot(x, (x/10)**(1.0/4), '#1CA429', label=r'$y_{4} = (\frac{x}{x \cdot max}) ^ \frac{1}{4}$', linewidth=2.0)

# x = 1, x = 2, x = 3 ...
vline1, = plt.plot([1, 1], [0, 1], '#666666', linewidth=1.25, dashes=[4, 3], alpha=0.75)
vline2, = plt.plot([2, 2], [0, 1], '#666666', linewidth=1.25, dashes=[4, 3], alpha=0.75)
vline3, = plt.plot([3, 3], [0, 1], '#666666', linewidth=1.25, dashes=[4, 3], alpha=0.75)
vline4, = plt.plot([4, 4], [0, 1], '#666666', linewidth=1.25, dashes=[4, 3], alpha=0.75)


line1a, = plt.plot([1, 2], [0.10000000000, 0.10000000000], '#FC533C', linewidth=1.25, alpha=0.75)
line1b, = plt.plot([2, 2], [0.10000000000, 0.20000000000], '#FC533C', linewidth=1.25, alpha=0.75)
plt.text(2.05, 0.16, '+0.1000', fontsize=10, weight='bold', color='#FC533C')
line2a, = plt.plot([1, 2], [0.31622776601, 0.31622776601], '#2E9ECB', linewidth=1.25, alpha=0.75)
line2b, = plt.plot([2, 2], [0.31622776601, 0.44721359550], '#2E9ECB', linewidth=1.25, alpha=0.75)
plt.text(2.05, 0.40, '+0.1310', fontsize=10, weight='bold', color='#2E9ECB')
line3a, = plt.plot([1, 2], [0.46415888336, 0.46415888336], '#DFAC5A', linewidth=1.25, alpha=0.75)
line3b, = plt.plot([2, 2], [0.46415888336, 0.58480354764], '#DFAC5A', linewidth=1.25, alpha=0.75)
plt.text(2.05, 0.54, '+0.1206', fontsize=10, weight='bold', color='#DFAC5A')
line4a, = plt.plot([1, 2], [0.56234132519, 0.56234132519], '#1CA429', linewidth=1.25, alpha=0.75)
line4b, = plt.plot([2, 2], [0.56234132519, 0.66874030497], '#1CA429', linewidth=1.25, alpha=0.75)
plt.text(2.05, 0.63, '+0.1064', fontsize=10, weight='bold', color='#1CA429')


line1c, = plt.plot([3, 4], [0.30000000000, 0.30000000000], '#FC533C', linewidth=1.25, alpha=0.75)
line1d, = plt.plot([4, 4], [0.30000000000, 0.40000000000], '#FC533C', linewidth=1.25, alpha=0.75)
plt.text(4.05, 0.36, '+0.1000', fontsize=10, weight='bold', color='#FC533C')
line2c, = plt.plot([3, 4], [0.54772255750, 0.54772255750], '#2E9ECB', linewidth=1.25, alpha=0.75)
line2d, = plt.plot([4, 4], [0.54772255750, 0.63245553203], '#2E9ECB', linewidth=1.25, alpha=0.75)
plt.text(4.05, 0.59, '+0.0847', fontsize=10, weight='bold', color='#2E9ECB')
line3c, = plt.plot([3, 4], [0.66943295008, 0.66943295008], '#DFAC5A', linewidth=1.25, alpha=0.75)
line3d, = plt.plot([4, 4], [0.66943295008, 0.73680629972], '#DFAC5A', linewidth=1.25, alpha=0.75)
plt.text(4.05, 0.70, '+0.0674', fontsize=10, weight='bold', color='#DFAC5A')
line4c, = plt.plot([3, 4], [0.74008280449, 0.74008280449], '#1CA429', linewidth=1.25, alpha=0.75)
line4d, = plt.plot([4, 4], [0.74008280449, 0.79527072876], '#1CA429', linewidth=1.25, alpha=0.75)
plt.text(4.05, 0.76, '+0.0552', fontsize=10, weight='bold', color='#1CA429')


# ticks
plt.xticks([0, 1, 2, 3, 4, 10], ['0', '1', '2', '3', '4', r'$x \cdot max$'], fontsize=14)
plt.yticks(np.arange(0, 1.1, 0.1), fontsize=14)

ax.set_xlim(xmin=0)
ax.set_ylim(ymin=0)

plt.xlabel('original fitness score', fontsize=15)
plt.ylabel('normalized fitness score', fontsize=15)

plt.legend(handles=[line1, line2, line3, line4], fontsize=18, loc=4)

plt.show()