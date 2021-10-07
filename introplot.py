import numpy as np
import matplotlib.pyplot as plt
import rich
c = rich.get_console()

plt.rcParams['font.family'] = 'serif'
#plt.rcParams['font.serif'] = 'Times New Roman; Noto Sans'
plt.rcParams['font.serif'] = 'FreeSerif'
#plt.rcParams['font.serif'] = 'Linux Libertine O'
plt.rcParams['font.size'] = 14

data = {
        #'N/A': (53.9, 1.0, 3.8),
        #'EST': (8.5, 33.0, 5.3),
        'ACT': (
            (27.5, 28.6, 33.3, 38.4, 46.5),
            (33.0, 17.0, 8.0, 5.0, 3.0),
            (33.9, 34.7, 27.3, 13.9, 5.8),
            ),
        #'amdsemi': (
        #    (25.6, 25.1, 28.0),
        #    (33.0, 17.0, 8.0),
        #    (38.0, 36.6, 33.5),
        #    ),
        #'amdsemi+aap0': (26.2, 9.0, 40.0),
        #'hml2rm': (
        #    (27.4, 29.0),
        #    (9.0, 5.0),
        #    (32.9, 30.8),
        #    ),
        #'hml2rmi': (25.2, 9.0, 39.8),
        'hmetrm': (
            (27.1, 28.3, 34.9, 39.2),
            (17.0, 9.0, 5.0, 3.0),
            (40.0, 37.2, 25.6, 14.0),
            ),
        }

plt.figure(figsize=[10.8, 4.8])

ax = plt.subplot(1,2,1)
for (name, (r1, cost, ers)) in data.items():
    c.print(name, r1, cost, ers)

    color = 'k'
    if name == 'ACT':
        color = 'm'
    plt.plot(cost, ers, f'-{color}o')
    if isinstance(cost, float):
        plt.annotate(name, xy=(cost, ers))
    elif isinstance(cost, tuple):
        plt.annotate(name, xy=(cost[0], ers[0]))
plt.xlabel('Training Cost')
plt.ylabel('Robustness (ERS)')
plt.xscale('log', base=2)
#plt.axis('equal')
#plt.axis('square')

ax.annotate('↖ Better', xy=(0.04, 0.92), xycoords='axes fraction',
        bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="k", lw=2),
        size=14)
ax.annotate('↘ Worse', xy=(0.77, 0.06), xycoords='axes fraction',
        bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="k", lw=2),
        size=14)

#plt.subplot(2,2,2)
#for (name, (r1, cost, ers)) in data.items():
#    c.print(name, r1, cost, ers)
#
#    color = 'k'
#    if name == 'EST':
#        color = 'b'
#    if name == 'ACT':
#        color = 'r'
#    plt.plot(cost, r1, f'-{color}o')
#    if isinstance(cost, float):
#        plt.annotate(name, xy=(cost, r1))
#    elif isinstance(cost, tuple):
#        plt.annotate(name, xy=(cost[0], r1[0]))
#plt.xlabel('Training Cost')
#plt.ylabel('Recall@1 (R@1)')
#plt.xscale('log', base=2)


ax = plt.subplot(1,2,2)
for (name, (r1, cost, ers)) in data.items():
    c.print(name, r1, cost, ers)

    color = 'k'
    if name == 'ACT':
        color = 'm'
    plt.plot(r1, ers, f'-{color}o')
    if isinstance(ers, float):
        plt.annotate(name, xy=(r1, ers))
    elif isinstance(ers, tuple):
        plt.annotate(name, xy=(r1[0], ers[0]))
plt.ylabel('Robustness (ERS)')
plt.xlabel('Recall@1')
plt.gca().invert_xaxis()
#plt.axis('equal')
#plt.axis('square')

ax.annotate('↖ Better', xy=(0.04, 0.92), xycoords='axes fraction',
        bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="k", lw=2),
        size=14)
ax.annotate('↘ Worse', xy=(0.77, 0.06), xycoords='axes fraction',
        bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="k", lw=2),
        size=14)

#plt.tight_layout()
#plt.show()
plt.savefig('introplot.svg')
