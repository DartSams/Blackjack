import random

class Card:

    def __init__(self,value,rank):
        self.value=value
        self.rank=rank

ace=Card(11,'Ace')
king=Card(10,'King')
queen=Card(10,'Queen')
jack=Card(10,'Jack')
ten=Card(10,'Ten')
nine=Card(9,'Nine')
eight=Card(8,'Eight')
seven=Card(7,'Seven')
six=Card(6,'Six')
five=Card(5,'Five')
four=Card(4,'Four')
three=Card(3,'Three')
two=Card(2,'Two')


class Betting:

    def __init__(self,amount):
        self.amount=amount

    def bet(self):
        print(int(self.amount)*2)
        


y=input('How much would you bet: ')
chips=Betting(y)
# chips.bet()





def hit():
    global num
    num+=1
    print('**************')
    extra=random.choice(lst)
    print(f'You drew a {extra.rank} of {random.choice(type_)}')
    player_hand.append(extra.value)


def adjust_ace():
    if sum(player_hand)>21 and 11 in player_hand:
        player_hand.remove(11)
        player_hand.append(1)
        # print(sum(player_hand))


def stand():
    #redo this its only asking to hit once

    adjust_ace()
    

    if sum(player_hand)>sum(dealer_hand) and sum(player_hand)<21:
        print(f'***Player wins with {sum(player_hand)}***')
    
    elif sum(dealer_hand)>sum(player_hand) and sum(dealer_hand)<21:
        print(f'***Dealer wins with {sum(dealer_hand)}***')

    elif sum(player_hand)==21:
        print('***Player has BLACKJACK***')

    elif sum(dealer_hand)==21:
        print('***Dealer has BLACKJACK***')

    elif sum(player_hand)==sum(dealer_hand):
        print('***PUSH***')

    elif sum(player_hand)>21:
        print('***Player Bust***')

    elif sum(dealer_hand)>21:
        print('***Dealer Bust***')
    


def player():
    print('**************')
    print('Player Drew')
    p1=random.choice(lst)
    p2=random.choice(lst)
    print(f'{p1.rank} of {random.choice(type_)}')
    print(f'{p2.rank} of {random.choice(type_)}\n')
    player_hand.append(p1.value)
    player_hand.append(p2.value)

def dealer():
    global d1,d2
    print('Dealer Drew:')
    d1=random.choice(lst)
    d2=random.choice(lst)
    print(f'{d1.rank} of {random.choice(type_)}')
    print('**HIDDEN CARD**')
    print(('**************\n'))
    # print(f'{d2.rank} of {random.choice(type_)}\n')
    dealer_hand.append(d1.value)
    dealer_hand.append(d2.value)


def check_win():
    if sum(player_hand)==21:
        print('Player has BLACKJACK')
        # another_game()
    elif sum(dealer_hand)==21:
        print('Dealer has BLACKJACK')
        # another_game()


def dealer_has():
    global d1,d2
    print(f'{d1.rank} of {random.choice(type_)}')
    print(f'{d2.rank} of {random.choice(type_)}\n')

def dealer_hit():
    if num>=1:
        for i in range(int(num)):
            print('Dealer drew:')
            print('**************')
            extra=random.choice(lst)
            print(f'Dealer drew a {extra.rank} of {random.choice(type_)}')
            player_hand.append(extra.value)
    else:
        pass

def another_game():
    global game
    next_game=input('Would you like to play another game (1/0)? ')
    if next_game=='1':
        player()
        dealer()
        check_win()
    else:
        print('Thanks for playing')
        game=False





lst=[ace,king,queen,jack,ten,nine,eight,seven,six,five,four,three,two]
type_=['Hearts','Spades','Diamonds','Clubs']
player_hand=[]
dealer_hand=[]
game=True
num=0



player()
dealer()
while game:
    print(f'Player hand is: {sum(player_hand)}')
    x=input('Would you like to hit or stand (1/0)? ')
    if x=='1':
        hit()
    elif x=='0':
        dealer_has()
        dealer_hit()
        stand()
        player_hand.clear()
        dealer_hand.clear()
        game=False
        again=input('Would you like to play again (1/0)? ')
        if again=='1':
            game=True
            player_hand.clear()
            dealer_hand.clear()
            player()
            dealer()
        elif again=='0':
            game=False