from tkinter import *
from tkinter import filedialog
from pytube import YouTube
import shutil

root=Tk()
root.title("Youtube Downloader")
root.geometry('300x200+1100+500')

def select_path():
    path1 = filedialog.askdirectory()
    path_label.insert(0, path1)
    
def download():
    ytb_url = url_label.get()
    where = path_label.cget("text")
    ytb_vd = YouTube(ytb_url)
    ytb_vd = YouTube(ytb_url).streams.get_highest_resolution().download()
    shutil(ytb_vd, where)
    
path_label = Entry(root, width=28)
path_btn1 = Button(root, text="Path", command=select_path)
url_label = Entry(root, width=28)
download_btn1 = Button(root, text="Download",command=download )

url_label.grid(row=1, column=0)
path_label.grid(row=2, column=0)
path_btn1.grid(row=2, column=1)
download_btn1.grid(row=3, column=0)

root.mainloop()