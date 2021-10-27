import numpy as np
import matplotlib.pyplot as plt
import rich
import argparse
c = rich.get_console()
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = 'FreeSerif'
plt.rcParams['font.size'] = 15
plt.rcParams['text.usetex'] = False
plt.rcParams['mathtext.fallback'] = 'cm'

data_cub = {
    'ACT[R]': (
        (30.6, 27.5), (9.0, 33.0), (31.3, 33.9) ),
    'HM[S,SGA]': (
        (38.0, 36.5), (9.0, 33.0), (32.4, 35.9) ),
    'HM[S,SGA]ICS': (
        (37.2, 37.2), (9.0, 33.0), (33.5, 33.5) ),
}
data_cars = {
    'ACT[R]': (
        (46.8, 43.4), (9.0, 33.0), (39.8, 38.6) ),
    'HM[S,SGA]': (
        (63.2, 62.3), (9.0, 9.0), (42.4, 44.9)),
}
data_sop = {
    'ACT[R]': (
        (45.1, 47.5), (9.0, 33.0), (50.3, 50.8) ),
    'HM[S,SGA]': (
        (49.0, 49.0), (9.0, 33.0), (61.7, 61.7) ),
}

styledict = {
    'ACT[R]': {
        'marker': '.',
        'linestyle': ':',
        'color': 'tab:cyan',
        'linewidth': 2.0,
    },
    'ACT[S]': {
        'marker': '.',
        'linestyle': ':',
        'color': 'tab:orange',
        'linewidth': 2.0,
    },
    'HM[R,M]': {
        'marker': 'v',
        'linestyle': '-.',
        'color': 'tab:blue',
        'linewidth': 2.0,
    },
    'HM[S,M]': {
        'marker': '^',
        'linestyle': '-.',
        'color': 'tab:red',
        'linewidth': 2.0,
    },
    'HM[S,SGA]': {
        'marker': 'h',
        'linestyle': '-',
        'color': 'darkviolet',
        'linewidth': 2.0,
    },
    'HM[S,-r/2]': {
        'marker': '+',
        'linestyle': '-.',
        'color': 'tab:gray',
        'linewidth': 2.0,
    },
    'HM[S,SGA]ICS': {
        'marker': 'o',
        'linestyle': '-.',
        'color': 'crimson',
        'linewidth': 2.0,
    },
}

plt.figure(figsize=[12, 7])

# 1 

ax = plt.subplot(2,3,1)
for (name, (r1, cost, ers)) in data_cub.items():
    if name in styledict:
        plt.plot(cost, ers, **(styledict[name]))
plt.xlabel('Training Cost')
plt.ylabel('Robustness (ERS)')
plt.xscale('log', base=2)
ax.legend(['ACT[$\mathcal{R}$]',
        'HM[$\mathcal{S},g_\mathsf{SGA}$]'],
        labelcolor='linecolor',
        )
plt.title('CUB Dataset')

# 4

ax = plt.subplot(2,3,4)
for (name, (r1, cost, ers)) in data_cub.items():
    if name in styledict:
        plt.plot(r1, ers, **(styledict[name]))
plt.xlabel('Recall@1')
plt.ylabel('Robustness (ERS)')
plt.gca().invert_xaxis()
ax.legend(['ACT[$\mathcal{R}$]',
        'HM[$\mathcal{S},g_\mathsf{SGA}$]'],
        labelcolor='linecolor',
        )
plt.title('CUB Dataset')

# 2

ax = plt.subplot(2,3,2)
for (name, (r1, cost, ers)) in data_cars.items():
    if name in styledict:
        plt.plot(cost, ers, **(styledict[name]))
plt.xlabel('Training Cost')
plt.ylabel('Robustness (ERS)')
plt.xscale('log', base=2)
ax.legend(['ACT[$\mathcal{R}$]',
        'HM[$\mathcal{S},g_\mathsf{SGA}$]'],
        labelcolor='linecolor',
        )
plt.title('CARS Dataset')

# 5

ax = plt.subplot(2,3,5)
for (name, (r1, cost, ers)) in data_cars.items():
    if name in styledict:
        plt.plot(r1, ers, **(styledict[name]))
plt.xlabel('Recall@1')
plt.ylabel('Robustness (ERS)')
plt.gca().invert_xaxis()
ax.legend(['ACT[$\mathcal{R}$]',
        'HM[$\mathcal{S},g_\mathsf{SGA}$]'],
        labelcolor='linecolor',
        )
plt.title('CARS Dataset')

# 3

ax = plt.subplot(2,3,3)
for (name, (r1, cost, ers)) in data_sop.items():
    if name in styledict:
        plt.plot(cost, ers, **(styledict[name]))
plt.xlabel('Training Cost')
plt.ylabel('Robustness (ERS)')
plt.xscale('log', base=2)
ax.legend(['ACT[$\mathcal{R}$]',
        'HM[$\mathcal{S},g_\mathsf{SGA}$]'],
        labelcolor='linecolor',
        )
plt.title('SOP Dataset')

# 6

ax = plt.subplot(2,3,6)
for (name, (r1, cost, ers)) in data_sop.items():
    if name in styledict:
        plt.plot(r1, ers, **(styledict[name]))
plt.xlabel('Recall@1')
plt.ylabel('Robustness (ERS)')
plt.gca().invert_xaxis()
ax.legend(['ACT[$\mathcal{R}$]',
        'HM[$\mathcal{S},g_\mathsf{SGA}$]'],
        labelcolor='linecolor',
        )
plt.title('SOP Dataset')

# end

plt.tight_layout(pad=1.0)
plt.savefig('sotaplot.svg')
