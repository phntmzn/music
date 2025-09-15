import numpy as np
import sounddevice as sd
from scipy.signal import windows

# Shepard tone parameters
SAMPLE_RATE = 44100
DURATION = 1.0  # seconds
BASE_FREQUENCIES = [110 * 2**(i / 12) for i in range(12)]  # C to B

def shepard_tone(frequency, center=370.0, octaves=6):
    """
    Generate a Shepard tone centered at `center` frequency.
    """
    t = np.linspace(0, DURATION, int(SAMPLE_RATE * DURATION), endpoint=False)
    tone = np.zeros_like(t)

    for n in range(-octaves, octaves + 1):
        f = frequency * (2 ** n)
        if f < 20 or f > SAMPLE_RATE / 2:
            continue
        gaussian = np.exp(-0.5 * (np.log2(f / center) ** 2) / (0.5 ** 2))
        tone += gaussian * np.sin(2 * np.pi * f * t)

    # Normalize
    tone /= np.max(np.abs(tone))
    # Optional: fade envelope to avoid clicks
    tone *= windows.hann(len(tone))

    return tone

def play_pair(note1_freq, note2_freq):
    tone1 = shepard_tone(note1_freq)
    tone2 = shepard_tone(note2_freq)
    sound = np.concatenate([tone1, tone2])
    sd.play(sound, SAMPLE_RATE)
    sd.wait()

# ----------- Tritone Example -------------

def midi_to_freq(midi_note):
    return 440.0 * 2 ** ((midi_note - 69) / 12)

if __name__ == "__main__":
    # Example 1: C → F#
    note1 = midi_to_freq(60)  # C4
    note2 = midi_to_freq(66)  # F#4 (tritone)

    print("Playing C → F# Shepard tone pair...")
    play_pair(note1, note2)

    # Example 2: G → C#
    input("Press Enter to continue to G → C#...")
    note3 = midi_to_freq(67)  # G4
    note4 = midi_to_freq(61)  # C#4

    print("Playing G → C# Shepard tone pair...")
    play_pair(note3, note4)
