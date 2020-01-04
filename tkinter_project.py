from tkinter import *
from tkcalendar import Calendar
import sqlite3
import tkinter.messagebox

root=Tk()
root.geometry("800x600")
root.title("Appreciation Today")

title = Label(root,text="Appreciation Today\n(choose today's date)",fg = 'navy blue',width=20,
              font=("Fixedsys", 19,"bold"))
title.pack(side='top')

def exit1():
    exit()

def thank_win(event):
    window = Tk()
    window.geometry("600x400")
    window.title("Thankfulness")
    title = Label(window, text="Write three things you are thankful for", fg='navy blue',
                  font=("Fixedsys", 16, "bold"))
    title.pack(side='top')

    def submit():
        first1 = first_entry.get()
        sec2 = second_entry.get()
        third3 = third_entry.get()
        conn = sqlite3.connect("Thanks.db")
        with conn:
            cursor = conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS Thanks(Date TEXT,First TEXT,Second TEXT, Third TEXT)')
        cursor.execute('INSERT INTO Thanks(Date,First,Second,Third) VALUES(?,?,?,?)',
                       (cal.get_date(), first1, sec2, third3))
        conn.commit()
        tkinter.messagebox.showinfo("Nice Job!", "Your data has been saved to the file, Thanks.db")
        exit1()

    first_label = Label(window, text = '1.', font=("Fixedsys", 15, "bold"), fg='#99ffbb', bg='white')
    first_label.place(x=50,y=75)

    first_entry = Entry(window,font=("Fixedsys", 15), fg='#99ffbb', bg='white',width=47)
    first_entry.place(x=100,y=75)

    sec_label = Label(window, text = '2.', font=("Fixedsys", 15, "bold"), fg='#99ccff', bg='white')
    sec_label.place(x=50,y=150)

    second_entry = Entry(window,font=("Fixedsys", 15), fg='#99ccff', bg='white',width=47)
    second_entry.place(x=100,y=150)

    third_label = Label(window, text = '3.', font=("Fixedsys", 15, "bold"), fg='#c299ff', bg='white')
    third_label.place(x=50,y=225)

    third_entry = Entry(window,font=("Fixedsys", 15), fg='#c299ff', bg='white',width=47)
    third_entry.place(x=100,y=225)

    quit_but = Button(window,text="Quit", width=12, bg='navy blue', fg='white', font = "Fixedsys",
                      command=exit1).place(x=150,y=300)

    save_but = Button(window,text="Save", width=12, bg='navy blue', fg='white', font = "Fixedsys",
                      command=submit).place(x=350,y=300)


cal = Calendar(root, font="Courier 14", locale='en_US',
            cursor="hand2", bordercolor='black', headersbackground='orange', normalbackground='#ffff80',
            weekendbackground='#ffff80',selectbackground='#cccc00')
cal.pack(fill="both", expand=True)
cal.bind('<<CalendarSelected>>', thank_win)

root.mainloop()