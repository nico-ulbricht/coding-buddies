import random
import sys

inputFile = open('songs.txt', 'r')
inputSongs = inputFile.readlines() # array
outputSongs = [] # array

for index in range(len(inputSongs)):
	randomIndex = random.randint(0, len(inputSongs) - 1)
	pickedSong = inputSongs[randomIndex]

	sanitizedSong = pickedSong.replace('\n', '')
	outputSongs.append(sanitizedSong)
	inputSongs.remove(pickedSong)

fileName = sys.argv[1]
outputFile = open(fileName, 'w')
outputFile.write('\n'.join(outputSongs))


open
readlines
write
join