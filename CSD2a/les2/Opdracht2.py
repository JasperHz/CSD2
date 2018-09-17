import simpleaudio as sa
import time
import numpy as np
import array

waveObject = sa.WaveObject.from_wave_file("./audioFiles/chord.wav")

# beatLengths is een array met lengte numPlaybackTimes gevuld met waardes van nootlengtes ingegeven door user
# nu wil ik de array beatLengths koppelen aan een geluid dat afgespeeld wordt met de lengte in van de array waarde

numPlaybackTimes = int(input())

beatLengths = []

for i in range(numPlaybackTimes):
    x = float(input())
    beatLengths.append(x)

bpm = input()
beatTime = 60 / int(bpm)

print(beatLengths)

print('Lets play the sound ' + str(numPlaybackTimes) + " times, at " + str(bpm) + " BPM. (One beat takes " + str(beatTime) + " seconds.")

def play (numTimes):
    for i in range(numTimes):
        sleepyTime = (beatLengths[i] * beatTime)
        print(i + 1, ". Playing sound for " + str(sleepyTime) + " seconds.")
        playObject = waveObject.play()
        time.sleep(sleepyTime)
        playObject.stop()

play(numPlaybackTimes)
