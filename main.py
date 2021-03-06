import hashlib
from tkinter import *
from mysql import connector

class App(Tk):

    def __init__(self):
        super().__init__()
        self.username = StringVar(value="Bob")
        self.password = StringVar(value="localhost:3000")

        frame1 = Frame(self)
        frame2 = Frame(self)
        frame3 = Frame(self)
        frame4 = Frame(self)

        frame1.pack(side=TOP)
        frame2.pack(side=TOP)
        frame3.pack(side=TOP)
        frame4.pack(side=TOP)

        Label(frame1, text="Username:", font=("Arial", 15), padx=5,pady=5).pack(side=LEFT)
        Entry(frame1, width=50, textvariable=self.username).pack(side=LEFT)

        Label(frame2, text="Password:", font=("Arial", 15), padx=5, pady=5).pack(side=LEFT)
        Entry(frame2, width=50, textvariable=self.password, show="*").pack(side=LEFT)
        
        Button(frame3, text="Login", command=self.login, font=("Arial", 15), padx=5, pady=5).pack(side=LEFT)
        Button(frame3, text="Register", command=self.register, font=("Arial", 15), padx=5, pady=5).pack(side=LEFT) 

        self.statusLabel = Label(frame4, text="status label", font=("Arial", 15), padx=5, pady=5)
        self.statusLabel.pack(side=LEFT)

        self.connect_sql()

    def connect_sql(self):
        self.mydb = connector.connect(
        host="192.168.0.21",
        port="3306",
        user="programski_dostop",
        password="programsko_geslo",
        database="PB_Login"
        )
        
        self.cursor = self.mydb.cursor()

    def status(self, status_text):
        self.statusLabel.config(text=status_text)

    def login(self):
        self.status("logging in")
        if self.check_user_exist(self.username.get()):
            self.cursor.execute("SELECT id FROM users WHERE name = %s AND pass = %s;", (self.username.get(), hashlib.sha256(self.password.get().encode()).hexdigest()))
            if self.cursor.fetchall():
                self.status("Logged in")
            else:
                self.status("Invalid password")
        else:
            self.status("User does not exist")


    def register(self):
        self.status("registering...")
        if self.cursor:
            if self.check_user_exist(self.username.get()):
                self.status("User allready exists")
                return
            self.cursor.execute("INSERT INTO users VALUES (NULL, %s, %s)", (self.username.get(),hashlib.sha256(self.password.get().encode()).hexdigest()))
            self.mydb.commit()
            self.status("Sucsessfuly registered")

    def check_user_exist(self, user : str):
        self.cursor.execute("SELECT * FROM users WHERE name=%s", (user,))
        if self.cursor.fetchall():
            return True
        return False

if __name__ == "__main__":

    app = App()
    app.mainloop()

    

    


    # CREATE TABLE `pb_login`.`users` ( `id` INT NOT NULL AUTO_INCREMENT , `name` VARCHAR(255) NOT NULL , `pass` VARCHAR(32) NOT NULL , PRIMARY KEY (`id`)) ENGINE = InnoDB;
    