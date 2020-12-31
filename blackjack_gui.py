from tkinter import *
import random
import mysql.connector
from PIL import ImageTk,Image
import sys
from config import *
import os


db=mysql.connector.connect(
    host= ip,
    user="root",
    passwd=passwd,
    database="testdatabase"
    )

#Variables
mycursor=db.cursor(buffered=True)
player_origin=155
dealer_origin=175
dealer_draw=0
dealer_hand=[]
player_hand=[]
stand_stat=False
double_down_stat=False
dirname=os.path.dirname(__file__)

#card class with properties of a name and number value
class Card:

    def __init__(self,name,value):
        self.name=name
        self.value=value

#the 4 types of cards
card_types=['clubs','spades','hearts','diamonds']

#13 cards with a name,random card type from the list of card types,and has a numeric value 2-11
ace=Card(f'ace of {random.choice(card_types)}',11)
two=Card(f'two of {random.choice(card_types)}',2)
three=Card(f'three of {random.choice(card_types)}',3)
four=Card(f'four of {random.choice(card_types)}',4)
five=Card(f'five of {random.choice(card_types)}',5)
six=Card(f'six of {random.choice(card_types)}',6)
seven=Card(f'seven of {random.choice(card_types)}',7)
eight=Card(f'eight of {random.choice(card_types)}',8)
nine=Card(f'nine of {random.choice(card_types)}',9)
ten=Card(f'ten of {random.choice(card_types)}',10)
jack=Card(f'jack of {random.choice(card_types)}',10)
queen=Card(f'queen of {random.choice(card_types)}',10)
king=Card(f'king of {random.choice(card_types)}',10)

#list of cards to draw later
card_nums=[ace,two,three,four,five,six,seven,eight,nine,ten,jack,queen,king]

#
def signup():
    global user1,passw1,user2,passw2,sign_enter,sign,create,create_user2,create_passw2,save,user2,del1,del2,test
    del1=True

    close_all()

    test=Label(root,text='Sign in Please',background='green',font=('Florent',50))
    test.grid(row=0,column=0,columnspan=10)

    user1=Label(root,background='green',text='Username:',font=('Florent',15))
    user1.grid(row=3,column=0,padx=50)
    passw1=Label(root,background='green',text='Password:',font=('Florent',15))
    passw1.grid(row=4,column=0,padx=50)

    user2=Entry(root)
    user2.grid(row=3,column=1)
    passw2=Entry(root)
    passw2.grid(row=4,column=1)

    sign_enter=Button(root,text='Enter',background='green',command=lambda: sign_in())
    sign_enter.grid(row=5,column=1)

#function to create account then saves the username and password to the mysql database everyaccount starts with $100
def create_account():
    global user1,passw1,user2,passw2,sign_enter,sign,create,create_user2,create_passw2,save,user2,del1,del2
    del2=True
    sign.grid_forget()
    create.grid_forget()

    user1=Label(root,background='green',text='Username:',font=('Florent',15))
    user1.grid(row=3,column=0,padx=50)
    passw1=Label(root,background='green',text='Password:',font=('Florent',15))
    passw1.grid(row=4,column=0,padx=50)

    create_user2=Entry(root)
    create_user2.grid(row=3,column=1)
    create_passw2=Entry(root)
    create_passw2.grid(row=4,column=1)

    save=Button(root,text='Save',background='green',command=lambda: add_to_db())
    save.grid(row=5,column=1)

    exit_=Button(root,text='Exit',command=lambda:after_create_acc())
    exit_.grid(row=5,column=2)
    
#after creating account and clicking saves this function starts the sign up function
def after_create_acc():
    global user1,passw1,user2,passw2,sign_enter,sign,create,create_user2,create_passw2,save,user2,del1,del2,test
    close_all()

    test=Label(root,text='Sign in Please',background='green',font=('Florent',50))
    test.grid(row=0,column=0,columnspan=10)

    signup()

#after creating an account this saves the username and password to the databse and gives that account a starting balance of $100
def add_to_db():
    global user1,passw1,user2,passw2,sign_enter,sign,create,create_user2,create_passw2,save,user2,del1,del2
    print(create_user2.get())
    print(create_passw2.get())
    
    mycursor.execute("INSERT INTO Blackjack (name,password,money) VALUES (%s,%s,%s)", (create_user2.get(),create_passw2.get(),100))
    db.commit()

    create_user2.delete(0,END)
    create_passw2.delete(0,END)

