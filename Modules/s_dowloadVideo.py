import tkinter as tk

from pytube import YouTube
def downloadVid():
#    global E1
#    string =E1.get()

    yt = YouTube("https://www.youtube.com/watch?v=8yvGCAvOAfM")
    print(yt.title)
    stream = yt.streams.first()
    stream.download()


root=tk.Tk()
    
w=tk.Label(root,text="Youtube Downloader")
w.pack()

#E1=tk.Entry(root,bd=10)
#E1.pack(side=tk.TOP)


button=tk.Button(root,text="Download",fg="red",command=downloadVid   )
button.pack(side=tk.BOTTOM)

root.mainloop()