from cgitb import strong
from distutils.command.config import config
from email.mime import image
from gc import freeze
import imp
from re import A
import tkinter as tk
from tkinter.ttk import Label
from ast import Div
from cProfile import label
from cgitb import text
from mimetypes import common_types
from msilib.schema import ComboBox
from tkinter import*
import tkinter.ttk as ttk
from turtle import  back, width
import keyboard
from PIL import ImageTk
root = tk.Tk()
root.title("Setting")
root.config(background="#2e2e2e")
root.resizable(False,False)
cho = ImageTk.PhotoImage(file='C:/Users/we202/Documents/GitHub/Picture/head1.ico', master=root)
checki = ImageTk.PhotoImage(file='C:/Users/we202/Documents/GitHub/YBCP/image/check.jpg')
wrong = ImageTk.PhotoImage(file='C:/Users/we202/Documents/GitHub/YBCP/image/wrong.png')
root.iconphoto(True, cho)
root.geometry('300x200+1100+500')


#항시 작동하는 기능 
#키 입력시 해당키 출력
def onKeyPress(event):
    global text
    a = event.char
    text.config(text='You pressed %s\n' % (a, ))
    #저장된 콤보박스값과 키보드입력값 대조
    if (ch1 == str(a)):
        checking.config(text="correct",image=checki)
          
    else:
      checking.config(text="wrong", image=wrong)
      
      
      
#벨류값 추출
def inse():
 e.configure(text=combobox.get())
 b.config(text=select_var.get())
#save 새로운창 생성
def newpage():
    win = Toplevel(root)
    win.geometry("200x70+1150+550")
    win.title("System")
    re=Label(win, text=select_var.get()+'+'+combobox.get())
    re.pack()
    end = Button(win, width=10,text="ok", command=win.destroy).pack()
#콤보박스 값 저장
def save():
    global ch1
    global ch2
    ch1 = combobox.get()
    ch2 = select_var.get()
    
dfe=Label(root,background="#2e2e2e")
dfe.pack()
#콤보박스 생성
val = [str(i) for i in range(0, 10)]
combobox = ttk.Combobox(root, height=10, values=val, state="readonly")
combobox.pack()
#라디오버튼 ctrl alt 생성
select_var = StringVar()
btn1 = Radiobutton(root, text="Ctrl", value="Ctrl" ,  variable=select_var, fg="#FFFFFF" ,bg="#2e2e2e")
btn1.config(background="#2e2e2e")
btn2 = Radiobutton(root, text="Alt", value="Alt", variable=select_var, fg="#FFFFFF", bg="#2e2e2e")
btn2.config(background="#2e2e2e")
btn1.pack()
btn2.pack()
#save 버튼 생성
btn3 = Button(root, text="Save",command=lambda:[inse(), newpage(), save()])
btn3.config(background="#2e2e2e", fg="#FFFFFF")
btn3.pack()
#키 확인 레이블
e = Label(root, fg="#FFFFFF")
e.config(background="#2e2e2e")
e.pack()
b = Label(root, fg="#FFFFFF") 
b.config(background="#2e2e2e")
b.pack()

text = Label(root, text="press any key", fg="#FFFFFF")
text.config(background="#2e2e2e")
text.place(x=110,y=140)   

checking = Label(root, fg="#FFFFFF")
checking.config(background="#2e2e2e")
checking.place(x=-10, y=190)

root.bind('<KeyPress>', onKeyPress)
root.mainloop()