import tkinter
import random

window = tkinter.Tk()
window.title("Rock-Paper-Scissors")
window.geometry("640x480")
window.resizable(False, False)

frame = tkinter.Frame(window)
frame.pack()

cpu_choice = ["✊", "✋", "✌️"] # Na poczatku musi byc puste, losowanie dopiero po kliknieciu
defense = random.choice(cpu_choice)

user_gesture_ui = tkinter.LabelFrame(frame, text="Choose your gesture:", font=("Arial", 12))
user_gesture_ui.grid(row=0, column=0, padx=20, pady=20)

rock_button = tkinter.Button(user_gesture_ui, text="✊", font=("Arial", 50), highlightthickness=0, bd=0)
rock_button.grid(row=0, column=0, padx=10, pady=10)
paper_button = tkinter.Button(user_gesture_ui, text="✋", font=("Arial", 50), highlightthickness=0, bd=0)
paper_button.grid(row=0, column=1, padx=10, pady=10)
scissors_button = tkinter.Button(user_gesture_ui, text="✌️", font=("Arial", 50), highlightthickness=0, bd=0)
scissors_button.grid(row=0, column=2, padx=10, pady=10)

cpu_gesture_ui = tkinter.LabelFrame(frame, text="CPU gesture:", font=("Arial", 12))
cpu_gesture_ui.grid(row=1, column=0, padx=20, pady=20)

cpu_choice_ui = tkinter.Label(cpu_gesture_ui, text=defense, font=("Arial", 50))
cpu_choice_ui.grid(row=1, column=0, padx=10, pady=10)

window.mainloop()