import matplotlib.pyplot as plt
import seaborn as sns

sns.set(font='Roboto',
        rc={'figure.figsize': (12, 5),
            'figure.facecolor': 'white',
            'savefig.facecolor': 'white',
            'axes.titlesize': 18,
            'axes.titleweight': 'bold',
            'axes.titlepad': 10,
            'axes.labelsize': 13,
            'xtick.labelsize': 11,
            'ytick.labelsize': 11,
            'axes.spines.right': False,
            'axes.spines.top': False,
            'axes.spines.left': False,
            'axes.edgecolor': 'dimgrey',
            'axes.facecolor': 'white',
            'axes.labelcolor': 'black',
            'axes.grid': 'y',
            'grid.linewidth': 0.5,
            'grid.color': 'dimgrey',
            'legend.facecolor': 'none',
            'legend.edgecolor': 'none',
            'lines.linewidth': 1.5,
            'lines.solid_capstyle': 'round',
            'patch.edgecolor': 'white',
            'patch.force_edgecolor': True,
            'text.color': 'black',
            'axes.labelcolor': 'black',
            'xtick.top': False,
            'xtick.bottom': False,
            'ytick.left': False,
            'ytick.right': False})

color_list = ['#000000', '#404040']
linestyle_list = ['-', ':']
plt.rcParams['axes.prop_cycle'] = plt.cycler(color=color_list,
                                             linestyle=linestyle_list)
