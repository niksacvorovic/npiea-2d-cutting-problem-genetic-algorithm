import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import math
from numpy import array

def visualise(chromosome, stock_width, stock_height):
    """
    Plots all genes (boards) from a chromosome in a single figure using a grid of subplots.
    """
    num_genes = len(chromosome.array)
    if num_genes == 0:
        print("Chromosome is empty, nothing to display.")
        return

    # Determine the grid size for the subplots (e.g., 2x2, 3x1, etc.)
    cols = int(math.ceil(math.sqrt(num_genes)))
    rows = int(math.ceil(num_genes / cols))

    # Create a figure and a set of subplots
    # figsize can be adjusted to make the overall window larger
    fig, axes = plt.subplots(rows, cols, figsize=(cols * 5, rows * 5))

    # If there's only one plot, axes is not an array, so make it one
    if num_genes == 1:
        axes = array([axes])

    # Flatten the axes array to make it easy to iterate over
    axes = axes.flatten()

    colors = ['#4E79A7', '#F28E2B', '#E15759', '#76B7B2', '#59A14F', '#EDC948', '#B07AA1']

    # Loop through each gene and its corresponding subplot axis
    for i, gene in enumerate(chromosome.array):
        ax = axes[i]
        ax.set_title(f"Gen {i + 1}")
        ax.set_xlim(0, stock_width)
        ax.set_ylim(0, stock_height)
        ax.set_aspect('equal', adjustable='box')

        # Plot all pieces for the current gene
        for rec in gene.pieces:
            # rec is (x, y, rotation, Piece_object)
            x_pos, y_pos, rotation, piece_obj = rec

            width = piece_obj.width
            height = piece_obj.height

            if rotation == 1:
                height, width = width, height

            patch = mpatches.Rectangle((x_pos, y_pos), width, height, edgecolor='k')
            patch.set_facecolor(colors[piece_obj.id % len(colors)])
            ax.add_patch(patch)

            ax.text(x_pos + width / 2, y_pos + height / 2, f'ID:{piece_obj.id}',
                    ha='center', va='center', color='white', fontsize=8)

    # Turn off any unused subplots in the grid
    for i in range(num_genes, len(axes)):
        axes[i].axis('off')

    plt.tight_layout(pad=3.0)  # Adds padding between plots
    plt.show()

