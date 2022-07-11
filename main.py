from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 2
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1.5
rep = 0
mark_tick = ""
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text=f"{0:02d}:{0:02d}")
    label_head.config(text="Timer", font=(FONT_NAME, 34, "bold"), fg=GREEN)
    check_mark.config(text="")
    global rep
    rep = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global rep
    rep += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if rep % 8 == 0:
        label_head.config(text="Break!", font=(FONT_NAME, 34, "bold"), fg=RED)
        count_down(long_break_sec)
    elif rep % 2 == 0:
        label_head.config(text="Break!", font=(FONT_NAME, 34, "bold"), fg=PINK)
        count_down(short_break_sec)
    else:
        label_head.config(text="Work!", font=(FONT_NAME, 34, "bold"), fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global mark_tick
    count_min = math.floor(count / 60)
    count_sec = count % 60
    time_display = f"{count_min:02d}:{count_sec:02d}"
    canvas.itemconfig(timer_text, text=time_display)
    if count >= 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if rep % 2 == 0:
            mark_tick += "✔"
            check_mark.config(text=mark_tick)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=40, bg=YELLOW)

label_head = Label(text="Timer", font=(FONT_NAME, 34, "bold"), fg= GREEN, bg=YELLOW)
label_head.grid(column=1, row=0)
label_head.config(padx=50, pady=20)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 24, "bold"), fill="white")
canvas.grid(column=1, row=2)



start_button = Button(text="Start", font=(FONT_NAME, 10, "bold"), fg= "blue", bg="white", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=3)

reset_button = Button(text="Reset", font=(FONT_NAME, 10, "bold"), fg= "blue", bg="white", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=3)


check_mark = Label(fg=GREEN, bg=YELLOW)
check_mark.grid(column=1, row=3)
check_mark.config(padx=20, pady=20)





window.mainloop()