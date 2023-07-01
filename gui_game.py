import tkinter
import random

window = tkinter.Tk()
window.title("Rock-Paper-Scissors")
window.geometry("640x480")
window.resizable(False, False)

frame = tkinter.Frame(window)
frame.pack()

defense = ""
cpu_choice = ["✊", "✋", "✌️"]

def cpu_move():
    global defense
    global cpu_choice
    defense = random.choice(cpu_choice)
    cpu_choice_ui.config(text=defense)

user_gesture_ui = tkinter.LabelFrame(frame, text="Choose your gesture:", font=("Arial", 12))
user_gesture_ui.grid(row=0, column=0, padx=20, pady=20)

rock_button = tkinter.Button(user_gesture_ui, text="✊")
rock_button.grid(row=0, column=0)
paper_button = tkinter.Button(user_gesture_ui, text="✋")
paper_button.grid(row=0, column=1)
scissors_button = tkinter.Button(user_gesture_ui, text="✌️")
scissors_button.grid(row=0, column=2)

for widget in user_gesture_ui.winfo_children():
    widget.grid_configure(padx=10, pady=10)
    widget.config(font=("Arial", 50), highlightthickness=0, bd=0, command=cpu_move)

cpu_gesture_ui = tkinter.LabelFrame(frame, text="CPU gesture:", font=("Arial", 12))
cpu_gesture_ui.grid(row=1, column=0, padx=20, pady=20)

cpu_choice_ui = tkinter.Label(cpu_gesture_ui, text="PH", font=("Arial", 50))
cpu_choice_ui.grid(row=1, column=0, padx=10, pady=10)

window.mainloop()