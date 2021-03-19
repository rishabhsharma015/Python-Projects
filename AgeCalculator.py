from tkinter import *
from datetime import date
from tkinter import messagebox
root = Tk()
root.geometry("450x670+40+30")
root.title("Age Calculator")


def calculate():
    today = date.today()
    birthdate = date(int(yearentry.get()), int(monthentry.get()), int(dayentry.get()))
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    Label(text="your age is {}".format(age)).grid(row=8, column=4, pady=50)


def permit():
    res = messagebox.askyesnocancel("Confirm", "Are you sure you want to exit?")
    if res == True:
        root.destroy()
    elif res == False:
        pass


Label(root, text="Welcome To Age Calc", bg="black", fg="yellow", font="comicsanms 19 bold").grid(row=1, column=4)
photo = PhotoImage(file="Age.png")
Label(image=photo).grid(row=2, column=4)
Label(text="Name").grid(row=3, column=0)
Label(text="year").grid(row=4, column=0)
Label(text="Month").grid(row=5, column=0)
Label(text="Day").grid(row=6, column=0)


nameValue = StringVar()
yearValue = StringVar()
monthValue = StringVar()
dayValue = StringVar()


nameEntry = Entry(root, textvariable=nameValue)
yearentry = Entry(root, textvariable=yearValue)
monthentry = Entry(root, textvariable=monthValue)
dayentry = Entry(root, textvariable=dayValue)
nameEntry.grid(row=3, column=5, pady=10)
yearentry.grid(row=4, column=5, pady=10)
monthentry.grid(row=5, column=5, pady=10)
dayentry.grid(row=6, column=5, pady=10)


Button(text="Calculate age", command=calculate).grid(row=7, column=4)
Button(text="Quit", command=permit).grid(row=10, column=4)

root.mainloop()
