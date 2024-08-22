from tkinter import *

# FUNCTIONS
user_text = ""
timer = None

#Save text file
def save_text():
    global user_text
    try:
        with open('textfile.txt', 'r') as f:
            infile=f.read()
    except FileNotFoundError:
        with open('textfile.txt', 'w') as f:
            f.write(user_text)
            user_text = ""
            return
    else:

        if infile == "":
            f.write(user_text)
        else:
            text_to_write = f'\n{user_text}'
            with open('textfile.txt', 'a') as f:
                f.write(text_to_write)
                user_text = ""
    finally:
        return

#start timing with first keystroke
def start(key_stroke):
    global timer, user_text
    if timer is not None:
        window.after_cancel(timer)

    #save all characters to user_text
    if key_stroke.char:
        user_text += key_stroke.char
        timer = window.after(10000, reset_app)
    # delete when backspace is pressed
    elif key_stroke.keysym == "BackSpace":
        user_text = user_text[0: len(user_text) - 1]
    return user_text

#restart app, delete stored text
def reset_app():
    global timer, user_text
    typing_area.delete(index1='1.0', index2='end')
    user_text = ""
    timer = None
    return



# UI SETUP
BORDER = "light goldenrod"
FG = 'peach puff'
BG = "grey7"

FONT1= ('Calibri', 14, "normal")
FONT2 = ('Calibri', 12, "normal")
HEAD_FONT = ('Arial', 24, "bold")

title = "Want to be motivated to write continuously? "
instruction = "If you don't press any key for 10 seconds, \nthe text you have written will disappear.\nLet's start!"

window = Tk()
window.title('Disappearing Text')
window.config(bg=BG, padx=10, pady=10)

title = Label(text=title, font=HEAD_FONT, bg=BG, fg=FG, padx=10, pady=10)

instructions = Label(text=instruction, font=FONT2, fg=FG, bg=BG, pady=10)

typing_area = Text(font=FONT1, bg=BG, fg=FG,
                   width=80, height=15, wrap='word',
                   highlightcolor=BORDER,
                   highlightthickness=2,
                   highlightbackground=BORDER,
                   padx=10, pady=10)

typing_area.bind('<KeyPress>', start)

reset = Button(text='Reset', fg=FG, bg=BG,
                   font=FONT1,
                   highlightbackground=FG,
                   highlightcolor=FG,
                   highlightthickness=0, border=2,  width=30, pady=10, padx=10,
                   command=reset_app)

save = Button(text='Save', fg=FG, bg=BG, font=FONT1,
                  highlightbackground=FG,
                  highlightcolor=FG,
                  highlightthickness=0, border=2, width=30, pady=10, padx=10,
                  command=save_text)

title.grid(row=0, column=0, columnspan=2)
instructions.grid(row=1, column=0, columnspan=2)
typing_area.grid(row=2, column=0, columnspan=2)
reset.grid(row=3, column=0)
save.grid(row=3, column=1)

window.mainloop()