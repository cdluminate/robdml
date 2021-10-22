import numpy as np
import matplotlib.pyplot as plt
import rich
c = rich.get_console()
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = 'FreeSerif'
plt.rcParams['font.size'] = 15

data = {
        'ACT': ( # [freeze]
            (27.5, 28.6, 30.6, 38.4, 46.5),
            (33.0, 17.0, 9.0, 5.0, 3.0),
            (33.9, 34.7, 31.3, 13.9, 5.8),
            ),
        'hmetrm': ( # [freeze]
            (23.1, 23.8, 27.0, 30.7, 34.3),
            (33.0, 17.0, 9.0, 5.0, 3.0),
            (38.0, 38.0, 35.1, 27.1, 18.1),
            ),
        'hmetsm': ( # [freeze]
            (35.3, 37.4, 38.4, 40.6, 44.5),
            (33.0, 17.0, 9.0, 5.0, 3.0),
            (35.7, 34.8, 29.6, 22.1, 11.6),
            ),
        'HM(S,SGA)': ( # [freeze]
            (47.5, 42.7, 38.0, 37.0, 36.5),
            (3.0, 5.0, 9.0, 17.0, 33.0),
            (11.7, 20.8, 32.4, 34.5, 35.9),
            ),
        'HM(S,-r/2)': ( # [freeze]
            (44.5, 40.0, 36.8, 35.2, 34.7),
            (3.0, 5.0, 9.0, 17.0, 33.0),
            (12.4, 24.7, 33.8, 36.8, 37.0),
            ),
        }

plt.figure(figsize=[10.8, 4.7])

ax = plt.subplot(1,2,1)
for (name, (r1, cost, ers)) in data.items():
    c.print(name, r1, cost, ers)

    if name == 'ACT':
        plt.plot(cost, ers, f'.-', color='dimgray')
    elif name == 'hmetrm':
        plt.plot(cost, ers, f'v-', color='tab:blue')
    elif name == 'hmetsm':
        plt.plot(cost, ers, f'^-', color='tab:red')
    elif name == 'HM(S,SGA)':
        plt.plot(cost, ers, f'h-', color='deeppink')
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

ax.annotate('↖ Better', xy=(0.04, 0.91), xycoords='axes fraction',
        bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="k", lw=2),
        size=17)
ax.annotate('↘ Worse', xy=(0.75, 0.06), xycoords='axes fraction',
        bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="k", lw=2),
        size=17)

ax = plt.subplot(1,2,2)
for (name, (r1, cost, ers)) in data.items():
    c.print(name, r1, cost, ers)

    if name == 'ACT':
        plt.plot(r1, ers, f'.-', color='dimgray')
    elif name == 'hmetrm':
        plt.plot(r1, ers, f'v-', color='tab:blue')
    elif name == 'hmetsm':
        plt.plot(r1, ers, f'^-', color='tab:red')
    elif name == 'HM(S,SGA)':
        plt.plot(r1, ers, f'h-', color='deeppink')
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

ax.annotate('↖ Better', xy=(0.04, 0.91), xycoords='axes fraction',
        bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="k", lw=2),
        size=17)
ax.annotate('↘ Worse', xy=(0.75, 0.06), xycoords='axes fraction',
        bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="k", lw=2),
        size=17)

plt.tight_layout(pad=1.0)
#plt.show()
plt.savefig('introplot.svg')
