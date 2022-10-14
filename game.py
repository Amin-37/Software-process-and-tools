import random
choices = ["1", "2", "3"]

class game(object):
    def rock_paper_scissor(self, choice, computer_choice):
        if choice == computer_choice:
            return 'Draw'
        elif choice == "1":
            if computer_choice == "3":
                return 'True'
            else:
                return 'False'
        elif choice == "2":
            if computer_choice == "1":
                return 'True'
            else:
                return 'False'
        elif choice == "3":
            if computer_choice == "2":
                return 'True'
            else:
                return 'False'

    def play_game(self):
        print('Options - \n1.Rock\n2.Paper\n3.Scissor')
        rounds_wins_lose = [0,0,0]
        while True:
            computer = random.choice(choices)
            if rounds_wins_lose[1] == 5 or rounds_wins_lose[2] == 5:
                if rounds_wins_lose[1] == 5:
                    print('Congrats! You won the game!')
                    print('You have played', rounds_wins_lose[0], 'times to get 5 points')
                    break
                else:
                    print('Congrats to computer, computer has won the game!')
                    print('Computer played', rounds_wins_lose[0], 'times to get 5 points')
                    break
            user_choice = input("Enter your choice:(Q to quit or R to restart the game) ")
            if user_choice in choices:
                rounds_wins_lose[0] += 1
                game = self.rock_paper_scissor(user_choice, computer)
                if game == 'True':
                    print('You Won')
                    rounds_wins_lose[1] += 1
                if game == 'False':
                    print('Computer won')
                    rounds_wins_lose[2] += 1
                if game == 'Draw':
                    print('Its a Draw')
            elif user_choice.upper() == 'Q':
                print('Exited program')
                break
            elif user_choice.upper() == 'R':
                print('Restarted ----------------')
                rounds_wins_lose = [0, 0, 0]
                print('Restart game!!.. ')
            else:
                print('Invalid ', end='')
                continue
