import random

songFile = open('songs.txt', 'r')
songs = songFile.readlines()

shuffledSongs = []
for index in range(len(songs)):
	randomSongIndex = random.randint(0, len(songs) - 1)
	selectedSong = songs[randomSongIndex]
	shuffledSongs.append(selectedSong.rstrip())
	songs.remove(selectedSong)

with open('songs_shuffled.txt', 'w+') as fileOut:
	fileOut.write('\n'.join(shuffledSongs))