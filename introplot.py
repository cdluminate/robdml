import numpy as np
import matplotlib.pyplot as plt
import rich
c = rich.get_console()

data = {
        #'N/A': (53.9, 1.0, 3.8),
        #'EST': (8.5, 33.0, 5.3),
        'ACT': (
            (27.5, 28.6, 33.3),
            (33.0, 17.0, 8.0),
            (33.9, 34.7, 27.3),
            ),
        'amdsemi': (
            (25.6, 25.1, 28.0),
            (33.0, 17.0, 8.0),
            (38.0, 36.6, 33.5),
            ),
        'amdsemi+aap0': (26.2, 9.0, 40.0),
        'hml2rm': (27.4, 9.0, 32.9),
        'hml2rmi': (25.2, 9.0, 39.8),
        }

plt.figure()

plt.subplot(1,2,1)
for (name, (r1, cost, ers)) in data.items():
    c.print(name, r1, cost, ers)

    color = 'k'
    if name == 'EST':
        color = 'b'
    if name == 'ACT':
        color = 'r'
    plt.plot(cost, ers, f'-{color}o')
    if isinstance(cost, float):
        plt.annotate(name, xy=(cost, ers))
    elif isinstance(cost, tuple):
        plt.annotate(name, xy=(cost[0], ers[0]))
plt.xlabel('Training Cost')
plt.ylabel('Robustness (ERS)')
plt.xscale('log', base=2)
#plt.axis('equal')

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


plt.subplot(1,2,2)
for (name, (r1, cost, ers)) in data.items():
    c.print(name, r1, cost, ers)

    color = 'k'
    if name == 'EST':
        color = 'b'
    if name == 'ACT':
        color = 'r'
    plt.plot(ers, r1, f'-{color}o')
    if isinstance(ers, float):
        plt.annotate(name, xy=(ers, r1))
    elif isinstance(ers, tuple):
        plt.annotate(name, xy=(ers[0], r1[0]))
plt.xlabel('Robustness (ERS)')
plt.ylabel('Recall@1 (R@1)')
#plt.axis('equal')


#plt.tight_layout()
plt.show()
