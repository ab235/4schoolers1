import register
import login

def main():
	answer = input("Do you want to register or login?")
	while (answer != 'register' and answer != 'login'):
		answer = input("Please enter either 'register' or 'login'.")
	if (answer == 'register'):
		register.main()
	else:
		login.main()

if __name__ == '__main__':
    main()
