from operator import mod
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Progressbar
from pytube import YouTube
from PIL import ImageTk
import shutil
import os
from moviepy.editor import VideoFileClip
root=Tk()
root.title("Youtube Downloader")
root.geometry('300x200+1100+500')

def select_path():
    path1 = filedialog.askdirectory()
    path_label.insert(0, path1)
    
def fdownload():
    ytb_url = url_label.get()
    where = path_label.cget("text")
    ytb_vd = YouTube(ytb_url)
    ytb_vd = YouTube(ytb_url).streams.filter(only_audio=True).first()
    ytb_vd.download()
    if chk.get() == 1:
     name = ytb_vd.download()
     front, back = os.path.splitext(name)
     Size = ytb_vd.filesize
     global MaxfileSize
     MaxfileSize = Size
     rename = front + '.mp3'
     os.rename(name, rename)
    


root.tk.call('wm', 'iconphoto', root._w, ImageTk.PhotoImage(file='C:/Users/we202/Documents/GitHub/YBCP/image/Youtube.ico'))

chk = IntVar()
checkbox = Checkbutton(root, text="MP3", variable=chk)    
path_label = Entry(root, width=28)
path_btn1 = Button(root, text="Path", command=select_path)
url_label = Entry(root, width=28)
download_btn1 = Button(root, text="Download",command=lambda:[fdownload(), barfunction()] )
bar = Progressbar(root, length=200,maximum=100, mode="determinate")



    
checkbox.grid(row=1, column=1)
url_label.grid(row=1, column=0)
path_label.grid(row=2, column=0)
path_btn1.grid(row=2, column=1)
download_btn1.grid(row=3, column=0)
bar.grid(row=4,column=0)
root.mainloop()