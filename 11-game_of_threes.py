import sys


DEBUG = True

def debug(text):
	if DEBUG == True:
		print(text)

def isDivisibleByThree(number):
	return number / 3 == int(number / 3)

def gameOfThrees(number):
	number = int(number)
	if isDivisibleByThree(number) == True:
		debug(str(number) + ' ' + '0')
		return number / 3
	elif isDivisibleByThree(number + 1) == True:
		debug(str(number) + ' ' + '1')
		return (number + 1) / 3
	else:
		debug(str(number) + ' ' + '-1')
		return (number - 1) / 3


startNumber = int(sys.argv[1])
workingNumber = startNumber

while workingNumber != 1:
	workingNumber = gameOfThrees(workingNumber)

debug(workingNumber)