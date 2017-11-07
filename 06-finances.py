# INPUT  
expenses = [
    { 'month':'August', 'name':'Sunglasses', 'cost': 30},
    { 'month':'May', 'name':'iPhone', 'cost': 600 },
    { 'month':'September', 'name':'Jacket', 'cost': 89.958878 },
    { 'month':'September', 'name':'Shirt', 'cost': 19.99 },
    { 'month':'May', 'name':'iPhone Insurance', 'cost': 15.5 },
]


# PROGRAM
whichMonth = input('which month? ')
for expense in expenses:
	if expense['month'] == whichMonth:
		print(expense['name'])