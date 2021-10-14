import numpy as np
import matplotlib.pyplot as plt
import rich
c = rich.get_console()
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = 'FreeSerif'
plt.rcParams['font.size'] = 14

data = {
        'ACT': (
            (27.5, 28.6, 30.6, 38.4, 46.5),
            (33.0, 17.0, 9.0, 5.0, 3.0),
            (33.9, 34.7, 31.3, 13.9, 5.8),
            ),
        #'amdsemi+aap0': (26.2, 9.0, 40.0),
        #'hml2rmi': (25.2, 9.0, 39.8),
        'hmetrm(bug)': (
            (27.0, 27.1, 28.3, 34.9, 39.2),
            (33.0, 17.0, 9.0, 5.0, 3.0),
            (40.3, 40.0, 37.2, 25.6, 14.0),
            ),
        'hmetrm': (
            (23.1, 23.8, 27.0, 30.7, 34.3),
            (33.0, 17.0, 9.0, 5.0, 3.0),
            (38.0, 38.0, 35.1, 27.1, 18.1),
            ),
        'hmetsm': (
            (38.4, 40.6, 44.5),
            (9.0, 5.0, 3.0),
            (29.6, 22.1, 11.6),
            ),
        'hmix': (
            (37.8, 42.7),
            (5.0, 3.0),
            (21.7, 12.5),
            ),
        }

plt.figure(figsize=[10.8, 4.8])

ax = plt.subplot(1,2,1)
for (name, (r1, cost, ers)) in data.items():
    c.print(name, r1, cost, ers)

    if name == 'ACT':
        plt.plot(cost, ers, f'-o', color='dimgray')
    elif name == 'hmetrm':
        plt.plot(cost, ers, f'-o', color='tab:blue')
    elif name == 'hmetsm':
        plt.plot(cost, ers, f'-o', color='tab:red')
    elif name == 'hmix':
        plt.plot(cost, ers, f'-o', color='deeppink')
    else:
        plt.plot(cost, ers, f'-o', color='k')
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

ax = plt.subplot(1,2,2)
for (name, (r1, cost, ers)) in data.items():
    c.print(name, r1, cost, ers)

    if name == 'ACT':
        plt.plot(r1, ers, f'-o', color='dimgray')
    elif name == 'hmetrm':
        plt.plot(r1, ers, f'-o', color='tab:blue')
    elif name == 'hmetsm':
        plt.plot(r1, ers, f'-o', color='tab:red')
    elif name == 'hmix':
        plt.plot(r1, ers, f'-o', color='deeppink')
    else:
        plt.plot(r1, ers, f'-o', color='k')
    if isinstance(ers, float):
        plt.annotate(name, xy=(r1, ers))
    elif isinstance(ers, tuple):
        plt.annotate(name, xy=(r1[0], ers[0]))
plt.xlabel('Recall@1')
plt.ylabel('Robustness (ERS)')
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
