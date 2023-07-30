from PIL import Image, ImageDraw, ImageFont
from tkinter import Label,Canvas,Button,Tk,PhotoImage,Entry

def watermark_the_photo():
    # get an image
    name = get_new_name()

    ab_ph = get_absolute_path()
    with Image.open(ab_ph).convert("RGBA") as base:
    #with Image.open(input("give me an absulute path of your default doc!:")).convert("RGBA") as base:

        # make a blank image for the text, initialized to transparent text color
        txt = Image.new("RGBA", base.size, (255, 255, 255, 0))

        # get a font
        
        # get a drawing context
        d = ImageDraw.Draw(txt)

        # draw text, half opacity
        d.text((10, 10), "@utkuslabel", fill=(255, 255, 255, 128))
        # draw text, full opacity
        d.text((60, 60), "@utkuslabel", fill=(255, 255, 255, 128))
        d.text((120, 120), "@utkuslabel", fill=(255, 255, 255, 128))

        out = Image.alpha_composite(base, txt)

        where = f"/Users/utkuozer/Desktop/{name}watermarked.png"

        out.save(where)

        out.show()

def get_absolute_path():
    path = url_insert.get()
    return path

def get_new_name():
    name = new_file_name.get()
    return name

def change_photograph():
    ab_ph = get_absolute_path()
    image_you_want_to_convert.config(file=ab_ph)



window = Tk()
window.minsize(width=500,height=700)
window.title('Inspect The Photo You Want!')


heading_label = Label(text='PHOTO WATERMARKER',fg="black",bg="white",width=55)
heading_label.grid(row=0,column=0)

canvas = Canvas(width=500,height=500,background="white",highlightthickness=0)
image_you_want_to_convert = PhotoImage(file='png.png')
#The code above may cause error sometimes which is caused by:
#Python Tkinter supports GIF, PGM, PPM, and PNG. So, try changing the extension of the file to one of them
canvas.create_image(250,250,image=image_you_want_to_convert)
canvas.grid(row=1,column=0)

button_save = Button(text="WATERMARK THIS ONE",command=watermark_the_photo)
button_save.grid(row=4,column=0)

button_show = Button(text="SHOW PHOTO",command=change_photograph)
button_show.grid(row=5,column=0)

url_insert = Entry(width=30,highlightbackground='white')
url_insert.insert(0,string="Please Type Absolute Path")
url_insert.grid(row=2,column=0)

new_file_name = Entry(width=30,highlightbackground='white')
new_file_name.insert(0,string="Please Type New File Name")
new_file_name.grid(row=3,column=0)



window.mainloop()