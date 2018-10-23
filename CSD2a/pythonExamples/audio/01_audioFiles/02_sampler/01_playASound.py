# simpleaudio is imported as sa -> shorter name
import simpleaudio as sa

"""
An example project in which three wav files are played after eachother.

------ HANDS-ON TIPS ------
- Answer the following question before running the code:
  Do you expect to hear the samples played simultaniously or after eachother?
  Why?

  Ik denk dat ze na elkaar aspelen aangezien er een wait_done tussen elke sample staat

- Alter the code:
  Play the sounds simultaniously.

- Alter the code:
  Ask the user to choose which one of the three samples should be played and
  only play the chosen sample.
"""

# load 3 audioFiles
sampleHigh = sa.WaveObject.from_wave_file("../audioFiles/Pop.wav")
sampleMid = sa.WaveObject.from_wave_file("../audioFiles/Laser1.wav")
sampleLow = sa.WaveObject.from_wave_file("../audioFiles/Dog2.wav")


print("Which sample do you want to play: HIGH, MID or LOW?")
sampleChoice = input()

if sampleChoice == "HIGH":
    sampleHighPlay = sampleHigh.play()
    sampleHighPlay.wait_done()
elif sampleChoice == "MID":
    sampleMidPlay = sampleMid.play()
    sampleMidPlay.wait_done()
elif sampleChoice == "LOW":
    sampleLowPlay = sampleLow.play()
    sampleLowPlay.wait_done()
else:
    print("ERROR - invalid input")