def sign_in():
    global bj,test
    print(passw2.get())
    mycursor.execute(f"SELECT * FROM Blackjack WHERE password = '{passw2.get()}' AND name = '{user2.get()}'")
    for i in mycursor:
        print(i)

    close_all()
    games=Label(root,text='Select a game',background='green',font=('Florent',50))
    games.grid(row=0,column=0,columnspan=10)
    bj=Button(root,text='Blackjack',command=lambda: start_bj())
    bj.grid(row=3,column=0,columnspan=10)

#starts the blackjack game 
def start_bj():
    global player_origin,dealer_draw,dealer_origin,stand_stat,player_num,dealer_num,hit,stand,double,img,load,card,test
    
    #makes the window bigger
    root.geometry('894x381')
    close_all()

    #creates the lines that section off the buttons,dealer and player hand's, and the dealer and player total using 4 coordinates the x and y postions are the top left of whats being drawn and then the next 2 coordinates which tells how far to draw the line and how thick
    canvas=Canvas(root,background='green')
    canvas.create_line(0,5, 160, 5,width=10)
    canvas.create_line(160,0, 160, 381,width=10)
    canvas.create_line(0,376, 160, 376,width=10)
    canvas.create_line(160,120, 892, 121,width=10)
    canvas.create_line(160,270, 892, 269,width=10)
    canvas.pack(fill = BOTH, expand = True)

    hit=Button(root,text='Hit Me',font=('Florent',10),command=lambda: player_hit())
    hit.place(x=55,y=55)

    stand=Button(root,text='Stand',font=('Florent',10),command=lambda: player_stand())
    stand.place(x=57,y=180)

    double=Button(root,text='Double Down',font=('Florent',10),command=lambda: double_down())
    double.place(x=40,y=300)

    dealer_num=Label(root,background='green',font=('Florent',20),text="Dealer's hand: ")
    dealer_num.place(x=170,y=130)

    player_num=Label(root,background='green',font=('Florent',20),text="PLayer's hand: ")
    player_num.place(x=170,y=223)

    
    dealer_hit()
    dealer_hidden()

    #initially deals 2 cards to the player and adds them to a list to be totalled up later
    for i in range(2):

        #every time the player draw's a card the player origin (top left of card) coordinate increases by 15 so the cards arent covering each other and makes that number the new card origin
        player_origin+=15

        #chooses random number from the card_nums list then matches it to that card
        extra=random.choice(card_nums)
        #chooses random card type from card_types list
        suite=random.choice(card_types)

        load=Image.open(fr'{dirname}\blackjack_cards\{extra.name}.png')
        card=ImageTk.PhotoImage(load)

        img=Label(image=card)
        img.image=card
        img.place(x=player_origin,y=278)
        player_hand.append(extra.value)
    
    update_text()

#deals another card to the player
def player_hit():
    global player_origin,dealer_draw,dealer_origin,stand_stat,img
    #each time the player chooses to hit a counter is added to the dealer so the dealer will also draw a card according to the counter
    dealer_draw+=1
    #the player origin (top left of card) increases by 15 so they arent overlapping
    player_origin+=15
    extra=random.choice(card_nums)
    suite=random.choice(card_types)

    load=Image.open(fr'{dirname}\blackjack_cards\{extra.name}.png')
    card=ImageTk.PhotoImage(load)

    img=Label(image=card)
    img.image=card
    img.place(x=player_origin,y=278)
    player_hand.append(extra.value)

    update_text()

#deals another card to dealer
def dealer_hit():
    global player_origin,dealer_draw,dealer_origin,stand_stat,img
    dealer_origin+=15
    extra=random.choice(card_nums)
    suite=random.choice(card_types)

    load=Image.open(fr'{dirname}\blackjack_cards\{extra.name}.png')
    card=ImageTk.PhotoImage(load)

    img=Label(image=card)
    img.image=card
    img.place(x=dealer_origin,y=10)
    dealer_hand.append(extra.value)

    update_text()
    
