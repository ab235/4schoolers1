import csv
import main

def main():
    data = []
    with open('users.csv') as file:
        csv_reader = csv.reader(file, delimiter = ',')
        for row in csv_reader:
            data.append(row)
    friends = []
    with open('friends.csv') as file:
        csv_reader = csv.reader(file, delimiter = ',')
        for row in csv_reader:
            friends.append(row)
    uname = input("Please enter your username: ")
    if (len(data) == 0):
        pswrd = input("Please enter your password: ")
        cnfrmpswrd = input("Please confirm your password: ")
        data += [[uname], [pswrd], [int(0)]]
    elif (uname in data[0]):
        print("User already registered! Sending back to home page...")
        main.main()
    else:
        pswrd = input("Please enter your password: ")
        cnfrmpswrd = input("Please confirm your password: ")
        if (pswrd == cnfrmpswrd):
            if (len(friends) < 2):
                friends = [data[0], [[] for x in range(len(data[0]))]]
            data[0].append(uname)
            data[1].append(pswrd)
            data[2].append(int(0))
            friends[0].append(uname)
            print(uname)
            friends[1].append([])
        else:
            print("Passwords do not match!")
    with open('users.csv', 'w') as file:
        csv_writer = csv.writer(file, delimiter = ',')
        for row in range(len(data)):
            csv_writer.writerow(data[row])
    with open('friends.csv', 'w') as file:
        csv_writer = csv.writer(file, delimiter = ',')
        for row in range(len(friends)):
            csv_writer.writerow(friends[row])
if __name__ == '__main__':
    main()
