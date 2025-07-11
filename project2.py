from tkinter import *
from tkinter import messagebox
from datetime import date
def calculate_age():
    try:
        day=int(day_entry.get())
        month=int(month_entry.get())
        year=int(year_entry.get())
        birth_date=date(year,month,day)
        today=date.today()
        age=today.year-birth_date.year
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age-=1
        result_var.set(f"You are {age} year{'s' if age != 1 else ''} old.")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid numeric date.")
root=Tk()
root.title("Age Calculator")
root.geometry("300x400")
root.resizable(False, False)
Label(root,text="Day (1-31):").pack(pady=(20, 0))
day_entry=Entry(root, justify="center")
day_entry.pack()
Label(root, text="month (1-12):").pack(pady=(10, 0))
month_entry=Entry(root, justify="center")
month_entry.pack()
Label(root, text="year:").pack(pady=(10, 0))
year_entry=Entry(root, justify="center")
year_entry.pack()
Button(root, text="Calculate Age", command=calculate_age).pack(pady=20)
result_var=StringVar()
Label(root, textvariable=result_var, font=("Arial", 14, "bold")).pack(pady=10)
day_entry.focus()
root.mainloop()