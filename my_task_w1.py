from tkinter import *
import sqlite3
def clicked(cursor, move):
    if move == 1:
        Name = entryName.get()
        Category = entryCategory.get()
        Date = entryTime.get()
        if Name and Category and Date:
            cursor.execute("INSERT INTO tasks(id, category, name, time) VALUES(NULL,?,?,?)", (Category,Name,Date))
    if move == 3: 
        window.destroy()
def btnPassage(passage, move):
    c = sqlite3.connect('tasks.db')
    cursor = c.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS tasks(id INTEGER PRIMARY KEY, category TEXT, name TEXT, time TEXT)")
    clicked(cursor, move)
    c.commit()
    c.close()

window = Tk()
window.title('Менеджер задач')

frame = Frame(window)

lblName = Label(frame, text='Задача: ')
lblName.grid(column=0,row=0)
entryName = Entry(frame, width=27)
entryName.grid(column=1,row=0)

lblCategory = Label(frame, text='Категория: ')
lblCategory.grid(column=0,row=1)
entryCategory = Entry(frame, width=27)
entryCategory.grid(column=1,row=1)

lblTime = Label(frame, text='Время:')
lblTime.grid(column=0,row=2)
entryTime = Entry(frame, width=27)
entryTime.grid(column=1,row=2 )

btn = Button(frame, text='Заказать')
btn.grid(column=1,row=3)

btnSp = Button(frame, text='Список задач')
btnSp.grid(column=1,row=4)

btnExit = Button(frame, text='Выход')
btnExit.grid(column=1,row=5)

frame.grid(column=0,row=0)

btn.bind('<Button-1>',lambda passage, x=1: btnPassage(passage, x))
btnSp.bind('<Button-1>', lambda passage, x=2: btnPassage(passage, x))
btnExit.bind('<Button-1>', lambda passage, x=3: btnPassage(passage, x))

window.mainloop()