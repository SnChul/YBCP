from cgitb import text
from mimetypes import common_types
from msilib.schema import ComboBox
from tkinter import*
import tkinter.ttk as ttk

from setuptools import Command

'''기본설정'''
home = Tk()
home.title("YBCP Setting") #창 이름 
home.geometry("340x280+1100+500") #가로 x 세로 +x +y 

# #프레임 씌우기
# frame = LabelFrame(home, text="sign",relief="solid", bd=1)
# frame.pack(side="bottom")

''' 숫자키 선택용 콤보박스 1~10'''
val = [str(i) for i in range(1, 11)]
#val 콤보박스 범위 지정
combobox = ttk.Combobox(home, height=10, values=val, state="readonly")
#combobox (home 창에 높이 10, val의 값을 벨류로 가져옴, 상태 = 읽기전용)
combobox.pack()


'''기능키 선택용 라디오버튼 Ctrl or Alt'''
select_var = StringVar()
#select_var를 정수형바로 설정
# def check():
#  print (select_var.get())
# #check select_var의 벨류값을 출력
btn1 = Radiobutton(home, text="Ctrl", value="Ctrl" ,  variable=select_var)
btn2 = Radiobutton(home, text="Alt", value="Alt", variable=select_var)
#btnN = 라디오버튼(home창에 text , 각 벨류, 눌렀을때 커맨트 check 실행 각 벨류값 출력, 가능한값, select_var 정수)
btn1.pack()
btn2.pack()

def inse():
 e.insert(0, combobox.get())
 e.insert(0, select_var.get())

'''설정 확인 및 저장버튼'''
def Allcheck():
  print("기능키=",select_var.get(),"숫자키=", combobox.get())
# btn3 선택된 기능키 숫자키 확인
btn3 = Button(home, text="Save", command=inse)
btn3.pack()

e = Entry(home,state="normal",width=13)
e.pack()



home.mainloop()