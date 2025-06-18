from tkinter import*
from datetime import date
root=Tk()
root.title("Getting started with widgets")
root.geometry("400x300")
lb1=Label(text="Hey There!",fg="white",bg="#93CBFF", height=1, width=300)
name_lb1=Label(text="Full name", bg="#3885D3")
name_entry=Entry()
def display():
    name=name_entry.get()
    global Message
    Message="Welcome to the Application! \n Todays date is"
    greet="Hello"+name+"\n"
    text_box.insert(END,greet)
    text_box.insert(END, Message)
    text_box.insert(END, date.today())
text_box=Text(height=3)
btn=Button(text="Beginn", command=display, height=1, bg= "#1261A0", fg="white")
lb1.pack()
name_lb1.pack()
name_entry.pack()
text_box.pack()
btn.pack()
root.mainloop()