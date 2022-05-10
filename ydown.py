from tkinter import *
from tkinter import filedialog
from pytube import YouTube
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
     rename = front + '.mp3'
     os.rename(name, rename)




chk = IntVar()
checkbox = Checkbutton(root, text="MP3", variable=chk)    
path_label = Entry(root, width=28)
path_btn1 = Button(root, text="Path", command=select_path)
url_label = Entry(root, width=28)
download_btn1 = Button(root, text="Download",command=fdownload )



checkbox.grid(row=1, column=1)
url_label.grid(row=1, column=0)
path_label.grid(row=2, column=0)
path_btn1.grid(row=2, column=1)
download_btn1.grid(row=3, column=0)

root.mainloop()