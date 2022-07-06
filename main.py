import math
from tkinter import *
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


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="It's Long Break")
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="It's Short Break")
    else:
        count_down(work_sec)
        timer_label.config(text="It's Work Time")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global reps
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            mark += "✔"
        check_mark_label.config(text=mark)

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps, timer
    window.after_cancel(timer)
    timer_label.config(text="TIMER")
    canvas.itemconfig(timer_text, text="00:00")
    check_mark_label.config(text="")
    reps = 0

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="TIMER")
timer_label.config(fg=GREEN, font=(FONT_NAME, 30, "normal"), bg=YELLOW)
timer_label.grid(column=1, row=0, padx=10, pady=10)

canvas = Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 110, image=tomato_img)
timer_text = canvas.create_text(106, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1, padx=10, pady=10)

start_button = Button(text="Start", command=start_timer)
start_button.config(width=8, bg=GREEN, border=3)
start_button.grid(column=0, row=2, padx=10, pady=10)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.config(width=8, bg=GREEN, border=3)
reset_button.grid(column=2, row=2, padx=10, pady=10)

check_mark_label = Label()
check_mark_label.config(font=("black", 15, "normal"), bg=YELLOW)
check_mark_label.grid(column=1, row=3, padx=10, pady=10)

window.mainloop()