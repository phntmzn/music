# circle_progressions.py

CHORD_QUALITIES = {
    'I': 'maj7',
    'ii': 'min7',
    'iii': 'min7',
    'IV': 'maj7',
    'V': '7',
    'vi': 'min7',
    'vii°': 'dim7'
}

CIRCLE_OF_FIFTHS = ['C', 'G', 'D', 'A', 'E', 'B', 'F#', 'Db', 'Ab', 'Eb', 'Bb', 'F']

def circle_progression(start='C', steps=4):
    """
    Generate a descending fifths progression (circle progression)
    e.g., E7 → A7 → D7 → G7
    """
    try:
        idx = CIRCLE_OF_FIFTHS.index(start)
    except ValueError:
        raise ValueError(f"Start key {start} not in circle of fifths")

    progression = []
    for i in range(steps):
        chord = CIRCLE_OF_FIFTHS[(idx + i) % 12] + '7'
        progression.append(chord)
    return progression


def ragtime_bridge(key='C'):
    """
    Returns the classic III7–VI7–II7–V7 → I turnaround
    For C major: E7–A7–D7–G7 → C
    """
    fifths = circle_progression('E', 4)  # E7 → A7 → D7 → G7
    return fifths + [key]


def classical_circle_vi_ii_V_I(key='C'):
    """
    Returns vi–ii–V–I progression in the given key
    For C major: Am7–Dm7–G7–Cmaj7
    """
    if key != 'C':
        raise NotImplementedError("Only C major supported for simplicity")

    return ['Am7', 'Dm7', 'G7', 'Cmaj7']


def full_circle_progression(key='C'):
    """
    Return all 7 diatonic chords in a full circle progression from the key
    vi → ii → V → I
    """
    return ['Am7', 'Dm7', 'G7', 'Cmaj7', 'Fmaj7', 'Bm7b5', 'Em7']


# ------------------- Example -------------------

if __name__ == "__main__":
    print("🎹 Ragtime Bridge (III7–VI7–II7–V7 → I):")
    print(" → ".join(ragtime_bridge()))

    print("\n🎼 Classical Circle Progression (vi–ii–V–I):")
    print(" → ".join(classical_circle_vi_ii_V_I()))

    print("\n🌀 Full Circle Progression:")
    print(" → ".join(full_circle_progression()))
