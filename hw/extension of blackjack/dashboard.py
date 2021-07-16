import csv

def add_friend(index):
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
    if (len(friends) < 2):
        friends = [data[0], [[] for x in range(len(data[0]))]]
    ans = input("Please enter the username of your friend: ")
    while (ans not in data[0] and ans not in friends[1][index]):
        ans = input("Please enter a non-friended username: ")
    print(type(friends[1][index]))
    friends[1][index].append([ans])
    with open('friends.csv', 'w') as file:
        csv_writer = csv.writer(file, delimiter = ',')
        for row in range(len(list(friends))):
            csv_writer.writerow(friends[row])

def view_friends(index):
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
    if (len(friends) < 2):
        friends = [data[0], [[] for x in range(len(data[0]))]]
    return friends[1][index]

def view_friends_money(index):
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
    if (len(friends) < 2):
        friends = [data[0], [[] for x in range(len(data[0]))]]
    ans = input("Which friend? Please enter the username of a friend. ")
    if (ans not in friends[1][index]):
        print("Sorry, you cannot view this person's money.")
        return [0, "Username not found"]
    else:
        dex = data[0].index(ans)
        return [data[2][dex], ans]
    

def main(index):
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
    if (len(friends) < 2):
        friends = [data[0], [[] for x in range(len(data[0]))]]
    ans = input ("Would you like to view your money? (y/n): ")
    while (ans != 'y' and ans != 'n'):
        ans = input("Please enter 'y' or 'n' for yes or no, respectively. ")
    if ans == 'y':
        print("Money: " + str(data[2][index]))
    ans = input("Would you like to deposit money? (y/n): ")
    while (ans != 'y' and ans != 'n'):
        ans = input("Please enter 'y' or 'n' for yes or no, respectively. ")
    if ans == 'y':
        ans = int(input("Please enter the amount you would like to deposit: "))
        while not (ans > 0):
            ans = int(input("Please enter a positive integer: "))
        data[2][index] = int(data[2][index])
        data[2][index] += ans
        print("You now have: " + str(data[2][index]))
    ans = input("Would you like to withdraw money? (y/n): ")
    while (ans != 'y' and ans != 'n'):
        ans = input("Please enter 'y' or 'n' for yes or no, respectively. ")
    if ans == 'y':
        ans = int(input("Please enter the amount you would like to withdraw: "))
        while not (ans > 0):
            ans = int(input("Please enter a positive integer: "))
        data[2][index] = int(data[2][index])
        data[2][index] -= ans
        print("You now have: " + str(data[2][index]))
    ans = input("Would you like to change your password? (y/n): ")
    while (ans != 'y' and ans != 'n'):
        ans = input("Please enter 'y' or 'n' for yes or no, respectively. ")
    if ans == 'y':
        nwpswrd = input("Please enter a new password: ")
        conf_nwpswrd = input("Please confirm new password: ")
        if (nwpswrd == conf_nwpswrd):
            data[1][index] = nwpswrd
            print("Password changed.")
        else:
            ans = input("Passwords do not match. Press q to quit or any other key to try again.")
            if (ans == 'q'):
                pass
            else:
                main()
    with open('users.csv', 'w') as file:
        csv_writer = csv.writer(file, delimiter = ',')
        for row in range(len(data)):
            csv_writer.writerow(data[row])

