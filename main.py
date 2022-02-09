import pandas as pd
import tkinter as tk

data = pd.read_csv("./data/sp1.csv")


window = tk.Tk()
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

#Radiobutton
def radio_used():
    print(radio_state.get())
#Variable to hold on to which radio button value is checked.
radio_state = tk.IntVar()
radiobutton1 = tk.Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = tk.Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()

#Buttons
def action():
    sorted = data.sort_values(by='A', ascending=True)
    print(sorted)
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

button = tk.Button(text="Sort A ascending", command=action)
# button.grid(column=1, row=0)


window.mainloop()