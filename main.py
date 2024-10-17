from tkinter import *
from tkinter import messagebox

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
checks = ""
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

def start():
    global reps
    work_min = WORK_MIN * 60
    short_break_min = SHORT_BREAK_MIN * 60
    long_break_min = LONG_BREAK_MIN * 60
    reps += 1
    if reps == 8:
        title_label.config(text="Break", fg=RED)
        count_down(short_break_min)
    elif reps % 2 == 0 and reps < 8:
        title_label.config(text="Break", fg=PINK)
        count_down(long_break_min)
    elif reps < 8:
        title_label.config(text="Work", fg=GREEN)
        count_down(work_min)


def reset():
    global timer, checks, reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text=f"00:00")
    title_label.config(text="Timer", fg=GREEN)
    checks = ""
    check_marks.config(text=checks)
    reps = 0


def count_down(count):
    global reps, checks, timer
    sec = count
    min = sec // 60
    sec %= 60
    canvas.itemconfig(timer_text, text=f"%02d:%02d" % (min, sec))
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start()
        if reps % 2 == 0 and reps < 8:
            checks += "✓"
            window.bell()
            messagebox.showinfo('End', "Take a break. You deserve it! 🤓")
            check_marks.config(text=checks)
        elif reps > 1 and reps < 8:
            window.bell()
            messagebox.showinfo('End', "Get back to work! 😊")


# set window color
window = Tk()
window.config(bg=YELLOW, padx=100, pady=50)
window.title("Pomodoro")

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
canvas.grid(row=1, column=1)

title_label = Label(text="Timer", font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
title_label.grid(row=0, column=1)

start_button = Button(text="Start", command=start, highlightthickness=1, bg=YELLOW, borderwidth=0,
                      highlightbackground=YELLOW)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", command=reset, highlightthickness=1, bg=YELLOW, borderwidth=0,
                      highlightbackground=YELLOW)
reset_button.grid(row=2, column=2)

check_marks = Label(text=checks, font=(FONT_NAME, 25, "bold"), fg=GREEN, bg=YELLOW)
check_marks.grid(row=3, column=1)

window.mainloop()
