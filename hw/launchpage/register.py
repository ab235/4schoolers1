import csv
import main

def main():
	data = []
	with open('Students.csv') as file:
    	csv_reader = csv.reader(file, delimiter = ',')
    	for row in csv_reader:
        	data.append(row)
	uname = input("Please enter your username: ")
	pswrd = input("Please enter your password: ")
	cnfrmpswrd = input("Please confirm your password: ")
	if (pswrd == cnfrmpswrd):
		if (user not in data[0]):
			data[0].append(user)
			data[1].append(pswrd)
		else:
			print("User already registered! Sending back to home page...")
			main.main()
	else:
		print("Passwords do not match!")
if __name__ == '__main__':
    main()