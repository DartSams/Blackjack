import random
import mysql.connector



db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Dartagnan18@",
    database="testdatabase"
    )


mycursor=db.cursor(buffered=True)

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
        mycursor.execute(f"UPDATE Blackjack SET money = money * 2 WHERE name = '{name}'")
        db.commit()
    
    elif sum(dealer_hand)>sum(player_hand) and sum(dealer_hand)<21:
        print(f'***Dealer wins with {sum(dealer_hand)}***')
        mycursor.execute(f"UPDATE Blackjack SET money = money / 2 WHERE name = '{name}'")
        db.commit()

    elif sum(player_hand)==21:
        print('***Player has BLACKJACK***')
        mycursor.execute(f"UPDATE Blackjack SET money = money * 2 WHERE name = '{name}'")
        db.commit()

    elif sum(dealer_hand)==21:
        print('***Dealer has BLACKJACK***')
        mycursor.execute(f"UPDATE Blackjack SET money = money / 2 WHERE name = '{name}'")
        db.commit()

    elif sum(player_hand)==sum(dealer_hand):
        print('***PUSH***')

    elif sum(player_hand)>21:
        print('***Player Bust***')
        mycursor.execute(f"UPDATE Blackjack SET money = money / 2 WHERE name = '{name}'")
        db.commit()

    elif sum(dealer_hand)>21:
        print('***Dealer Bust***')
        mycursor.execute(f"UPDATE Blackjack SET money = money * 2 WHERE name = '{name}'")
        db.commit()
    


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
        mycursor.execute(f"UPDATE Blackjack SET money = money * 2 WHERE name = '{name}'")
        db.commit()
        # another_game()
    elif sum(dealer_hand)==21:
        print('Dealer has BLACKJACK')
        # another_game()
        mycursor.execute(f"UPDATE Blackjack SET money = money * 2 WHERE name = '{name}'")
        db.commit()


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




# player()
# dealer()
# check_win()
# while game:
    # chips.bet()
    # print(f'Player hand is: {sum(player_hand)}')
    # # print(f'Dealer hand is: {sum(dealer_hand)}')
    # # check_win()
    # # player_hand.clear()
    # # dealer_hand.clear()
    # x=input('Would you like to hit or stand (1/0)? ')
    # if x=='1':
    #     hit()
    # elif x=='0':
    #     print('\nDealer has:')
    #     dealer_has()
    #     # print('Dealer drew')
    #     dealer_hit()
    #     stand()
    #     player_hand.clear()
    #     dealer_hand.clear()
    #     # another_game()
    #     next_game=input('Would you like to play another game (1/0)? ')
    #     if next_game=='1':
    #         player_hand.clear()
    #         dealer_hand.clear()
    #         player()
    #         dealer()
    #         # check_win()
    #     else:
    #         print('Thanks for playing')
    #         game=False








##check for blackjack before hit/stand 
##add betting system
##dealer draws cards based on how many times player hit(drew)
##dealer hidden card

print('For commands type (/help)')
help_=input('What would you like to do: ').lower()

if help_=='/help':
    print('/sign in')
    print('/create account')
    print('/rules')    
    print('/delete')

if help_=='/sign in':
    name=input('Name please: ')
    mycursor.execute(f"SELECT * FROM Blackjack WHERE name = '{name}'")
    for i in mycursor:
        print(i)

elif help_=='/create account':
    name=input('Name please: ')
    mycursor.execute("INSERT INTO Blackjack (name,money) VALUES (%s,%s)", (name,100))
    db.commit()

elif help_=='/rules':
    print("""
The goal of the game blackjack also called 21 is to have a higher hand than the dealer and be below 21
but if your hand is equal to 21 then you immediately win.

    ***Ex. Player drew:
    eight of Diamonds
    ten of Hearts

    Dealer drew:
    five of Hearts
    hidden card***

In this scenario the player wins.

If the player and dealer's hand are tied this is called a push.

    ***Ex. Player drew:
    eight of Diamonds
    seven of Hearts

    Dealer drew:
    five of Hearts
    ten of clubs***

in this scenario the player and dealer hand's are tied

During the game phase you are aloud to do 2 things such as hit or stand
if you choose to hit the dealer will deal another card to the player.


But if you choose to stand this ends the round and the dealer will 
draw (x) amount of times the player drew a card it reveals the dealer's hand
and checks who is closer to 21 or has 21.""")

elif help_=='/delete':
    name=input('Please enter username: ')
    mycursor.execute(f"DELETE FROM Blackjack WHERE name = '{name}'")
    db.commit()


elif help_=='/play':
    name=input('PLease enter your username: ')
    player()
    dealer()
    while game:
        print(f'Player hand is: {sum(player_hand)}')
        x=input('Would you like to hit or stand (1/0)? ')
        if x=='1':
            hit()
        elif x=='0':
            print('Dealer has:')
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


