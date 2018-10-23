import simpleaudio as sa
import time
import random
from midiutil.MidiFile import MIDIFile
from midiutil import MIDIFile

x = 0

#HIGH 5/4
highSeq54 = [
            [1,1,0,x,0],
            [1,0,x,0,1],
            [1,1,x,1,0],
            [1,x,1,1,1]
            ]

#HIGH 7/8
highSeq78 = [
            [1,1,x,1,1,0,1],
            [0,1,0,1,x,1,0],
            [1,0,1,0,1,0,1],
            [1,1,1,1,1,x,1]
            ]

#MID 5/4
midSeq54 = [
            [0,0,x,0,0],
            [1,0,1,0,1],
            [0,1,0,1,0],
            [0,0,1,x,1]
            ]

#MID 7/8
midSeq78 = [
            [0,0,0,x,0,0,1],
            [1,0,1,0,1,0,1],
            [0,1,0,1,x,1,0],
            [1,0,x,1,1,0,1]
            ]

#LOW 5/4
lowSeq54 = [
            [1,0,0,0,0],
            [1,0,x,0,0],
            [1,0,0,1,0],
            [1,0,0,x,1]
            ]

#LOW 7/8
lowSeq78 = [
            [1,0,x,0,x,0,0],
            [1,0,1,0,1,0,1],
            [1,0,x,1,0,1,0],
            [1,0,1,x,0,0,1]
            ]

print("Which measure would you like to use? Type 5/4 or 7/8")
rythmChoice = input()

chosenSeqHigh = []
chosenSeqMid = []
chosenSeqLow = []
numerator = 0
denominator = 0

if rythmChoice == "5/4":
    chosenSeqHigh = highSeq54
    chosenSeqMid = midSeq54
    chosenSeqLow = lowSeq54
    numerator = 4
    denominator = 5
elif rythmChoice == "7/8":
    chosenSeqHigh = highSeq78
    chosenSeqMid = midSeq78
    chosenSeqLow = lowSeq78
    numerator = 8
    denominator = 7
else:
    print("ERROR - invalid input")

finalSeqHigh = []
finalSeqMid = []
finalSeqLow = []

#Repeats through the rythm data a set amount of times(8) and appends them to a single list (output: 8 lists in 1 list)
for i in range(8):
    p = random.choice(chosenSeqHigh)
    finalSeqHigh.append(p)

finalSeqFlatHigh = []

#Goes through the lists with lists and turns it into one big list
for sublist in finalSeqHigh:
    for item in sublist:
        finalSeqFlatHigh.append(item)

#Repeats through the rythm data a set amount of times(8) and appends them to a single list (output: 8 lists in 1 list)
for i in range(8):
    p = random.choice(chosenSeqMid)
    finalSeqMid.append(p)

finalSeqFlatMid = []

#Goes through the lists with lists and turns it into one big list
for sublist in finalSeqMid:
    for item in sublist:
        finalSeqFlatMid.append(item)

#Repeats through the rythm data a set amount of times(8) and appends them to a single list (output: 8 lists in 1 list)
for i in range(8):
    p = random.choice(chosenSeqLow)
    finalSeqLow.append(p)

finalSeqFlatLow = []

#Goes through the lists with lists and turns it into one big list
for sublist in finalSeqLow:
    for item in sublist:
        finalSeqFlatLow.append(item)



print("High play data:",finalSeqFlatHigh)
print("Mid play data:",finalSeqFlatMid)
print("Low play data:",finalSeqFlatLow)

Kick = sa.WaveObject.from_wave_file("./chord.wav")
Snare = sa.WaveObject.from_wave_file("./chord.wav")
Hihat = sa.WaveObject.from_wave_file("./chord.wav")

# Kick = sa.WaveObject.from_wave_file("./audioFiles/Kick_17_copy.wav")
# Snare = sa.WaveObject.from_wave_file("./audioFiles/Snare_808_2_copy.wav")
# Hihat = sa.WaveObject.from_wave_file("./audioFiles/Shaker_02_copy1.wav")


bpm = 80
# Calculate quarter note duration
quarterNote = 60 / bpm
# Calculate sixteenth note duration
sixteenthNote = quarterNote / 4.0

# Use the length of the finalSeqFlatLow to go through the all the lists
for i in range(len(finalSeqFlatLow)):

    if finalSeqFlatLow[i] == x:
        finalSeqFlatLow[i] = random.randrange(2)
    if finalSeqFlatLow == 1:
        Kick.play()
    if finalSeqFlatMid[i] == x:
        finalSeqFlatMid[i] = random.randrange(2)
    if finalSeqFlatMid[i] == 1:
        Snare.play()
    if finalSeqFlatHigh[i] == x:
        finalSeqFlatHigh[i] = random.randrange(2)
    if finalSeqFlatHigh[i] == 1:
        Hihat.play()
    # Wait a 16th note and repeat the loop
    time.sleep(sixteenthNote)


# ----- MIDI BULLSHIT -----

track    = 0
channel  = 0
time     = 0    # In beats
duration = 0.25 # In beats
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

print("Done!")
