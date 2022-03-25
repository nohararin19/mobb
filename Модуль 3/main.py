from tkinter import *
from tkinter import messagebox
import tkinter.font as font
import csv



def games_store():
    # создание окна выбора игр
    games = Toplevel(root)
    games.title(my_title)
    games.geometry(my_res)
    games.iconbitmap(my_icon)

    bg = PhotoImage(file='img/games.png')
    canvas1 = Canvas(games, width=1024, height=768)
    canvas1.grid(row=0, column=0)
    canvas1.create_image(0, 0, image=bg, anchor='nw')

    gameFrame = Frame(games)
    gameFrame.grid(row=0, column=0)

    # получение данных с csv файла
    filepath = 'csv/video_games.csv'

    File = open(filepath)
    Reader = csv.reader(File)
    Data = list(Reader)
    del (Data[0])

    list_of_entries = []
    for x in list(range(0, len(Data))):
        list_of_entries.append(Data[x][0])

    var = StringVar(value=list_of_entries)
    listbox1 = Listbox(gameFrame, listvariable=var, heigh=40, width=50)
    listbox1.grid(row=0, column=0, sticky='n')

    def update():   # функция для отоброжения конкретных данных с csv файла
        index = listbox1.curselection()[0]
        namelabel2.config(text=Data[index][0])
        genrelabel2.config(text=Data[index][5])
        publisherlabel2.config(text=Data[index][7])
        pricelabel2.config(text=Data[index][10])

        return None

    def buy():
        acc = Toplevel(root)
        acc.title(my_title)
        acc.geometry('640x480')
        acc.iconbitmap(my_icon)

        Label(acc, text='Войдите в аккаунт').pack()
        Label(acc, text='Логин ').pack()
        e = Entry(acc)
        e.pack()

        def add_user():
            File = open('users.csv', 'a', newline='')
            Writer = csv.writer(File)
            list_of_users = [e.get()]
            Writer.writerow(list_of_users)
            messagebox.showinfo(title='Покупка', message='Поздравляем, товар успешно куплен!')

        Button(acc, text='Войти', command=add_user).pack()

    # меню окна
    button1 = Button(gameFrame, text="Подробнее", command=update).grid(row=5, column=1)
    button2 = Button(gameFrame, text='Купить', command=buy).grid(row=5, column=0)

    namelabel = Label(gameFrame, text="Название")
    genrelabel = Label(gameFrame, text="Жанр")
    publisherlabel = Label(gameFrame, text="Издатель")
    pricelabel = Label(gameFrame, text="Цена (в $)")

    a = 0
    for i in (namelabel, genrelabel, publisherlabel, pricelabel):
        i.grid(row=a + 1, column=0, sticky='w')
        a += 1

    namelabel2 = Label(gameFrame, text="")
    genrelabel2 = Label(gameFrame, text="")
    publisherlabel2 = Label(gameFrame, text="")
    pricelabel2 = Label(gameFrame, text="")

    x = 0
    for i in (namelabel2, genrelabel2, publisherlabel2, pricelabel2):
        i.grid(row=x+1, column=1, sticky='w')
        x += 1

    games.mainloop()


def my_games():
    lib = Toplevel(root)
    lib.title(my_title)
    lib.geometry('640x480')
    lib.iconbitmap(my_icon)

    Label(lib, text='Войдите в аккаунт').pack()
    Label(lib, text='Логин ').pack()
    e = Entry(lib)
    e.pack()

    def show_input():
        myLabel = Label(lib, text=e.get())
        myLabel.pack()

    Button(lib, text='Войти', command=show_input).pack()


def close():
    if messagebox.askyesno('Выход', 'Вы уверены?'):
        root.destroy()


# var
my_title = 'MOBB'
my_res = '1024x768'
my_icon = 'img/mobb.ico'
my_spacebar = 50 * ' '

# main (root) window creation
root = Tk()
root.title(my_title)
root.geometry(my_res)
root.iconbitmap(my_icon)

bg = PhotoImage(file='img/bg.png')
canvas1 = Canvas(root, width=1024, height=768)
canvas1.grid(row=0, column=0)
canvas1.create_image(0, 0, image=bg, anchor='nw')

# creation of the frames
myFrame = Frame(root)
myFrame.grid(row=0, column=0)


# creation of the buttons
myFont = font.Font(family='Helvetica', size=15)

myButton1 = Button(myFrame, text='Выбрать игру', bg='#FFEB3B', padx=59, pady=30,
                   command=games_store)
myButton1['font'] = myFont
myButton1.grid(row=0, column=0)

myButton2 = Button(myFrame, text='  Мои игры     ', bg='#FFEB3B', padx=57, pady=30,
                   command=my_games)
myButton2['font'] = myFont
myButton2.grid(row=1, column=0)

myButton3 = Button(myFrame, text='   Выход           ', bg='#D32F2F', padx=49, pady=30,
                   command=close)
myButton3['font'] = myFont
myButton3.grid(row=2, column=0)
root.mainloop()
