from tkinter import *

def celc_to_far():
    try:
        labelOutput.config(text = 9/5*int(entryInput.get())+25)
    except ValueError:
        labelOutput.config(text='Ошибка ввода')
window = Tk()
window.title('tk')
window.geometry('250x150')
labelTitle = Label(text='Температура в Цельсиях:')
labelTitle.pack()
entryInput = Entry(width=30, justify='center')
entryInput.pack(padx=5)
labelOutput = Label(text='')
labelOutput.pack()
btnConvert = Button(text='Конвертировать!', command=celc_to_far)
btnConvert.pack()
btnExit = Button(text='Выход', command= lambda x=window: x.destroy())
btnExit.pack()
window.mainloop()