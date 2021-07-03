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
    if (len(data) == 0):
        print("Database empty.")
    else:
        if (uname in data[0]):
            dex = data[0].index(uname)
            if (pswrd == data[1][dex]):
                print("Login successful. Transferring to dashboard...")
                dashboard.main(dex)
                return dex
            else:
                ans = input("Login unsuccessful. Press q to quit or any other key to try again. ")
                if (ans == 'q'):
                    print("Good day.")
                else:
                    main()
        else:
            print("Username not in database. Please register and try again. Transferring you back to home page...")
            main.main()
            
if __name__ == '__main__':
    main()
