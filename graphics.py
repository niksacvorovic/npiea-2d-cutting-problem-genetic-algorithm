import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def visualise(board, rectangles):
    fig, ax = plt.subplots()
    ax.set(xlim=board.width, ylim=board.height)
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
    for (i, rec) in enumerate(rectangles):
        patch = mpatches.Rectangle((rec.x, rec.y), rec.width, rec.height)
        patch.set_color(colors[i % len(colors)])
        ax.add_patch(patch)
    plt.show()