# retrograde.py

def retrograde_pitches(sequence):
    """
    Reverse the order of pitch sequence.
    Input:  List of pitch names or MIDI numbers.
    Output: Reversed list.
    """
    return sequence[::-1]

def retrograde_with_rhythm(notes_with_durations):
    """
    Reverse a melody that includes rhythm.
    Input:  List of (pitch, duration) tuples.
    Output: Reversed list of tuples.
    """
    return notes_with_durations[::-1]

def pretty_print_pitch_sequence(seq):
    return " → ".join(str(n) for n in seq)


# ------------------- Example -------------------
if __name__ == "__main__":
    # Basic retrograde of MIDI pitches
    melody = [60, 62, 64, 65, 67, 69, 71, 72]  # C major scale
    retro = retrograde_pitches(melody)

    print("Original melody (MIDI): ", pretty_print_pitch_sequence(melody))
    print("Retrograde melody     : ", pretty_print_pitch_sequence(retro))

    # Retrograde with rhythm (pitch, duration)
    melody_rhythm = [(60, 1.0), (62, 0.5), (64, 0.5), (65, 1.0)]
    retro_rhythm = retrograde_with_rhythm(melody_rhythm)

    print("\nOriginal melody with rhythm:")
    for note, dur in melody_rhythm:
        print(f"Note: {note}, Duration: {dur}")

    print("\nRetrograde melody with rhythm:")
    for note, dur in retro_rhythm:
        print(f"Note: {note}, Duration: {dur}")
