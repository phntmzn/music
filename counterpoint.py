from random import choice

# MIDI pitch names for reference
NOTE_NAMES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
CONSONANT_INTERVALS = [0, 3, 4, 5, 7, 8, 9]  # unison, 3rd, 4th, 5th, 6th, octave

def pitch_to_str(pitch):
    return NOTE_NAMES[pitch % 12] + str(pitch // 12)

def generate_counterpoint(cantus_firmus, key='C', mode='ionian'):
    counterpoint = []

    for i, note in enumerate(cantus_firmus):
        candidates = []
        for interval in CONSONANT_INTERVALS:
            up = note + interval
            down = note - interval
            for p in [up, down]:
                if 40 <= p <= 80:  # vocal range constraint
                    candidates.append(p)

        # Avoid direct repetition of previous interval
        if counterpoint:
            prev_interval = abs(counterpoint[-1] - cantus_firmus[i-1])
            candidates = [p for p in candidates if abs(p - note) != prev_interval]

        if not candidates:
            return None  # Failed to find valid note

        selected = choice(candidates)
        counterpoint.append(selected)

    return counterpoint

# Example cantus firmus (in MIDI note numbers)
cantus = [60, 62, 64, 65, 67, 69, 71, 72]  # C major scale

cp = generate_counterpoint(cantus)

if cp:
    print("Cantus Firmus: ", [pitch_to_str(p) for p in cantus])
    print("Counterpoint : ", [pitch_to_str(p) for p in cp])
else:
    print("Failed to generate valid counterpoint.")
