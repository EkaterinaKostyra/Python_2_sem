from tkinter import *
import os
def clicked(task1,task2,move):
    if move == 1: 
        Name = entryName.get()
        Category = entryCategory.get()
        Date = entryTime.get()
        if Name and Category and Date:
            task2.write(f"Задача: {Name} Категория: {Category} Дата: {Date}")    
    if  move == 2:
        txt.config(state=NORMAL)
        txt.delete(1.0, END)
        txt.insert(END,''.join(task1).strip())
        txt.config(state=DISABLED)
    if  move == 3: 
        window.destroy()
def btnPassage(pasage,  move):
    if os.path.exists('task_list.json'): 
        with open("task_list.json", 'r', encoding='utf8') as in_file, open("task_list.json", 'a',encoding='utf8') as out_file:
            clicked(in_file.read(), out_file, move)
    else:
        with open("task_list.json", 'w', encoding='utf8') as out_file:
            clicked("", out_file, move)

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
entryTime.grid(column=1,row=2)

btn = Button(frame, text='Заказать')
btn.grid(column=1,row=3)

btnSp = Button(frame, text='Список задач')
btnSp.grid(column=1,row=4)

btnExit = Button(frame, text='Выход')
btnExit.grid(column=1,row=5)
frame.grid(column=0,row=0)

scroll = Scrollbar(window, orient=VERTICAL)
scroll.grid(column=2,row=0)
txt = Text(window, yscrollcommand=scroll.set, width=35,height=9)
txt.grid(column=1, row=0)
scroll.config(command=txt.yview)

btn.bind('<Button-1>',lambda passage, x=1: btnPassage(passage, x))
btn.bind('<Button-1>', lambda passage, x=2: btnPassage(passage, x))
btnExit.bind('<Button-1>', lambda passage, x=3: btnPassage(passage, x))

window.mainloop()