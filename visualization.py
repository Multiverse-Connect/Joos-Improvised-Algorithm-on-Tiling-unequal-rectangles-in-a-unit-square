import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle as PatchRect
import random


def random_color():

    return (
        random.random(),
        random.random(),
        random.random()
    )


def draw(algo):

    fig, ax = plt.subplots(figsize=(10, 10))

    # ---------------------------------------------------------
    # Draw packed rectangles
    # ---------------------------------------------------------

    for p in algo.placements:

        color = random_color()

        rect = PatchRect(
            (p.x, p.y),
            p.width,
            p.height,
            facecolor=color,
            edgecolor='black',
            linewidth=0.5,
            alpha=0.7
        )

        ax.add_patch(rect)

    # ---------------------------------------------------------
    # Draw remaining empty boxes
    # ---------------------------------------------------------

    for b in algo.boxes:

        rect = PatchRect(
            (b.x, b.y),
            b.w,
            b.h,
            fill=False,
            edgecolor='red',
            linestyle='dashed',
            linewidth=1.0
        )

        ax.add_patch(rect)

    # ---------------------------------------------------------
    # Axes settings
    # ---------------------------------------------------------

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    ax.set_aspect('equal')

    ax.set_title("Algorithm A Rectangle Packing")

    plt.tight_layout()

    plt.show()