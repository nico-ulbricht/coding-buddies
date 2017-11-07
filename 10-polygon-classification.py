# INPUT  
polygons = [
	[1, 2, 3],
	[2, 2, 2, 2],
	[2, 4, 2, 4],
	[5, 6, 3],
	[2, 4, 3, 4],
]


# OUTPUT
def isTriangle(polygon):
	sizeCount = len(polygon)
	return sizeCount == 3

def isRectangle(polygon):
	if len(polygon) != 4:
		return False

	return polygon[0] == polygon[2] and polygon[1] == polygon[3]

def isSquare(polygon):
	if len(polygon) != 4:
		return False

	return polygon[0] == polygon[1] == polygon[2] == polygon[3]


for polygon in polygons:
	print(polygon)
	if isTriangle(polygon) == True:
		print('TRIANGLE')
	elif isSquare(polygon) == True:
		print('SQUARE')
	elif isRectangle(polygon) == True:
		print('RECTANGLE')
	else:
		print('I DUNNO')

