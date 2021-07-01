import csv

def main(index):
    data = []
    with open('users.csv') as file:
        csv_reader = csv.reader(file, delimiter = ',')
        for row in csv_reader:
            data.append(row)
    ans = input("Would you like to see all users? (y/n): ")
    while (ans != 'y' and ans != 'n'):
        ans = input("Please enter 'y' or 'n' for yes or no, respectively. ")
    if ans == 'y':
        print("Users: " + str(data[0]))
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
    print("Good day.")

