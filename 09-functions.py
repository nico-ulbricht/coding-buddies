def greeting(name):
	print('Hello ' + name)

def isDivisibleByThree(number):
	return number/3 == int(number/3)

def isPalindrome(inputText):
	convertedText = inputText.lower().replace(' ', '')

	reversedText = convertedText[::-1]
	return reversedText == convertedText

greeting('Nico') # prints 'Hello Nico'
print(isDivisibleByThree(9)) # prints True
print(isDivisibleByThree(7)) # prints False
print(isPalindome('Anna')) # prints True
print(isPalindome('Nico is cool')) # prints False