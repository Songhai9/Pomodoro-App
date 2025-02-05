from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global timer
    window.after_cancel(timer)
    timer_label.config(text='TIMER')
    check_marks.config(text='')
    canvas.itemconfig(timer_text, text='00:00')
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    if reps % 8 == 0:
        countdown(LONG_BREAK_MIN * 60)
        timer_label.config(text='LONG BREAK', fg=RED)
    elif reps % 2 == 0:
        countdown(SHORT_BREAK_MIN * 60)
        timer_label.config(text='SHORT BREAK', fg=PINK)
    else:
        countdown(WORK_MIN * 60)
        timer_label.config(text='WORK')
        

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    global timer
    if count // 60 < 10 and count % 60 >= 10:
        canvas.itemconfig(timer_text, text=f'0{count // 60}:{count % 60}')
    if count // 60 < 10 and count % 60 < 10:
        canvas.itemconfig(timer_text, text=f'0{count // 60}:0{count % 60}')
    elif count // 60 >= 10 and count % 60 >= 10:
       canvas.itemconfig(timer_text, text=f'{count // 60}:{count % 60}')
    elif count // 60 >= 10 and count % 60 < 10:
        canvas.itemconfig(timer_text, text=f'{count // 60}:0{count % 60}')
    if count > 0:
       timer = window.after(1000, countdown, count - 1)
    if count == 0:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            mark += "✓"
        check_marks.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
pic = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=pic)
timer_text = canvas.create_text(103, 130, text='00:00', fill="white", font=(FONT_NAME, 50, 'bold'))

timer_label = Label(text='TIMER', fg=GREEN)
start_btn = Button(text='Start', highlightthickness=0, command=start_timer)
reset_btn = Button(text='Reset', highlightthickness=0, command=reset)
check_marks = Label(fg=GREEN)

timer_label.config(bg=YELLOW, font=(FONT_NAME, 30, 'bold'))
check_marks.config(bg=YELLOW)


timer_label.grid(row=0, column=1)
canvas.grid(column=1, row=1)
start_btn.grid(row=2, column=0)
reset_btn.grid(row=2, column=2)
check_marks.grid(row=2, column=1)

window.mainloop()