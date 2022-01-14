import tkinter
from mysql import connector

class App(tkinter.Tk):
    def test(self):
        print("Hello world")

if __name__ == "__main__":

    app = App()

    app.test()

    mydb = connector.connect(
    host="localhost",
    user="",
    password=""
    )

    print(mydb) 