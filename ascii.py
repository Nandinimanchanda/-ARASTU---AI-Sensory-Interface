import ascii_magic
import tkinter as tk
from PIL import Image,ImageTk

win=tk.Tk()

win.configure(background="black")
L1=tk.Label()
L1.pack()
output = ascii_magic.from_image("C:\\Users\\nandi\\.vscode\\ascii_art\\laptop.jpg")
output.to_terminal()
#photo = ImageTk.PhotoImage(Image.open("C:\\Users\\nandi\OneDrive\\Pictures\\Screenshots\\APJ.png"))



L1.configure(image=photo)

win.mainloop()

