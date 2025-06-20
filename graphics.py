import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.widgets import Button
from classes import Chromosome, Gene, Piece

def visualise(chromosome):
    fig, ax = plt.subplots()
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
    plt.subplots_adjust(bottom=0.2)
    axprev = plt.axes([0.3, 0.05, 0.15, 0.075])  # [left, bottom, width, height]
    axnext = plt.axes([0.55, 0.05, 0.15, 0.075])
    index = 0

    def plot_current(index):
        ax.set(xlim=chromosome.array[index].board.width, ylim=chromosome.array[index].board.width)
        for (i, rec) in enumerate(chromosome.array[index].pieces):
            patch = mpatches.Rectangle((rec[0], rec[1]), rec[2].width, rec[2].height)
            patch.set_color(colors[i % len(colors)])
            ax.add_patch(patch)
    
    def next_plot(event):
        nonlocal index
        if index < len(chromosome.array) - 1:
            index += 1
            ax.clear()
            ax.set_title(f"Board {index + 1}")
            plot_current(index)
            fig.canvas.draw_idle()

    def prev_plot(event):
        nonlocal index
        if index > 0:
            index -= 1
            ax.clear()
            ax.set_title(f"Board {index + 1}")
            plot_current(index)
            fig.canvas.draw_idle()

    btn_prev = Button(axprev, 'Previous')
    btn_prev.on_clicked(prev_plot)

    btn_next = Button(axnext, 'Next')
    btn_next.on_clicked(next_plot)

    ax.set_title(f"Board {index + 1}")
    plot_current(index)

    plt.show()

# pieces = [Piece(1, 10, 20), Piece(2, 20, 25), Piece(3, 20, 15), Piece(4, 10, 20), 
        #   Piece(5, 15, 15), Piece(6, 20, 5)]
# genes = [Gene(Piece(10, 100, 100), [(30, 30, pieces[1]), (50, 50, pieces[2])]), 
        #  Gene(Piece(10, 100, 100), [(0, 0, pieces[0])]),
        #  Gene(Piece(10, 100, 100), [(20, 20, pieces[3]), (60, 30, pieces[4]), (20, 40, pieces[5])])]
# chromosome = Chromosome(genes)
# visualise(chromosome)