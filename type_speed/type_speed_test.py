from tkinter import *
import math

FONT_NAME="Courier"
words=[]
list_of_words=[]
timercheck=None

with open("100_words.txt", "r") as f:
    words=f.readlines()
for i in words:
    list_of_words.append(i.strip())


def start_time():
    countdown(60)
def countdown(count):
    length=0
    count_sec= count%60
    if count_sec <10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer,text=f"00:{count_sec}")
    words= input.get(1.0, "end-1c").split(" ")
    for word in words:
        if word in list_of_words:
            length += 1
            if length >= 9:
                wordlist.config(text=f"{list_of_words[10:20]}")
            elif length >= 19:
                wordlist.config(text=f"{list_of_words[20:30]}")
            elif length >= 29:
                wordlist.config(text=f"{list_of_words[30:40]}")
            elif length >= 39:
                wordlist.config(text=f"{list_of_words[40:50]}")
            elif length >= 49:
                wordlist.config(text=f"{list_of_words[50:60]}")
            elif length >= 59:
                wordlist.config(text=f"{list_of_words[60:70]}")
            elif length >= 69:
                wordlist.config(text=f"{list_of_words[70:80]}")
            elif length >= 79:
                wordlist.config(text=f"{list_of_words[80:90]}")
            elif length >= 89:
                wordlist.config(text=f"{list_of_words[90:100]}")



    if count>0:
        global timercheck
        timercheck=window.after(1000,countdown, count-1)
    elif count == 0:
        name.config(text=f"You managed to write {length} words correctly")


window = Tk()
window.title("Type speed test")
window.config(padx=100, pady=50)



canvas=Canvas(width=200, height=200, highlightthickness=0, borderwidth=10 )
img=PhotoImage(file="typing.png")
canvas.create_image(100,120, image=img)
text=canvas.create_text(175,200, text="designed by Freepik", fill="black", font=(FONT_NAME, 4, "normal"))
timer=canvas.create_text(100,40, text="01:00", fill="black", font=(FONT_NAME, 20, "normal"))


name=Label(text="Test your typing speed! \nType the words you see below in the empty field\n and separate them by space.\n\nHit start to start the clock", font=(FONT_NAME,12,"bold"), padx=10, pady=10)

wordlist=Label(text=f"{list_of_words[0:10]}", font=(FONT_NAME,8,"normal"),padx=10, pady=10)

input=Text(width=30, height=5, padx=10, pady=10)
start=Button(text="Start", command=start_time)

name.grid(column=0, columnspan=2, row=0)
canvas.grid(column=0, columnspan=2, row=1)
wordlist.grid(column=0, columnspan=2, row=3)
input.grid(column=0, columnspan=2, row=4)
start.grid(column=0, columnspan=2, row=2)


window.mainloop()

