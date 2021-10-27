import numpy as np
import matplotlib.pyplot as plt
import rich
import argparse
c = rich.get_console()
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = 'FreeSerif'
plt.rcParams['font.size'] = 15

ag = argparse.ArgumentParser()
ag.add_argument('-w', '--whichone', type=int, required=True)
ag = ag.parse_args()

whichone = ag.whichone

ACT_R = {
    'ACT[R]': ( # [freeze]
        (27.5, 28.6, 30.6, 38.4, 46.5),
        (33.0, 17.0, 9.0, 5.0, 3.0),
        (33.9, 34.7, 31.3, 13.9, 5.8),
        ),
}
ACT_S = {
    'ACT[S]': ( # [freeze]
        (53.0, 49.3, 42.8, 40.5, 39.4),
        (3.0, 5.0, 9.0, 17.0, 33.0),
        (5.1, 7.1, 18.7, 23.7, 24.2),
        ),
}
HM_RM = {
    'HM[R,M]': ( # [freeze]
        (23.1, 23.8, 27.0, 30.7, 34.3),
        (33.0, 17.0, 9.0, 5.0, 3.0),
        (38.0, 38.0, 35.1, 27.1, 18.1),
        ),
}
HM_SM = {
    'HM[S,M]': ( # [freeze]
        (35.3, 37.4, 38.4, 40.6, 44.5),
        (33.0, 17.0, 9.0, 5.0, 3.0),
        (35.7, 34.8, 29.6, 22.1, 11.6),
        ),
}

if whichone == 0:
    # all
    data = {
        **ACT_R,
        **ACT_S,
        **HM_RM,
        **HM_SM,
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
elif whichone == 1:
    # fig 1
    data = {
        **ACT_R,
        **ACT_S,
        'HM[S,SGA]': ( # [freeze]
            (47.5, 42.7, 38.0, 37.0, 36.5),
            (3.0, 5.0, 9.0, 17.0, 33.0),
            (11.7, 20.8, 32.4, 34.5, 35.9),
            ),
        'HM[S,-r/2]': ( # [freeze]
            (44.5, 40.0, 36.8, 35.2, 34.7),
            (3.0, 5.0, 9.0, 17.0, 33.0),
            (12.4, 24.7, 33.8, 36.8, 37.0),
            ),
    }
elif whichone == 2:
    # effectiveness of HM
    data = {
        **ACT_R,
        **ACT_S,
        **HM_RM,
        **HM_SM,
    }
else:
    raise ValueError

styledict = {
    'ACT[R]': {
        'marker': '.',
        'linestyle': ':',
        'color': 'tab:cyan',
    },
    'ACT[S]': {
        'marker': '.',
        'linestyle': ':',
        'color': 'tab:orange',
    },
    'HM[R,M]': {
        'marker': 'v',
        'linestyle': '-.',
        'color': 'tab:blue',
    },
    'HM[S,M]': {
        'marker': '^',
        'linestyle': '-.',
        'color': 'tab:red',
    },
}

plt.figure(figsize=[10.8, 4.7])

ax = plt.subplot(1,2,1)
for (name, (r1, cost, ers)) in data.items():
    c.print(name, r1, cost, ers)

    if name in styledict:
        plt.plot(cost, ers, **(styledict[name]))
    elif name == 'HM(S,SGA)':
        plt.plot(cost, ers, marker='h', linestyle='-', color='deeppink')
    else:
        plt.plot(cost, ers, marker='+', linestyle='-.', color='k')
    #if isinstance(cost, float):
    #    plt.annotate(name, xy=(cost, ers))
    #elif isinstance(cost, tuple):
    #    plt.annotate(name, xy=(cost[0], ers[0]))
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

if whichone == 2:
    ax.legend(['ACT[$\mathcal{R}$]',
        'ACT[$\mathcal{S}$]',
        'HM[$\mathcal{R},\mathcal{M}$]',
        'HM[$\mathcal{S},\mathcal{M}$]'],
        bbox_to_anchor=(0.55,0.5))

ax = plt.subplot(1,2,2)
for (name, (r1, cost, ers)) in data.items():
    c.print(name, r1, cost, ers)

    if name in styledict:
        plt.plot(r1, ers, **(styledict[name]))
    elif name == 'HM(S,SGA)':
        plt.plot(r1, ers, f'h-', color='deeppink')
    else:
        plt.plot(r1, ers, f'-o', color='k')
    #if isinstance(ers, float):
    #    plt.annotate(name, xy=(r1, ers))
    #elif isinstance(ers, tuple):
    #    plt.annotate(name, xy=(r1[0], ers[0]))
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

if whichone == 2:
    ax.legend(['ACT[$\mathcal{R}$]',
        'ACT[$\mathcal{S}$]',
        'HM[$\mathcal{R},\mathcal{M}$]',
        'HM[$\mathcal{S},\mathcal{M}$]'],
        bbox_to_anchor=(0.55,0.5))

plt.tight_layout(pad=1.0)
#plt.show()

if whichone == 2:
    plt.savefig('fighmeff.svg')
else:
    plt.savefig('introplot.svg')
