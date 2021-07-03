from blackjack import Card, Deck, Player, Game
import register
import login
import dashboard
# player pays $100 to play a game
# they get $500 if sum = 21
# they get $300 if sum = 20
# they get $200 if sum = 19
# they get $150 if sum = 18
# they get $50 if sum = 17
# they get $10 if sum = 16



def main():
    answer = input("Do you want to register or login?: ")
    while (answer != 'register' and answer != 'login'):
        answer = input("Please enter either 'register' or 'login'. ")
    if (answer == 'register'):
        register.main()
    loginlist = login.main()
    player = Player(loginlist[0])
    player.money = loginlist[2]
    new_game = True
    ans = input("Would you like to view friends? (y/n): ")
    while (ans != 'y' and ans != 'n'):
        ans = input("Please enter 'y' or 'n' for yes or no, respectively. ")
    if ans == 'y':
        print("Friends: " + str(dashboard.view_friends(loginlist[3])))
    ans = input("Would you like to add a friend? (y/n): ")
    while (ans != 'y' and ans != 'n'):
        ans = input("Please enter 'y' or 'n' for yes or no, respectively. ")
    if ans == 'y':
        dashboard.add_friend(loginlist[3])
    ans = 'y'
    while (ans != 'n'):
        ans = input("Would you like to add another friend? (y/n): ")
        while (ans != 'y' and ans != 'n'):
            ans = input("Please enter 'y' or 'n' for yes or no, respectively. ")
        if ans == 'y':
            dashboard.add_friend(loginlist[3])
    ans = input("Would you like to view a friend's money? (y/n)")
    while (ans != 'y' and ans != 'n'):
        ans = input("Please enter 'y' or 'n' for yes or no, respectively. ")
    if ans == 'y':
        lis = view_friends_money(loginlist[3])
        print(str(lis[1]) + "'s money: " + str(lis[0]))
    while (new_game):
        game = Game(player)
        next_card = True
        while (next_card):
            game_continue = game.turn()
            if (not game_continue):
                break


            x = input('Do you want to take a card (y/n): ')
            if (x == 'n' or x=='N' or x=='no' or x=='NO'):
                next_card = False
    
        payoff = game.stop()
        print('You won: $' + str(payoff))
        print('You know have $' + str(player.money))
        
        x = input('do you want to play another game (y/n): ')
        if (x == 'n' or x=='N' or x=='no' or x=='NO'):
            new_game = False

    print('Thank you for visiting 4Schoolers BlackJack')
    print('You now have: $' + str(player.money))



if __name__ == '__main__':
    main()
