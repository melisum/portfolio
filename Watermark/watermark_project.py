
from tkinter import *
from PIL import Image, ImageDraw, ImageFont, ImageTk
from tkinter import filedialog


def create_watermark():
    fileTypes = [("Image files", "*.png;*.jpg;*.jpeg")]
    path = filedialog.askopenfilename(filetypes=fileTypes)
    # if file is selected
    if len(path):
        img = Image.open(path).convert("RGBA")
        img = img.resize((600, 400))

    # if no file is selected, then we are displaying below message
    else:
        print("No file is chosen !! Please choose a file.")
    mark = input.get()
    # get an image
    # make a blank image for the text, initialized to transparent text color
    txt = Image.new("RGBA", img.size, (255, 255, 255, 0))
    # get a drawing context
    d = ImageDraw.Draw(txt)
    fnt = ImageFont.load_default(14)
        # draw text, half opacity
    d.text((20, 50), f"{mark}      {mark}      {mark}      {mark}      {mark}      {mark}      {mark}      {mark}      {mark}      {mark}      {mark}      {mark}      {mark} ", font=fnt, fill=(255, 255, 255, 128))
    d.text((20, 100), f"{mark}      {mark}      {mark}      {mark}      {mark}      {mark}      {mark}      {mark}      {mark}      {mark}      {mark}      {mark}      {mark} ", font=fnt, fill=(255, 255, 255, 128))
    d.text((20, 150), f"{mark}      {mark}      {mark}      {mark}      {mark}      {mark}      {mark}      {mark}      {mark}      {mark}      {mark}      {mark}      {mark} ", font=fnt, fill=(255, 255, 255, 128))
    d.text((20, 200), f"{mark}      {mark}      {mark}      {mark}      {mark}      {mark}      {mark}      {mark}      {mark}      {mark}      {mark}      {mark}      {mark} ", font=fnt, fill=(255, 255, 255, 128))
    d.text((20, 250), f"{mark}      {mark}      {mark}      {mark}      {mark}      {mark}      {mark}      {mark}      {mark}      {mark}      {mark}      {mark}      {mark} ", font=fnt, fill=(255, 255, 255, 128))
    d.text((20, 300), f"{mark}      {mark}      {mark}      {mark}      {mark}      {mark}      {mark}      {mark}      {mark}      {mark}      {mark}      {mark}      {mark} ", font=fnt, fill=(255, 255, 255, 128))
    d.text((20, 350), f"{mark}      {mark}      {mark}      {mark}      {mark}      {mark}      {mark}      {mark}      {mark}      {mark}      {mark}      {mark}      {mark} ", font=fnt, fill=(255, 255, 255, 128))


    generated_image = Image.alpha_composite(img, txt)
    generated_image.show()


window = Tk()
window.title("Watermark Generator")
window.config(padx=100, pady=50, bg="#f7f5dd")
FONT_NAME="Courier"


canvas=Canvas(width=200, height=280, bg="#f7f5dd", highlightthickness=0)


name=Label(text="Create a custom Watermark", bg="#f7f5dd", font=(FONT_NAME,12,"bold"))
timer=Label(text="Type in your Watermark text here:", bg="#f7f5dd", font=(FONT_NAME,8,"normal"))
input=Entry(width=30)
upload=Button(text="Upload & Create", command=create_watermark)


name.grid(columnspan=3, row=1)
timer.grid(column=1, row=2)
input.grid(column=2, row=2)
upload.grid(columnspan=3, row=3)


window.mainloop()



