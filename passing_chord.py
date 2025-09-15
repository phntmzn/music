from typing import List, Tuple

SEMITONE_STEPS = {'C': 0, 'C#': 1, 'Db': 1, 'D': 2, 'D#': 3, 'Eb': 3,
                  'E': 4, 'F': 5, 'F#': 6, 'Gb': 6, 'G': 7, 'G#': 8, 'Ab': 8,
                  'A': 9, 'A#': 10, 'Bb': 10, 'B': 11}

NOTE_ORDER = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#',
              'G', 'G#', 'A', 'A#', 'B']

def note_to_index(note: str) -> int:
    return SEMITONE_STEPS[note]

def index_to_note(index: int) -> str:
    return NOTE_ORDER[index % 12]

def root_of(chord: str) -> str:
    return chord.rstrip('m7Mdimaug')

def add_passing_chords(prog: List[str]) -> List[str]:
    new_prog = []

    for i in range(len(prog) - 1):
        root1 = note_to_index(root_of(prog[i]))
        root2 = note_to_index(root_of(prog[i + 1]))

        new_prog.append(prog[i])

        # Find chromatic or stepwise root motion
        if abs(root2 - root1) == 2:
            mid = (root1 + (1 if root2 > root1 else -1)) % 12
            passing = index_to_note(mid) + 'm7'  # default minor 7 as jazzy filler
            new_prog.append(passing)

    new_prog.append(prog[-1])
    return new_prog

if __name__ == "__main__":
    original = ['Cmaj7', 'Em7', 'Am7', 'Dm7', 'G7', 'Cmaj7']
    enhanced = add_passing_chords(original)

    print("Original progression:")
    print(" → ".join(original))

    print("\nWith passing chords:")
    print(" → ".join(enhanced))
