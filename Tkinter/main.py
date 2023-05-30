import tkinter as tk

WIDTH = 800
HEIGHT = 600

root = tk.Tk()
root.resizable(False, False)

root.geometry("{}x{}".format(WIDTH,HEIGHT))
root.title("My first GUI")

label = tk.Label(root, text="Hello World!", font=('Arial', 15))
label.pack(padx=20, pady=20)
# label.place(relx=0.5, rely=0.5, anchor="center") #Center the label

textbox = tk.Text(root, width=WIDTH, height=(HEIGHT // (HEIGHT - 400)) ,font=('Arial', 13), bg='#333333')
textbox.pack(padx=10, pady=10)

buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

btn1 = tk.Button(buttonframe, text="1", font=("Arial", 18))
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

btn2 = tk.Button(buttonframe, text="2", font=("Arial", 18))
btn2.grid(row=0, column=1, sticky=tk.W+tk.E)

btn3 = tk.Button(buttonframe, text="3", font=("Arial", 18))
btn3.grid(row=0, column=2, sticky=tk.W+tk.E)

btn4 = tk.Button(buttonframe, text="4", font=("Arial", 18))
btn4.grid(row=1, column=0, sticky=tk.W+tk.E)

btn5 = tk.Button(buttonframe, text="5", font=("Arial", 18))
btn5.grid(row=1, column=1, sticky=tk.W+tk.E)

btn6 = tk.Button(buttonframe, text="6", font=("Arial", 18))
btn6.grid(row=1, column=2, sticky=tk.W+tk.E)

buttonframe.pack(fill=tk.X)

# anotherbtn = tk.Button(root, text="TEST")
# anotherbtn.place(x=350, y=250, height=100, width=100)

# button = tk.Button(root, text="Click Me!", font=("Arial", 18))
# button.pack(padx=10, pady=10)

# myentry = tk.Entry(root)
# myentry.pack()

root.mainloop()