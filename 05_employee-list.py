# INPUT
employees = [
	{ "name": "Nico", "department": "engineering" },
	{ "name": "Goscha", "department": "engineering" },
	{ "name": "Nina", "department": "ops" },
	{ "name": "Francois", "department": "sales" },
	{ "name": "Bastian", "department": "ops" },
	{ "name": "Emily", "department": "pops" },
	{ "name": "Tomasz", "department": "product" }
]


# CODE
department = input('Which department? ')
for employee in employees:
	if department == employee["department"]:
		print(employee["name"])