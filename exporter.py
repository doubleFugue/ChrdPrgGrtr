
from info import tempo as gTempo # Imports tempo variable from info.py
from generator import chord_progression as chordprog
from jchord import ChordProgression, MidiConversionSettings # Imports external library jchord

def midiExporter():
    strChordprog = ' '.join(chordprog) # Converts chordprog to a string seperated by spaces (since ChordProgression only accepts strings)
    prog = ChordProgression.from_string(strChordprog)
    prog.to_midi(MidiConversionSettings(filename="exportedMidi.midi", tempo=gTempo, beats_per_chord=4, instrument=16))
    return


