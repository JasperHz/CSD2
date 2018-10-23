import simpleaudio as sa
import time
import random
from midiutil.MidiFile import MIDIFile
from midiutil import MIDIFile

bpm = 120
numerator = 4
denominator = 5

finalSeqFlatHigh = [1,1,1,1,1,1,1,1]
finalSeqFlatMid =  [1,0,1,1,0,1,1,0]
finalSeqFlatLow =  [1,0,1,0,1,0,1,0]



track    = 0
channel  = 0
time     = 0    # In beats
duration = 0.5  # In beats
tempo    = bpm  # In BPM
volume   = 100  # 0-127, as per the MIDI standard
trackName = "IrregularBeatGenerator"
clocks_per_tick = 24


MyMIDI = MIDIFile(1)  # Three track, defaults to format 1 (tempo track is created
                      # automatically)

MyMIDI.addTimeSignature(track, time, numerator, denominator, clocks_per_tick, notes_per_quarter=8)
MyMIDI.addTrackName(track, time, trackName)

MyMIDI.addTempo(track, time, tempo)

for i, pitch in enumerate(finalSeqFlatHigh):
    if finalSeqFlatHigh[i] == 1:
        MyMIDI.addNote(track, channel, 62, time + i, duration, volume)

for i, pitch in enumerate(finalSeqFlatMid):
    if finalSeqFlatMid[i] == 1:
        MyMIDI.addNote(track, channel, 61, time + i, duration, volume)

for i, pitch in enumerate(finalSeqFlatLow):
    if finalSeqFlatLow[i] == 1:
        MyMIDI.addNote(track, channel, 60, time + i, duration, volume)

print("Would you like to save this to a MIDI file? Y/N")
writeToMidi = input()

if writeToMidi == "Y":
    with open("IrregularBeatGenerator.mid", "wb") as output_file:
        MyMIDI.writeFile(output_file)
        print("Written to IrregularBeatGenerator.mid")
else: print("No MIDI written.")
