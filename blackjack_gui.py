from tkinter import *
import random
import mysql.connector
from PIL import ImageTk,Image
import sys
from config import *



db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=passwd,
    database="testdatabase"
    )

mycursor=db.cursor(buffered=True)
player_origin=155
dealer_origin=175
dealer_draw=0
dealer_hand=[]
player_hand=[]
stand_stat=False
double_down_stat=False

class Card:

    def __init__(self,name,value):
        self.name=name
        self.value=value

card_values=['clubs','spades','hearts','diamonds']

ace=Card(f'ace of {random.choice(card_values)}',11)
two=Card(f'two of {random.choice(card_values)}',2)
three=Card(f'three of {random.choice(card_values)}',3)
four=Card(f'four of {random.choice(card_values)}',4)
five=Card(f'five of {random.choice(card_values)}',5)
six=Card(f'six of {random.choice(card_values)}',6)
seven=Card(f'seven of {random.choice(card_values)}',7)
eight=Card(f'eight of {random.choice(card_values)}',8)
nine=Card(f'nine of {random.choice(card_values)}',9)
ten=Card(f'ten of {random.choice(card_values)}',10)
jack=Card(f'jack of {random.choice(card_values)}',10)
queen=Card(f'queen of {random.choice(card_values)}',10)
king=Card(f'king of {random.choice(card_values)}',10)

card_nums=[ace,two,three,four,five,six,seven,eight,nine,ten,jack,queen,king]




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
    

def after_create_acc():
    global user1,passw1,user2,passw2,sign_enter,sign,create,create_user2,create_passw2,save,user2,del1,del2,test
    close_all()

    test=Label(root,text='Sign in Please',background='green',font=('Florent',50))
    test.grid(row=0,column=0,columnspan=10)

    signup()

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
    mycursor.execute(f"SELECT * FROM Blackjack WHERE password = '{passw2.get()}'")
    for i in mycursor:
        print(i)

    close_all()
    games=Label(root,text='Select a game',background='green',font=('Florent',50))
    games.grid(row=0,column=0,columnspan=10)
    bj=Button(root,text='Blackjack',command=lambda: start_bj())
    bj.grid(row=3,column=0,columnspan=10)


def start_bj():
    global player_origin,dealer_draw,dealer_origin,stand_stat,player_num,dealer_num,hit,stand,double,img,load,card,test
 
    root.geometry('894x381')
    close_all()

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

    for i in range(2):
        player_origin+=15
        extra=random.choice(card_nums)
        suite=random.choice(card_values)

        load=Image.open(rf"C:\Users\godof\VSCodeProjects\GitHub\Blackjack\blackjack cards\{extra.name}.png")
        card=ImageTk.PhotoImage(load)

        img=Label(image=card)
        img.image=card
        img.place(x=player_origin,y=278)
        player_hand.append(extra.value)
    
    update_text()

def player_hit():
    global player_origin,dealer_draw,dealer_origin,stand_stat,img
    dealer_draw+=1
    player_origin+=15
    extra=random.choice(card_nums)
    suite=random.choice(card_values)

    load=Image.open(rf"C:\Users\godof\VSCodeProjects\GitHub\Blackjack\blackjack cards\{extra.name}.png")
    card=ImageTk.PhotoImage(load)

    img=Label(image=card)
    img.image=card
    img.place(x=player_origin,y=278)
    player_hand.append(extra.value)

    update_text()


def dealer_hit():
    global player_origin,dealer_draw,dealer_origin,stand_stat,img
    dealer_origin+=15
    extra=random.choice(card_nums)
    suite=random.choice(card_values)

    load=Image.open(rf"C:\Users\godof\VSCodeProjects\GitHub\Blackjack\blackjack cards\{extra.name}.png")
    card=ImageTk.PhotoImage(load)

    img=Label(image=card)
    img.image=card
    img.place(x=dealer_origin,y=10)
    dealer_hand.append(extra.value)

    update_text()
    

def dealer_hidden():
    global player_origin,dealer_draw,dealer_origin,stand_stat,img
    dealer_origin+=15
    extra=random.choice(card_nums)
    suite=random.choice(card_values)

    if stand_stat==False:
        load=Image.open(rf"C:\Users\godof\VSCodeProjects\GitHub\Blackjack\blackjack cards\hidden card.jpg")
        card=ImageTk.PhotoImage(load)

        img=Label(image=card)
        img.image=card
        img.place(x=dealer_origin,y=10)
        stand_stat=False
    
    else:
        load=Image.open(rf"C:\Users\godof\VSCodeProjects\GitHub\Blackjack\blackjack cards\{extra.name}.png")
        card=ImageTk.PhotoImage(load)

        img=Label(image=card)
        img.image=card
        img.place(x=dealer_origin-15,y=10)
        dealer_hand.append(extra.value)


