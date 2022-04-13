from tkinter import *

COLORS = ["#9A9483", "#AAA492", "#C7BEA2", "#E5DCC3", "#ffffff"]
count = 4


def start(event=None):
    entry.grid(column=0, row=0, columnspan=2)
    canvas.delete(logo_image)
    canvas.itemconfig(label, text="Don't Stop Typing or your Progress will be lost🔊")
    entry.config(background="#ffffff")
    entry.bind('<Key>', reset)
    count_down(count)


def reset(event=None):
    canvas.itemconfig(label_2, text="")
    window.after_cancel(timer)
    start()


def count_down(c):
    global timer
    canvas.itemconfig(timer_text, text=f"0{c}")
    entry.config(background=COLORS[c])
    if c == 0:
        entry.delete(0, END)
        canvas.itemconfig(label_2, text="All your Progress is lost 😓\ntry again.")
    elif c > 0:
        timer = window.after(1000, count_down, c - 1)


window = Tk()

window.config(padx=20, pady=20, width=600, height=400, bg="#FBD6D2")
window.title("Keep Writing App")

canvas = Canvas(window, width=600, height=400, bg="#FBD6D2")
canvas.grid(column=0, row=0, columnspan=2)

label = canvas.create_text(300, 60, text="Welcome to the forbidden game!\n\tPress Start!", font="Areal 15 bold",
                           fill="#3A3845")

exit_button = Button(window, text="Exit", command=window.destroy, height=2, width=5, bg="#EBD8C3")
exit_button.grid(column=1, row=1)

start_button = Button(window, text="Start", command=start, height=2, width=5, bg="#EBD8C3")
start_button.grid(column=0, row=1)

logo = PhotoImage(file="logo.png")
logo_image = canvas.create_image(300, 250, image=logo)

entry = Entry(window, width=30, font='Arial 20')

timer_text = canvas.create_text(300, 150, text="", fill="#46244C", font=("Helvetica", 25, "bold"))

label_2 = canvas.create_text(300, 300, text="", font="Areal 15 bold", fill="#3A3845")

window.mainloop()
