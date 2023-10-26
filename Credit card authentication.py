from tkinter import*
from tkinter import messagebox
from PIL import ImageTk,Image

root=Tk()
root.title("Credit Card Authentication")
root.geometry("600x400")
root.configure(background="#818ea3")

input_box = Entry()
input_box.place(relx=0.5,rely=0.3,anchor=CENTER)
img=ImageTk.PhotoImage(Image.open("credit.jpg"))
label = Label(root,Image=img)

def authentication():
    try:
        input_value = int(input_box.get())
        message.showinfo("Alert","Credit Card has been accepted")
    except(ValueError):
        message.showinfo("Error","Credit card has not been accepted please enter valid pin")

btn = Button(root,text="Check credit card",command=authentication)
btn.place(relx=0.5,rely=0.4,anchor=CENTER)
label.place(relx=0.5,rely=0.7,anchor=CENTER)

root.mainloop()