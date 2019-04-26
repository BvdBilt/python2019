from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
window = Tk()

window.title("Image selector")

window.geometry('600x600')

def select_image():
    path = filedialog.askopenfilename(filetypes=[("Image File",'.jpg')])
    im = Image.open(path)
    tkimage = ImageTk.PhotoImage(im)
    showImg=Label(window, image=tkimage)
    showImg.image = tkimage
    showImg.pack()

btn = Button(window, text="Select image", command=select_image)
btn.pack(side="bottom", fill="both", expand="yes", padx="100", pady="100")

window.mainloop()