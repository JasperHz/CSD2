import simpleaudio as sa
import time
import numpy as np
import array

waveObject = sa.WaveObject.from_wave_file("./audioFiles/chord.wav")

print("Hoe vaak wil je de sample afspelen?")

numPlaybackTimes = int(input())

beatLengths = []

print("Geef nu " + str(numPlaybackTimes) + " nootwaardes in.")

for i in range(numPlaybackTimes):
    x = float(input())
    beatLengths.append(x)

print("Welk BPM wil je gebruiken?")

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







# python3 Opdracht2.py < input.txt  om aan te roepen.
# hihat = sa.WaveObject
#
# def playSample(sampleObject):
#     play_obj = sampleObject.play()
#
# playSample(hihat[1])
