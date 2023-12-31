import tkinter
import random

window = tkinter.Tk()
window.title("Rock-Paper-Scissors")
window.geometry("800x600")
window.resizable(False, False)

frame = tkinter.Frame(window)
frame.pack()

defense = ""
cpu_choice = ["✊", "✋", "✌️"]
attack = "TEST"

def user_move(gesture):
    global attack
    global defense
    attack = gesture
    #result_ui.config(text=attack+defense)

def cpu_move():
    global defense
    global cpu_choice
    defense = random.choice(cpu_choice)
    cpu_choice_ui.config(text=defense)

def evaluation():
    if attack == "✊":
        if defense == "✊": 
            result_ui.config(text="DRAW")
        if defense == "✋":
            result_ui.config(text="YOU LOSE")
            #cpu_wins +=1
        if defense == "✌️":
            result_ui.config(text="YOU WIN")
            #user_wins += 1

    if attack == "✋":
        if defense == "✋": 
            result_ui.config(text="DRAW")
        if defense == "✌️":
            result_ui.config(text="YOU LOSE")
            #cpu_wins += 1
        if defense == "✊":
            result_ui.config(text="YOU WIN")
            #user_wins += 1

    if attack == "✌️":
        if defense == "✌️": 
            result_ui.config(text="DRAW")
        if defense == "✊":
            result_ui.config(text="YOU LOSE")
            #cpu_wins += 1
        if defense == "✋":
            result_ui.config(text="YOU WIN")
            #user_wins += 1

user_gesture_ui = tkinter.LabelFrame(frame, text="Choose your gesture:")
user_gesture_ui.grid(row=0)

rock_button = tkinter.Button(user_gesture_ui, text="✊", command=lambda: [cpu_move(), user_move("✊"), evaluation()])
rock_button.grid(column=0)
paper_button = tkinter.Button(user_gesture_ui, text="✋", command=lambda: [cpu_move(), user_move("✋"), evaluation()])
paper_button.grid(column=1)
scissors_button = tkinter.Button(user_gesture_ui, text="✌️", command=lambda: [cpu_move(), user_move("✌️"), evaluation()])
scissors_button.grid(column=2)

round_result_ui = tkinter.LabelFrame(frame, text="Round result:")
round_result_ui.grid(row=1)

result_ui = tkinter.Label(round_result_ui, text=attack)
result_ui.grid(column=0)

cpu_gesture_ui = tkinter.LabelFrame(frame, text="CPU gesture:")
cpu_gesture_ui.grid(row=2)

cpu_choice_ui = tkinter.Label(cpu_gesture_ui, text="")
cpu_choice_ui.grid(column=0)

for widget_labelframe in frame.winfo_children():
    widget_labelframe.grid_configure(column=0, padx=20, pady=20)
    widget_labelframe.config(font=("Arial", 12), width=10)

for widget_button in user_gesture_ui.winfo_children():
    widget_button.grid_configure(row=0, padx=10, pady=10)
    widget_button.config(font=("Arial", 50), highlightthickness=0, bd=0)

for widget_label_result in round_result_ui.winfo_children():
    widget_label_result.grid_configure(row=1, padx=20, pady=20)
    widget_label_result.config(font=("Arial", 50), width=10, justify='center')

for widget_label_cpu in cpu_gesture_ui.winfo_children():
    widget_label_cpu.grid_configure(row=1, padx=20, pady=20)
    widget_label_cpu.config(font=("Arial", 50), width=10, justify='center')

window.mainloop()