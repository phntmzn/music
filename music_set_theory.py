from itertools import permutations

# Convert note names to pitch classes
NOTE_TO_PC = {
    'C': 0,  'C#': 1,  'Db': 1,  'D': 2,  'D#': 3,  'Eb': 3,
    'E': 4,  'F': 5,  'F#': 6,  'Gb': 6,  'G': 7,  'G#': 8,
    'Ab': 8, 'A': 9,  'A#': 10, 'Bb': 10, 'B': 11
}

def to_pitch_classes(notes):
    return sorted({NOTE_TO_PC[n] % 12 for n in notes})

def transpose(pcset, n):
    return sorted((p + n) % 12 for p in pcset)

def invert(pcset):
    return sorted((12 - p) % 12 for p in pcset)

def normal_form(pcset):
    perms = [sorted([(n - p) % 12 for n in pcset]) for p in pcset]
    perms = sorted(perms, key=lambda x: (max(x) - min(x), x))
    return perms[0]

def prime_form(pcset):
    nf = normal_form(pcset)
    inv_nf = normal_form(invert(pcset))
    return min(nf, inv_nf)

def interval_vector(pcset):
    iv = [0] * 6
    for i in range(len(pcset)):
        for j in range(i+1, len(pcset)):
            interval = (pcset[j] - pcset[i]) % 12
            if 1 <= interval <= 6:
                iv[interval - 1] += 1
    return iv

# Example Usage
if __name__ == "__main__":
    notes = ['C', 'D', 'F']
    pcs = to_pitch_classes(notes)
    print("Pitch Classes:", pcs)
    print("Normal Form:", normal_form(pcs))
    print("Prime Form:", prime_form(pcs))
    print("Interval Vector:", interval_vector(pcs))
    print("Transposed +3:", transpose(pcs, 3))
    print("Inverted:", invert(pcs))