#deals a face down card to the dealer to be hidden from the player
def dealer_hidden():
    global player_origin,dealer_draw,dealer_origin,stand_stat,img,dirname
    #the dealer origin (top left of card) increases by 15 so they arent overlapping
    dealer_origin+=15
    extra=random.choice(card_nums)
    suite=random.choice(card_types)

    #if player hasnt chose to stand then the dealer's hidden card will stay face down
    if stand_stat==False:
        load=Image.open(fr'{dirname}\blackjack_cards\hidden card.jpg')
        card=ImageTk.PhotoImage(load)

        img=Label(image=card)
        img.image=card
        img.place(x=dealer_origin,y=10)
        stand_stat=False
    
    #but if the player has chose to stand the dealer's face down card is deleted and a new card with a numeric value and type is drawn
    else:
        load=Image.open(fr'{dirname}\blackjack_cards\{extra.name}.png')
        card=ImageTk.PhotoImage(load)

        img=Label(image=card)
        img.image=card
        img.place(x=dealer_origin-15,y=10)
        dealer_hand.append(extra.value)

#ends the player's ability to draw cards
def player_stand():
    global player_origin,dealer_draw,dealer_origin,stand_stat,img
    stand_stat=True
    dealer_hidden()
    #deals a new card to the dealer from the counter of how many times the player has drawn
    if dealer_draw>=1:
        for i in range(int(dealer_draw)):
            dealer_hit()
    print(int(dealer_draw))
    print(sum(player_hand))

    check_21()
    update_text()
    
    #redefining the the variables for the next game so the cards dont appear off screen
    player_origin=155
    dealer_origin=175
    dealer_draw=0
    stand_stat=False
    double_down_stat=False

#function to deal 1 final card to the player and puts them in stand
def double_down():
    double_down_stat=True
    player_hit()
    player_stand()

#updates the text of the player and dealer's hands to display the sum of each hand
def update_text():
    player_num.configure(text=f"PLayer's hand: {sum(player_hand)}")
    print(player_hand)
    dealer_num.configure(text=f"Dealer's hand: {sum(dealer_hand)}")
    print(dealer_hand)

#adjust for ace of both hands if the total of a hand is above 21 and if their is a ace card then is sets the value of the ace to 1
def adjust_ace():
    if sum(player_hand)>21 and player_hand.count(11)>0:
        player_hand.remove(11)
        player_hand.append(1)

    if sum(dealer_hand)>21 and dealer_hand.count(11)>0:
        dealer_hand.remove(11)
        dealer_hand.append(1)

    print('player total: '+str(sum(player_hand)))

