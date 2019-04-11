from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
window = Tk()

window.title("Image selectah")

window.geometry('600x600')

path = filedialog.askopenfilename(filetypes=[("Image File",'.jpg')])
im = Image.open(path)
tkimage = ImageTk.PhotoImage(im)
showImg=Label(window,image = tkimage)
showImg.image = tkimage
showImg.pack()

# def select_image(self):
#
#     path = filedialog.askopenfilename(filetypes=[("Image File",'.jpg')])
#     im = Image.open(path)
#     tkimage = ImageTk.PhotoImage(im)
#     showImg=Label(window,image = tkimage)
#     showImg.image = tkimage
#     showImg.pack()
#     return self

# btn = Button(window, text="Select image", command=select_image)
# btn.pack(side="bottom", fill="both", expand="yes", padx="100", pady="100")

window.mainloop()