def player_stand():
    global player_origin,dealer_draw,dealer_origin,stand_stat,img
    stand_stat=True
    dealer_hidden()
    if dealer_draw>=1:
        for i in range(int(dealer_draw)):
            dealer_hit()
    print(int(dealer_draw))
    print(sum(player_hand))

    check_21()
    update_text()
    
    
    player_origin=155
    dealer_origin=175
    dealer_draw=0
    stand_stat=False
    double_down_stat=False

def double_down():
    double_down_stat=True
    player_hit()
    player_stand()

def update_text():
    player_num.configure(text=f"PLayer's hand: {sum(player_hand)}")
    print(player_hand)
    dealer_num.configure(text=f"Dealer's hand: {sum(dealer_hand)}")
    print(dealer_hand)


def adjust_ace():
    if sum(player_hand)>21 and player_hand.count(11)>0:
        player_hand.remove(11)
        player_hand.append(1)

    if sum(dealer_hand)>21 and dealer_hand.count(11)>0:
        dealer_hand.remove(11)
        dealer_hand.append(1)

    print('player total: '+str(sum(player_hand)))


def check_21():
    adjust_ace()

    if sum(player_hand)>sum(dealer_hand) and sum(player_hand)<21:
        print(f'***Player wins with {sum(player_hand)}***')
        win_lose=Label(root,background='green',text='PLayer wins',font=('Florent',30))
        win_lose.place(x=450,y=160)
        mycursor.execute(f"UPDATE Blackjack SET money = money * 2 WHERE password = '{passw2.get()}'")
        db.commit()
        if double_down_stat==True:
            mycursor.execute(f"UPDATE Blackjack SET money = money * 2 WHERE password = '{passw2.get()}'")
            db.commit()
    
    elif sum(dealer_hand)>sum(player_hand) and sum(dealer_hand)<21:
        print(f'***Dealer wins with {sum(dealer_hand)}***')
        win_lose=Label(root,background='green',text='Dealer wins',font=('Florent',30))
        win_lose.place(x=450,y=160)
        mycursor.execute(f"UPDATE Blackjack SET money = money / 2 WHERE password = '{passw2.get()}'")
        db.commit()
        

    elif sum(player_hand)==21:
        print('***Player has BLACKJACK***')
        win_lose=Label(root,background='green',text='Player has BLACKJACK',font=('Florent',30))
        win_lose.place(x=450,y=160)
        mycursor.execute(f"UPDATE Blackjack SET money = money * 2 WHERE password = '{passw2.get()}'")
        db.commit()
        if double_down_stat==True:
            mycursor.execute(f"UPDATE Blackjack SET money = money * 2 WHERE password = '{passw2.get()}'")
            db.commit()

    elif sum(dealer_hand)==21:
        print('***Dealer has BLACKJACK***')
        win_lose=Label(root,background='green',text='Dealer has BLACKJACK',font=('Florent',30))
        win_lose.place(x=450,y=160)
        mycursor.execute(f"UPDATE Blackjack SET money = money / 2 WHERE password = '{passw2.get()}'")
        db.commit()

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

    
    elif sum(player_hand)>21 and sum(dealer_hand)>21:
        print('***Both Bust***')
        win_lose=Label(root,background='green',text='Both Bust',font=('Florent',30))
        win_lose.place(x=450,y=160)
        
    elif sum(dealer_hand)>21 and sum(player_hand)<21:
        print('***PLayer wins***')
        win_lose=Label(root,background='green',text='Player Wins',font=('Florent',30))
        win_lose.place(x=450,y=160)
        mycursor.execute(f"UPDATE Blackjack SET money = money * 2 WHERE password = '{passw2.get()}'")
        db.commit()
    
    ending()


def ending():
    hit.place_forget()
    stand.place_forget()
    double.place_forget()

    new_game=Button(root,text='New Game',command=lambda: game_again())
    new_game.place(x=55,y=55)


    quit_=Button(root,text='Quit',command=lambda: sys.exit())
    quit_.place(x=70,y=300)


def game_again():
    player_hand.clear()
    dealer_hand.clear()
    

    for widget in root.winfo_children():
        widget.place_forget()
        widget.pack_forget()

    stand_stat=False
    start_bj()


def close_all():
    global user1,passw1,user2,passw2,sign_enter,sign,create,create_user2,create_passw2,save,user2,del1,del2
    for widget in root.winfo_children():
        widget.grid_forget()
        widget.pack_forget()
        widget.place_forget()



root=Tk()
root.title('Blackjack')
root.configure(background='green')

welcome1=Label(root,text='Welcome to',background='green',font=('Florent',50))
welcome2=Label(root,text="Dart's Casino",background='green',font=('Florent',50))
welcome1.grid(row=0,column=0,columnspan=10)
welcome2.grid(row=1,column=0,columnspan=10)


sign=Button(root,text='Sign In',background='green',font=('Florent',15),command=lambda:signup())
sign.grid(row=3,column=0,columnspan=10)
create=Button(root,text='Create Account',background='green',font=('Florent',15),command=lambda: create_account())
create.grid(row=4,column=0,columnspan=10)


root.mainloop()