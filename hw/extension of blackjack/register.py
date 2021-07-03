import csv
import main

def main():
    data = []
    with open('users.csv') as file:
        csv_reader = csv.reader(file, delimiter = ',')
        for row in csv_reader:
            data.append(row)
    uname = input("Please enter your username: ")
    if (uname in data[0]):
        print("User already registered! Sending back to home page...")
        main.main()
    pswrd = input("Please enter your password: ")
    cnfrmpswrd = input("Please confirm your password: ")
    if (pswrd == cnfrmpswrd):
        if (len(data) > 0):
            data[0].append(uname)
            data[1].append(pswrd)
            data[2].append(0)
        else:
            data += [[uname], [pswrd], [0]]
    else:
        print("Passwords do not match!")
    with open('users.csv', 'w') as file:
        csv_writer = csv.writer(file, delimiter = ',')
        for row in data:
            csv_writer.writerow(data[0])
            csv_writer.writerow(data[1])
            csv_writer.writerow(data[2])
if __name__ == '__main__':
    main()
