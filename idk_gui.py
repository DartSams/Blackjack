from tkinter import *
import random
import mysql.connector
from PIL import ImageTk,Image



db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Dartagnan18@",
    database="testdatabase"
    )

mycursor=db.cursor(buffered=True)
player_origin=155
dealer_origin=160
dealer_draw=0
dealer_hand=[]
player_hand=[]

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
    global user1,passw1,user2,passw2,sign_enter,sign,create,create_user2,create_passw2,save,user2,del1,del2
    del1=True
    sign.grid_forget()
    create.grid_forget()

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

def add_to_db():
    global user1,passw1,user2,passw2,sign_enter,sign,create,create_user2,create_passw2,save,user2,del1,del2
    print(create_user2.get())
    print(create_passw2.get())
    create_user2.delete(0,END)
    create_passw2.delete(0,END)

    # mycursor.execute("INSERT INTO Blackjack (name,password,money) VALUES (%s,%s,%s)", (create_user2.get(),create_passw2.get(),100))
    # db.commit()

def sign_in():
    global bj
    print(passw2.get())
    mycursor.execute(f"SELECT * FROM Blackjack WHERE password = '{passw2.get()}'")
    for i in mycursor:
        print(i)

    user1.grid_forget()
    passw1.grid_forget()
    user2.grid_forget()
    passw2.grid_forget()
    sign_enter.grid_forget()

    bj=Button(root,text='Blackjack',command=lambda: start_bj())
    bj.grid(row=3,column=0,columnspan=10)


def start_bj():
    root.geometry('894x381')
    welcome1.grid_forget()
    welcome2.grid_forget()
    bj.grid_forget()


    canvas=Canvas(root,background='green')
    canvas.create_line(0,5, 160, 5,width=10)
    canvas.create_line(160,0, 160, 381,width=10)
    canvas.create_line(0,376, 160, 376,width=10)
    canvas.create_line(160,120, 892, 121,width=10)
    canvas.create_line(160,270, 892, 269,width=10)
    canvas.pack(fill = BOTH, expand = True)

    hit=Button(root,text='Hit Me',font=('Florent',10),command=lambda: player_hit())
    hit.place(x=55,y=55)

    stand=Button(root,text='Stand',font=('Florent',10))
    stand.place(x=57,y=180)

    double=Button(root,text='Double Down',font=('Florent',10))
    double.place(x=40,y=300)

    dealer_num=Label(root,background='green',font=('Florent',20),text="Dealer's hand: ")
    dealer_num.place(x=170,y=130)

    player_num=Label(root,background='green',font=('Florent',20),text="PLayer's hand: ")
    player_num.place(x=170,y=223)

    win_lose=Label(root,background='green',text='PLayer blackjack',font=('Florent',50))
    win_lose.place(x=350,y=160)

    dealer_hit()
    dealer_hit()

    player_hit()
    player_hit()

def player_hit():
    global player_origin,dealer_draw,dealer_origin
    dealer_draw+=1
    player_origin+=15
    extra=random.choice(card_nums)
    suite=random.choice(card_values)

    load=Image.open(rf"C:\Users\godof\PycharmProjects\PythonProjects\GitHub\Blackjack\{extra.name}.png")
    card=ImageTk.PhotoImage(load)

    img=Label(image=card)
    img.image=card
    img.place(x=player_origin,y=278)

def dealer_hit():
    global player_origin,dealer_draw,dealer_origin
    dealer_draw+=1
    dealer_origin+=15
    extra=random.choice(card_nums)
    suite=random.choice(card_values)

    load=Image.open(rf"C:\Users\godof\PycharmProjects\PythonProjects\GitHub\Blackjack\{extra.name}.png")
    card=ImageTk.PhotoImage(load)

    img=Label(image=card)
    img.image=card
    img.place(x=dealer_origin,y=10)

def close_all():
    global user1,passw1,user2,passw2,sign_enter,sign,create,create_user2,create_passw2,save,user2,del1,del2
    # if del1==True:
    #     user1.grid_forget()
    #     passw1.grid_forget()
    #     user2.grid_forget()
    #     passw2.grid_forget()
    #     sign_enter.grid_forget()
    #     del1=False

    # elif del2==True:
    #     user1.grid_forget()
    #     passw1.grid_forget()
    #     create_user2.grid_forget()
    #     create_passw2.grid_forget()
    #     save.grid_forget()
    #     del2=False

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

# exit=Button(root,text='Exit',command=lambda: close_all())
# exit.grid(row=5,column=10)

# x=random.choice(num)
# y=random.choice(suite)
# card=ImageTk.PhotoImage(Image.open(rf"C:\Users\godof\PycharmProjects\PythonProjects\GitHub\Blackjack\{x} of {y}.png"))
# label=Label(image=card)
# label.place(x=550,y=200)

root.mainloop()