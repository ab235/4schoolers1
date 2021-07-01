import csv
import main

def main():
    data = []
    with open('users.csv') as file:
        csv_reader = csv.reader(file, delimiter = ',')
        for row in csv_reader:
            data.append(row)
    uname = input("Please enter your username: ")
    pswrd = input("Please enter your password: ")
    cnfrmpswrd = input("Please confirm your password: ")
    if (pswrd == cnfrmpswrd):
        if (len(data) > 0):
            if (uname not in data[0]):
                data[0].append(uname)
                data[1].append(pswrd)
            else:
                print("User already registered! Sending back to home page...")
                master.main()
        else:
            data += [[uname], [pswrd]]
    else:
        print("Passwords do not match!")
    with open('users.csv', 'w') as file:
        csv_writer = csv.writer(file, delimiter = ',')
        for row in data:
            csv_writer.writerow(data[0])
            csv_writer.writerow(data[1])
if __name__ == '__main__':
    main()
