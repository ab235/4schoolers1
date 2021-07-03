import csv

def add_friend(index):
    with open('users.csv') as file:
        csv_reader = csv.reader(file, delimiter = ',')
        for row in csv_reader:
            data.append(row)
    with open('friends.csv') as file:
        csv_reader = csv.reader(file, delimiter = ',')
        for row in csv_reader:
            friends.append(row)
    ans = input("Please enter the username of your friend: ")
    while (ans not in data[0] and ans not in friends[1][index]):
            ans = input("Please enter a non-friended username: ")
    friends[1][index] += ans

def view_friends(index):
    with open('friends.csv') as file:
        csv_reader = csv.reader(file, delimiter = ',')
        for row in csv_reader:
            friends.append(row)
    return friends[1][index]

def view_friends_money(index):
    with open('users.csv') as file:
        csv_reader = csv.reader(file, delimiter = ',')
        for row in csv_reader:
            data.append(row)
    with open('friends.csv') as file:
        csv_reader = csv.reader(file, delimiter = ',')
        for row in csv_reader:
            friends.append(row)
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
    with open('friends.csv') as file:
        csv_reader = csv.reader(file, delimiter = ',')
        for row in csv_reader:
            friends.append(row)
    if (len(friends) == 0):
        friends.append([data[0], [[] for x in range(len(data[0]))]])
    ans = input("Would you like to deposit money? (y/n): ")
    while (ans != 'y' and ans != 'n'):
        ans = input("Please enter 'y' or 'n' for yes or no, respectively. ")
    if ans == 'y':
        ans = int(input("Please enter the amount you would like to deposit: "))
        while (ans > 0):
            ans = int(input("Please enter a positive integer: "))
        data[2][index] += ans
    ans = input("Would you like to withdraw money? (y/n): ")
    while (ans != 'y' and ans != 'n'):
        ans = input("Please enter 'y' or 'n' for yes or no, respectively. ")
    if ans == 'y':
        ans = int(input("Please enter the amount you would like to withdraw: "))
        while (ans > 0):
            ans = int(input("Please enter a positive integer: "))
        data[2][index] -= ans
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
        for row in data:
            csv_writer.writerow(data[0])
            csv_writer.writerow(data[1])
            csv_writer.writerow(data[2])
    print("Good day.")

