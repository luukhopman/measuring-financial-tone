import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix


def log_step(func):
    """
    Decorates a function that manipulates a pandas DataFrame to add logging statements
    :param func: function to log
    :returns: the result of the function
    """
    def wrapper(df, *args, **kwargs):
        result = func(df, *args, **kwargs)
        print(
            f'[{func.__name__}] nrows={result.shape[0]:,} ncols={result.shape[1]:,}')
        return result
    return wrapper


def accuracy_f1_score(y_true, y_pred):
    accuracy = accuracy_score(y_true, y_pred)
    f1 = f1_score(y_true, y_pred, average='weighted')
    print(f"Accuracy: {accuracy:.2%}\nF1-score: {f1:.2%}")


def plot_confusion_matrix(y_true, y_pred, xlabel='', ylabel=None, ax=None):
    # Set font
    plt.rcParams['font.sans-serif'] = 'Roboto'

    # Create confusion matrix
    labels = ['negative', 'neutral', 'positive']
    cm = confusion_matrix(y_true, y_pred, normalize='true', labels=labels)

    # Plot matrix
    g = sns.heatmap(cm, cbar=False, vmin=0, vmax=1, cmap='binary',
                    center=0.5, linewidth=0.05, annot_kws={"fontsize": 22},
                    square=True, annot=True,  fmt='.2f', ax=ax)

    # Labels
    g.set_xlabel(xlabel, fontsize=22, labelpad=10, fontweight='bold')
    g.set_ylabel(ylabel, fontsize=22, labelpad=10, fontweight='bold')
    g.xaxis.set_label_position('top')

    # Handle ticks
    tick_labels = [f'${l.title()}$' for l in labels]  # italics
    g.set_xticklabels(tick_labels, ha='center', fontsize=18)
    g.set_yticklabels(tick_labels, va='center', fontsize=18)
    g.xaxis.set_ticks_position('top')
    g.tick_params(axis='both', which='both', length=0)
