import csv
import main
import dashboard



def main():
    data = []
    with open('users.csv') as file:
        csv_reader = csv.reader(file, delimiter = ',')
        for row in csv_reader:
            data.append(row)
    uname = input("Please enter your username: ")
    pswrd = input("Please enter your password: ")
    entry = False
    if (len(data) == 0):
        print("Database empty.")
    else:
        if (uname in data[0]):
            dex = data[0].index(uname)
            if (pswrd == data[1][dex]):
                print("Login successful. Transferring to dashboard...")
                dashboard.main(dex)
                entry = True
            else:
                ans = input("Login unsuccessful. Press q to quit or any other key to try again. ")
                if (ans == 'q'):
                    print("Good day.")
                else:
                    main()
        else:
            print("Username not in database. Please register and try again.")
    return [uname, pswrd, data[2][dex], dex, entry]
if __name__ == '__main__':
    main()
