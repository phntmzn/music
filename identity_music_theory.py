# identity_music_theory.py

NOTES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

SCALE_PATTERNS = {
    'major':        [2, 2, 1, 2, 2, 2, 1],
    'minor':        [2, 1, 2, 2, 1, 2, 2],
    'locrian':      [1, 2, 2, 1, 2, 2, 2],
    'dorian':       [2, 1, 2, 2, 2, 1, 2],
    'phrygian':     [1, 2, 2, 2, 1, 2, 2],
    'lydian':       [2, 2, 2, 1, 2, 2, 1],
    'mixolydian':   [2, 2, 1, 2, 2, 1, 2],
    'harmonic_minor': [2, 1, 2, 2, 1, 3, 1],
}

CHORD_PATTERNS = {
    'major':      [0, 4, 7],
    'minor':      [0, 3, 7],
    'diminished': [0, 3, 6],
    'augmented':  [0, 4, 8],
    'maj7':       [0, 4, 7, 11],
    'min7':       [0, 3, 7, 10],
    'dom7':       [0, 4, 7, 10],
    'dim7':       [0, 3, 6, 9],
}

def get_scale(root, pattern):
    idx = NOTES.index(root)
    scale = [NOTES[idx]]
    for step in pattern:
        idx = (idx + step) % 12
        scale.append(NOTES[idx])
    return scale

def identify_scale(given_notes):
    for name, pattern in SCALE_PATTERNS.items():
        for root in NOTES:
            scale = get_scale(root, pattern)[:-1]
            if set(scale) == set(given_notes):
                return f"{root} {name} scale"
    return "Unknown scale"

def identify_chord(given_notes):
    indices = sorted([NOTES.index(n) for n in given_notes])
    for root in NOTES:
        root_idx = NOTES.index(root)
        for name, intervals in CHORD_PATTERNS.items():
            chord = [(root_idx + i) % 12 for i in intervals]
            if sorted(chord) == [NOTES.index(n) % 12 for n in given_notes]:
                return f"{root} {name} chord"
    return "Unknown chord"

# Example usage
if __name__ == "__main__":
    print(identify_scale(['C', 'D', 'E', 'F', 'G', 'A', 'B']))      # C major
    print(identify_scale(['C', 'D', 'D#', 'F', 'G', 'G#', 'A#']))   # C locrian
    print(identify_chord(['C', 'E', 'G']))                          # C major
    print(identify_chord(['C', 'Eb', 'G', 'Bb']))                   # C min7
