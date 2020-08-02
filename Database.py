import sqlite3

def userTable():
    connection = sqlite3.connect("userLogin.db")
    connection.execute("CREATE TABLE Employees(USERNAME TEXT NOT NULL, EMAIL TEXT, PASSWORD TEXT )")
   # connection.execute("INSERT INTO Employees VALUES (?,?,?)",('admin','josh@gmail','admin'))

    connection.commit()

    connection.close()



