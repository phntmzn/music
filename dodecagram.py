import matplotlib.pyplot as plt
import numpy as np

NOTE_NAMES = ['C', 'C#', 'D', 'D#', 'E', 'F',
              'F#', 'G', 'G#', 'A', 'A#', 'B']

def plot_dodecagram(pitch_classes, title="Dodecagram", connect=True):
    """
    pitch_classes: List of pitch class integers (0-11)
    """
    theta = np.linspace(0, 2 * np.pi, 12, endpoint=False)
    x = np.cos(theta)
    y = np.sin(theta)

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_aspect('equal')
    ax.axis('off')

    # Draw the circle and place labels
    for i in range(12):
        ax.plot(x[i], y[i], 'o', color='black')
        ax.text(1.15 * x[i], 1.15 * y[i], NOTE_NAMES[i],
                ha='center', va='center', fontsize=10)

    # Connect pitch classes
    points_x = [x[i] for i in pitch_classes]
    points_y = [y[i] for i in pitch_classes]

    if connect:
        ax.plot(points_x + [points_x[0]], points_y + [points_y[0]],
                color='blue', linewidth=2, linestyle='-')
        ax.scatter(points_x, points_y, color='red', zorder=5)

    ax.set_title(title)
    plt.show()

# ---------------- Example ----------------

if __name__ == "__main__":
    # Twelve-tone row (random or custom)
    tone_row = [0, 4, 2, 7, 9, 11, 3, 8, 10, 5, 1, 6]
    plot_dodecagram(tone_row, title="12-Tone Row Dodecagram")
