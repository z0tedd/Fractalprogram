
import random
import turtle
import tkinter
from tkinter import *
stack2 = []
def clicked(): #создание кнопки
    btn.configure(text="Кнопка нажата!!")
    h = int(cio.get())
    det = int(hio.get())
    p= int(uio.get())
    uuuuu = int(uuio.get())
    rule1 = str(yui.get())
    start = str(rio.get())
    yshit = str(jojo.get())
    if cia.get() == True:
        rnd = 1
        rule2 = 1
    elif ((cia.get()) == False) and p>=2:
        rnd = 3
        rule=str(tui.get())
    else:
        rnd = 0
        rule2 =str(tui.get())
    if (aio.get()) == True:
        lft=1
    else:
        lft=int(dio.get())
    if (bio.get()) == True:
        rgt=1
    else:
        rgt=int(eio.get())
    window.destroy()
    stack2.append((h,rgt,lft,det,p,uuuuu,rule1,rule2,rnd,start,yshit))
    return stack2

def textbat(tex, colum, ro, tias): #Создание надписей
    lbl = Label(window, text=tex)
    lbl.grid(column=int(colum), row=int(ro))
    txt = Entry(window,width=25, state=tias)
    txt.grid(column= int(colum+1), row=int(ro))
    return txt
def chkadd(ji, jo,tex): #создание галочки
    chk_state = BooleanVar()
    chk_state.set(False)
    chk = Checkbutton(window, text= tex, var=chk_state)
    chk.grid(column=ji, row=jo)
    return chk_state

def chain(start): #создание правила
    leng = ''
    bank['F'] = rule1
    bank['Y'] = yshit
    for guuu in range(p):
        if rnd == 1:
            bank['X']+=bank2[random.randint(1,3)]
        elif rule2 == '1':
            bank['X']= bank2[1]
            if rnd ==3:
                bank['X']+=bank2[random.randint(1,3)]
        elif rule2 == '2':
            bank['X'] = bank2[2]
            if rnd ==3:
                bank['X']+=bank2[random.randint(1,3)]
        elif rule2 == '3':
            bank['X'] = bank2[3]
            if rnd ==3:
                bank['X']+=bank2[random.randint(1,3)]
        else:
            bank['X']=bank2[4]
            if rnd ==3:
                bank['X']+=bank2[random.randint(1,4)]
            
    for d in range(det):
        for a in start:
            leng+=bank[a]
        start = leng
        leng = ''
    print(bank['X'])
    print(bank['Y'])
    return start

stack=[] #рисование
def draw(lft,rgt,h):
    for a in start:
        if a == 'F':
            turtle.forward(h)
        elif a == '-':
            if lft == 1:
                lft=random.randint(-30, -30)
                turtle.left(lft)
            else:
                turtle.left(lft)
        elif a == '[':
            stack.append((turtle.pos(),turtle.heading() ))
        elif a == ']':
            delta,alfa = stack.pop()
            turtle.penup()
            turtle.setheading(alfa)
            turtle.setposition(delta)
            turtle.pendown()
        elif a == '+':
            if rgt == 1:
                rgt=random.randint(-30, 30)
                turtle.right(rgt)
            else:
                turtle.right(rgt)
        elif a == 'X':
            pass
        elif a == 'Y':
            pass
        else:
            print('shit')
            continue
#окно
window = Tk() 
window.title("Добро пожаловать!") 
window.geometry('1000x300')

btn = Button(window, text="Нажми меня", command=clicked)
btn.grid(column=2, row=0)

lbl = Label(window, text='Встроенные правила 1:F[+X]F[-X]+X,/////2:F[+X][-X]FX,/////3:F-[[X]+X]+F[+FX]-')
lbl.grid(column=0, row=10)
lbl = Label(window, text='Если галка рандом стоит, не пишите в окна слева!!!!')
lbl.grid(column=0, row=11)

aio = chkadd(2,1,'random\рандом от - 30 до 30')
bio =chkadd(2,2,'random\рандом от - 30 до 30')
cia =chkadd(2,7, 'random\рандом правила X из встроенных')
trias = 'normal'
cio=textbat('length\Длина линии',0,0,'normal')
dio=textbat('угол\angle градуса при повороте влево',0,1,trias)
eio=textbat('угол\angle градуса при повороте налево',0,2,trias)
hio=textbat('Сколько раз будет повторяться правило\repeting rules',0,3,'normal')
uio=textbat('кол-во разных правил ',0,4,'normal')
uuio=textbat('кол-во деревьев, поставьте 1, чтобы не нагружать компьютер',0,5,'normal')
yui=textbat('правило F',0,6,'normal')
tui=textbat('правило X',0,7,trias)
rio=textbat('старт',0,9,'normal')
jojo=textbat('правило Y', 0,8,'normal')
window.mainloop()

    
turtle.tracer(0)
turtle.penup()
turtle.setposition(0,0)
turtle.pensize(0.5)
turtle.pendown()
bank = {'+':'+','-':'-', '[':'[', ']':']', 'F':'', 'X':'', 'Y':''}
#сама программа
h,rgt,lft,det,p,uuuuu,rule1,rule2,rnd,start,yshit = stack2.pop()
tru = False
bank2 = {1:'F[+X]F[-X]+X',2:'F[+X][-X]FX', 3:'F-[[X]+X]+F[+FX]-X',4:rule2}
for i in range(uuuuu):
    start = chain(start)
    print(start)
    draw(lft,rgt,h)
    turtle.penup()
    turtle.setposition(0,0)
    turtle.pendown()
    turtle.update()
turtle.mainloop()
