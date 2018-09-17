import array

numPlaybackTimes = int(input())
beatLengths = []
for i in range(numPlaybackTimes):
    x = float(input())
    beatLengths.append(x)

    print(beatLengths[i])
