import simpleaudio as sa
import time
import random
from midiutil.MidiFile import MIDIFile
from midiutil import MIDIFile

x = 0

#HIGH 5/4=
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
            [0,1,0,1,0],
            [1,0,1,0,1],
            [0,x,0,x,0],
            [0,0,1,x,0]
            ]

#MID 7/8
midSeq78 = [
            [0,1,0,1,0,1,0],
            [1,0,1,0,1,0,1],
            [0,1,0,x,0,1,0],
            [1,0,0,0,1,0,0]
            ]

#LOW 5/4
lowSeq54 = [
            [1,0,0,0,0],
            [1,0,0,0,0],
            [1,0,0,0,0],
            [1,0,0,x,0],
            [1,0,0,1,0],
            [1,0,1,x,0]
            ]

#LOW 7/8
lowSeq78 = [
            [1,0,0,0,0,0,0],
            [1,0,0,0,0,0,0],
            [1,0,0,0,0,0,0],
            [1,0,0,0,x,0,0],
            [1,0,x,0,1,0,0],
            [1,0,1,0,x,0,1]
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
for i in range(32):
    p = random.choice(chosenSeqHigh)
    finalSeqHigh.append(p)

finalSeqFlatHigh = []

#Goes through the lists with lists and turns it into one big list
for sublist in finalSeqHigh:
    for item in sublist:
        finalSeqFlatHigh.append(item)

#Repeats through the rythm data a set amount of times(8) and appends them to a single list (output: 8 lists in 1 list)
for i in range(32):
    p = random.choice(chosenSeqMid)
    finalSeqMid.append(p)

finalSeqFlatMid = []

#Goes through the lists with lists and turns it into one big list
for sublist in finalSeqMid:
    for item in sublist:
        finalSeqFlatMid.append(item)

#Repeats through the rythm data a set amount of times(8) and appends them to a single list (output: 8 lists in 1 list)
for i in range(32):
    p = random.choice(chosenSeqLow)
    finalSeqLow.append(p)

finalSeqFlatLow = []

#Goes through the lists with lists and turns it into one big list
for sublist in finalSeqLow:
    for item in sublist:
        finalSeqFlatLow.append(item)

print("What BPM do you want to use?")
bpmInput = float(input())

print("Do you want to choose the samples? Y/N")

inputChangeSamples = input()

if inputChangeSamples == "Y":

    print("Which kick do you want to use? 1, 2 or 3?")
    inputKickChoice = input()

    if inputKickChoice == "1":
        Kick = sa.WaveObject.from_wave_file("./audioFiles/Kick_1.wav")

    elif inputKickChoice == "2":
        Kick = sa.WaveObject.from_wave_file("./audioFiles/Kick_2.wav")

    elif inputKickChoice == "3":
        Kick = sa.WaveObject.from_wave_file("./audioFiles/Kick_3.wav")

    else: print("Error, please choose one of 3 options!")

    print("Which snare do you want to use? 1, 2 or 3?")
    inputSnareChoice = input()

    if inputSnareChoice == "1":
        Snare = sa.WaveObject.from_wave_file("./audioFiles/Snare_1.wav")

    elif inputSnareChoice == "2":
        Snare = sa.WaveObject.from_wave_file("./audioFiles/Snare_2.wav")

    elif inputSnareChoice == "3":
        Snare = sa.WaveObject.from_wave_file("./audioFiles/Snare_3.wav")

    else: print("Error, please choose one of 3 options!")

    print("Which Hihat do you want to use? 1, 2 or 3?")
    inputHihatChoice = input()

    if inputHihatChoice == "1":
        Hihat = sa.WaveObject.from_wave_file("./audioFiles/Hihat_1.wav")

    elif inputHihatChoice == "2":
        Hihat = sa.WaveObject.from_wave_file("./audioFiles/Hihat_2.wav")

    elif inputHihatChoice == "3":
        Hihat = sa.WaveObject.from_wave_file("./audioFiles/Hihat_3.wav")

    else: print("Error, please choose one of 3 options!")

else:
    Kick = sa.WaveObject.from_wave_file("./audioFiles/Kick_1.wav")
    Snare = sa.WaveObject.from_wave_file("./audioFiles/Snare_1.wav")
    Hihat = sa.WaveObject.from_wave_file("./audioFiles/Hihat_1.wav")


print("High play data:",finalSeqFlatHigh)
print("Mid play data:",finalSeqFlatMid)
print("Low play data:",finalSeqFlatLow)


bpm = bpmInput
# Calculate quarter note duration
quarterNote = 60 / bpm
# Calculate sixteenth note duration
sixteenthNote = quarterNote / 4.0

# Use the length of the finalSeqFlatLow to go through the all the lists
for i in range(len(finalSeqFlatLow)):

    if finalSeqFlatLow[i] == x:
        finalSeqFlatLow[i] = random.randrange(2)
    if finalSeqFlatLow[i] == 1:
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


# ----- MIDI EXPORT -----

track    = 0
channel  = 0
time     = 0    # In beats
duration = 1    # In beats
tempo    = bpm  # In BPM
volume   = 100  # 0-127, as per the MIDI standard
trackName = "IrregularBeatGenerator"
clocks_per_tick = 24

MyMIDI = MIDIFile(1)  # One track, defaults to format 1 (tempo track is created
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