#after the player has chosen to stand this checks who has the higher total and is below 21
def check_21():
    adjust_ace()

    #if the player has a higher total and below 21 they win and their money is doubled
    if sum(player_hand)>sum(dealer_hand) and sum(player_hand)<21:
        print(f'***Player wins with {sum(player_hand)}***')
        win_lose=Label(root,background='green',text='PLayer wins',font=('Florent',30))
        win_lose.place(x=450,y=160)
        mycursor.execute(f"UPDATE Blackjack SET money = money * 2 WHERE password = '{passw2.get()}'")
        db.commit()
        #before the player chose to stand if they chose to double down and the player has a higher total and below 21 their money is doubled for a total of being quadrupled
        if double_down_stat==True:
            mycursor.execute(f"UPDATE Blackjack SET money = money * 2 WHERE password = '{passw2.get()}'")
            db.commit()
    
    elif sum(dealer_hand)>sum(player_hand) and sum(dealer_hand)<21:
        print(f'***Dealer wins with {sum(dealer_hand)}***')
        win_lose=Label(root,background='green',text='Dealer wins',font=('Florent',30))
        win_lose.place(x=450,y=160)
        mycursor.execute(f"UPDATE Blackjack SET money = money / 2 WHERE password = '{passw2.get()}'")
        db.commit()
        
    #if the player'stotal equal to a perfect 21 the player wins
    elif sum(player_hand)==21:
        print('***Player has BLACKJACK***')
        win_lose=Label(root,background='green',text='Player has BLACKJACK',font=('Florent',30))
        win_lose.place(x=450,y=160)
        mycursor.execute(f"UPDATE Blackjack SET money = money * 2 WHERE password = '{passw2.get()}'")
        db.commit()
        #before the player chose to stand if they chose to double down and the player has a higher total and below 21 their money is doubled for a total of being quadrupled
        if double_down_stat==True:
            mycursor.execute(f"UPDATE Blackjack SET money = money * 2 WHERE password = '{passw2.get()}'")
            db.commit()
    #if the dealer's total hand is 21 then the player's money is divided by 21
    elif sum(dealer_hand)==21:
        print('***Dealer has BLACKJACK***')
        win_lose=Label(root,background='green',text='Dealer has BLACKJACK',font=('Florent',30))
        win_lose.place(x=450,y=160)
        mycursor.execute(f"UPDATE Blackjack SET money = money / 2 WHERE password = '{passw2.get()}'")
        db.commit()

    #if the player and dealer's total hands are tied then its a PUSH and the player keeps their original amount of money
    elif sum(player_hand)==sum(dealer_hand):
        print('***PUSH***')
        win_lose=Label(root,background='green',text='Push',font=('Florent',30))
        win_lose.place(x=450,y=160)

    elif sum(player_hand)>21:
        print('***Player Bust***')
        win_lose=Label(root,background='green',text='PLayer Bust',font=('Florent',30))
        win_lose.place(x=450,y=160)
        mycursor.execute(f"UPDATE Blackjack SET money = money / 2 WHERE password = '{passw2.get()}'")
        db.commit()

    #if player and dealer's total hands are over 21 then they both BUST the player keeps their original amount of money
    elif sum(player_hand)>21 and sum(dealer_hand)>21:
        print('***Both Bust***')
        win_lose=Label(root,background='green',text='Both Bust',font=('Florent',30))
        win_lose.place(x=450,y=160)
        
    #if dealer's hand is above 21 and the player's hand is below 21 the the player wins and gets their money doubled
    elif sum(dealer_hand)>21 and sum(player_hand)<21:
        print('***PLayer wins***')
        win_lose=Label(root,background='green',text='Player Wins',font=('Florent',30))
        win_lose.place(x=450,y=160)
        mycursor.execute(f"UPDATE Blackjack SET money = money * 2 WHERE password = '{passw2.get()}'")
        db.commit()
        #before the player chose to stand if they chose to double down and the player has a higher total and below 21 their money is doubled for a total of being quadrupled
        if double_down_stat==True:
            mycursor.execute(f"UPDATE Blackjack SET money = money * 2 WHERE password = '{passw2.get()}'")
            db.commit()
    
    ending()

#at the end of the game the buttons hit,stand,and double down are removed and replaced with the buttons new game and quit
def ending():
    hit.place_forget()
    stand.place_forget()
    double.place_forget()

    new_game=Button(root,text='New Game',command=lambda: game_again())
    new_game.place(x=55,y=55)


    quit_=Button(root,text='Quit',command=lambda: sys.exit())
    quit_.place(x=70,y=300)

#if the player chose to start a new game the the previos total of the player and dealer's hand are erased
def game_again():
    player_hand.clear()
    dealer_hand.clear()
    

    for widget in root.winfo_children():
        widget.place_forget()
        widget.pack_forget()

    #resets the stand variable back to false so the function player_stand doesnt automatically start
    stand_stat=False
    start_bj()

#function to clear everything in the window 
def close_all():
    global user1,passw1,user2,passw2,sign_enter,sign,create,create_user2,create_passw2,save,user2,del1,del2
    for widget in root.winfo_children():
        widget.grid_forget()
        widget.pack_forget()
        widget.place_forget()



root=Tk()
root.title('Blackjack')
#sets the background of the window to be green
root.configure(background='green')

#opening welcome label
welcome1=Label(root,text='Welcome to',background='green',font=('Florent',50))
welcome2=Label(root,text="Dart's Casino",background='green',font=('Florent',50))
welcome1.grid(row=0,column=0,columnspan=10)
welcome2.grid(row=1,column=0,columnspan=10)

#when run 2 buttons appear sign up or create account
sign=Button(root,text='Sign In',background='green',font=('Florent',15),command=lambda:signup())
sign.grid(row=3,column=0,columnspan=10)
create=Button(root,text='Create Account',background='green',font=('Florent',15),command=lambda: create_account())
create.grid(row=4,column=0,columnspan=10)


root.mainloop()