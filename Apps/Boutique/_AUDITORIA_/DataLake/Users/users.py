import csv

FIELDS = ['id', 'first_name', 'last_name', 'email', 'password']

USERS = []

# CSV IMPORTATION
with open('_users.csv', newline='\n') as csvfile:

    reader = csv.reader(csvfile, delimiter=',')

    reader.__next__() # Skip header
   
    for row in reader:

        u = {}

        u["id"] = row[0]
        u["first_name"] = row[1]
        u["last_name"] = row[2]
        u["email"] = row[3]
        u["password"] = row[4]

        USERS.append ( u )

# CSV EXPORTATION - DATA FRAME
with open('users.csv', 'w') as csvfile:

	writer = csv.DictWriter (csvfile, fieldnames = FIELDS)
	
	writer.writeheader()

	writer.writerows(USERS)
