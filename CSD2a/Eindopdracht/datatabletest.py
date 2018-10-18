import random
from midiutil.MidiFile import MIDIFile
from midiutil import MIDIFile


#Generates an int for x, either 1 or 0
x = random.randrange(2)
print("X =",x)

#HIGH 5/4
highSeq54 = [
            [1,1,0,1,0],
            [1,0,1,0,1],
            [1,1,0,1,0],
            [1,1,1,1,1]
            ]

#HIGH 7/8
highSeq78 = [
            [1,1,0,1,1,0,1],
            [0,1,0,1,0,1,0],
            [1,0,1,0,1,0,1],
            [1,1,1,1,1,1,1]
            ]

#MID 5/4
midSeq54 = [
            [0,0,1,0,0],
            [1,0,1,0,1],
            [0,1,0,1,0],
            [0,0,1,0,1]
            ]

#MID 7/8
midSeq78 = [
            [0,0,0,1,0,0,1],
            [1,0,1,0,1,0,1],
            [0,1,0,1,0,1,0],
            [1,0,0,1,1,0,1]
            ]

#LOW 5/4
lowSeq54 = [
            [1,0,0,0,0],
            [1,0,1,0,0],
            [1,0,0,1,0],
            [1,0,0,1,1]
            ]

#LOW 7/8
lowSeq78 = [
            [1,0,0,0,0,0,0],
            [1,0,1,0,1,0,1],
            [1,0,0,1,0,1,0],
            [1,0,1,1,0,0,1]
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
    numerator == 4
    denominator == 5
elif rythmChoice == "7/8":
    chosenSeqHigh = highSeq78
    chosenSeqMid = midSeq78
    chosenSeqLow = lowSeq78
    numerator == 8
    denominator == 7
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

# ----- MIDI BULLSHIT -----

degrees  = [60, 62, 64, 65, 67, 69, 71, 72]  # MIDI note number
track    = 0
channel  = 0
time     = 0    # In beats
duration = 1    # In beats
tempo    = bpm  # In BPM
volume   = 100  # 0-127, as per the MIDI standard
trackName = IrregularBeatGenerator

addTimeSignature(track, time, numerator, denominator, clocks_per_tick, notes_per_quarter=8)
addTrackName(track, time, trackName)

MyMIDI = MIDIFile(3)  # One track, defaults to format 1 (tempo track is created
                      # automatically)
MyMIDI.addTempo(track, time, tempo)

for i, pitch in enumerate(finalSeqFlatLow):
    MyMIDI.addNote(track, channel, pitch, time + i, duration, volume)

with open("IrregularBeatGenerator.mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)





print("Done!")




# Extra zooi ------------------------

# HIGH
# if beatValue = 1:
#   sampleHigh.play
#   elif beatValue = x:
#     n = random.generate(0 of 1)
#     if n = 1:
#       sampleHigh.play
# else niks
