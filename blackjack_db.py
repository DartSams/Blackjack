import mysql.connector
from config import *

db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=passwd,
    database="testdatabase"
    )


mycursor=db.cursor(buffered=True)

# mycursor.execute("CREATE TABLE Blackjack (name VARCHAR(50),password VARCHAR(50), money int UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)")

# for i in range(5):
#     x=input('Name please: ')

#     mycursor.execute("INSERT INTO Blackjack (name,money) VALUES (%s,%s)", (x,100))
# db.commit()

# mycursor.execute('SELECT name FROM Blackjack')



###create acc
# x=input('Name please: ')
# mycursor.execute("INSERT INTO Blackjack (name,password,money) VALUES (%s,%s,%s)", ('dart','passw',100))
# db.commit()

###sign in
# y=input('Name please: ')
# mycursor.execute(f"SELECT * FROM Blackjack WHERE name = '{y}'")

###delete entries
# mycursor.execute("DELETE FROM Blackjack WHERE money > 1")
# db.commit()


# mycursor.execute(f"UPDATE Blackjack SET money = money / 2 WHERE name = '{y}'")
# db.commit()
# mycursor.execute(f"SELECT * FROM Blackjack WHERE name = '{y}'")
mycursor.execute('SELECT * FROM Blackjack')
for i in mycursor:
    print(i)


###delete a table
# mycursor.execute("DROP TABLE Blackjack")
# db.commit()