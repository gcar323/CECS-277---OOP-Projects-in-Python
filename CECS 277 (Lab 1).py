# Three Card Monte
import math
import random
import check_input 

balance = 100
cards = '''+-----+ +-----+ +-----+
|     | |     | |     | 
|  1  | |  2  | |  3  |
|     | |     | |     |
+-----+ +-----+ +-----+'''

def check_bet(balance):
    x = check_input.get_int_range('How much you wanna bet? ' , 1 , balance)
    return x 
def check_placement():
    x = random.randint(1,3)
    if x == 1:
        print('''+-----+ +-----+ +-----+
|     | |     | |     | 
|  Q  | |  K  | |  K  |
|     | |     | |     |
+-----+ +-----+ +-----+''')
        return 1
    elif x == 2:
        print('''+-----+ +-----+ +-----+
|     | |     | |     | 
|  K  | |  Q  | |  K  |
|     | |     | |     |
+-----+ +-----+ +-----+''')
        return 2
    elif x == 3:
        print('''+-----+ +-----+ +-----+
|     | |     | |     | 
|  K  | |  K  | |  Q  |
|     | |     | |     |
+-----+ +-----+ +-----+''')
        return 3
        
# main
print(f"""-Three card Monte-
Find the queen to double your bet!

You have ${balance}""")
again = True
while balance > 0 and again == True:
    to_gamble = check_bet(balance)
    print(cards)
    queen_guess = int(input("Find the queen: "))
    queen_placement = check_placement()
    if queen_guess == queen_placement:
        print('You got lucky this time...')
        balance = balance + to_gamble
        again = check_input.get_yes_no('Play again? (Y/N): ')
    else:
        print('Sorry... you lose')
        balance = balance - to_gamble
        if balance == 0:
            again = False
        else:
            again = check_input.get_yes_no('Play again? (Y/N): ')
    if balance > 0:
        print(f"\nYou have ${balance}")
    else:
        print("You're out of money. Beat it loser!")
print(f'You have ${balance}')










