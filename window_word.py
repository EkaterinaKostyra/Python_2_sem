from tkinter import *
from tkinter import messagebox as mb
import requests
from bs4 import BeautifulSoup
import random

spisok = []
url = 'https://lifehacker.ru/200-essential-english-words/'
resp = requests.get(url)
soup = BeautifulSoup(resp.content, features="html.parser")
words = soup.findAll('li')
for word in words:
    if '\n' not in word:
        spisok.append(word.text)

spisok = ''.join(spisok).replace(';',' — ').replace('.',' — ').split(' — ')
russianWords = spisok[1::2]
englishWords = spisok[0::2]
voc = dict(zip(englishWords, russianWords)) 

def checkAnswer():
    if entryTranslate.get().lower() == voc[rndWord.get()]:
        mb.showinfo('Победа','Вы угадали слово!')
        rndWord.set(random.choice(list(voc.keys())))
        entryTranslate.delete(0, END)
    else:
        mb.showerror('Проигрыш', f'Перевод не правильный!\nПравильное значение: {voc[rndWord.get()]}')
        rndWord.set(random.choice(list(voc.keys())))
        entryTranslate.delete(0, END)

window = Tk()
window.title('tk')
rndWord = StringVar()
rndWord.set(random.choice(list(voc.keys()))) 
labelTitle = Label(window, text='Случайное слово: ')
labelTitle.pack()
labelWord = Label(window, textvariable=rndWord)
labelWord.pack()
labelTranslate = Label(window, text='Укажите перевод: ')
labelTranslate.pack()
entryTranslate = Entry(window, width=40)
entryTranslate.pack(padx=5)
btnAnswer = Button(window, text='Готово!', command=checkAnswer)
btnAnswer.pack()
btnExit = Button(text='Выход', command=lambda x=window: x.destroy())
btnExit.pack()
window.mainloop()