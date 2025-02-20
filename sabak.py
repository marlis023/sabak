from tkinter import *

<<<<<<< HEAD
def on_button_click(value):
    current_text = entry_var.get()
    if value == "=":
        try:
            result = eval(current_text)
            entry_var.set(result)
        except Exception as e:
            entry_var.set("Error")
    elif value == "C":
        entry_var.set("")
    else:
        entry_var.set(current_text + value)

root = Tk()
root.title("Калькулятор")
root.geometry("250x200")

entry_var = StringVar()
entry = Entry(root, textvariable=entry_var, font=("Arial", 20), justify=RIGHT)
entry.pack(fill=X, padx=10, pady=10)

buttons = [
    ["15","+","5","="]
]

for row in buttons:
    frame = Frame(root)
    frame.pack(expand=True, fill=BOTH)
    for btn_text in row:
        button = Button(frame, text=btn_text, font=("Arial", 18), command=lambda b=btn_text: on_button_click(b))
        button.pack(side=LEFT, expand=True, fill=BOTH)

root.mainloop()
=======
a=int(input())
b=int(input())
print("a+b")
>>>>>>> 0109b288091a42a38459c33d96fb12099efeb2e6
