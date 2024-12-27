from tkinter import *
from PIL import Image, ImageTk
from pystray import *
import threading

time_apr = "day"


def tray_app():
    # this is completely different program I should move it to the another file soon, it create tray icon and execute func opmenu
    tray_image = Image.open("images/lol.png")

    icon = Icon("Mainmenu", tray_image, menu = Menu(
        MenuItem("Exit", opmenu),
        MenuItem("Ch. Moka", opmenu)
        ))

    icon.run()


def opmenu(icon, item):
    global root, label, time_apr, photo
    if str(item) == "Exit":
        root.destroy()
    elif str(item) == "Ch. Moka":
        if time_apr == "day":
            image_path = "images/Mokanight.png"
            image = Image.open(image_path)
            photo = ImageTk.PhotoImage(image)
        
            label.configure(image=photo)
        
            time_apr = "night"
        else:
            image_path = "images/Mokaday.png"
            image = Image.open(image_path)
            photo = ImageTk.PhotoImage(image)
        
            label.configure(image=photo)
        
            time_apr = "day"
       
        
def move(event):
    global label, photo
    if time_apr == "day":
        image_path = "images/Mokada_pick.png"
        
    else:
        image_path = "images/Mokani_pick.png"


    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)
    label.configure(image=photo)


    # Calculate new window position
    new_x = event.x_root - window_width // 2
    new_y = event.y_root

    # Ensure the window stays within screen borders
    if new_x < 0:
        new_x = 0
    elif new_x + window_width > screen_width:
        new_x = screen_width - window_width

    if new_y < 0:
        new_y = 0
    elif new_y + window_height > screen_height:
        new_y = screen_height - window_height

    # Update window position
    root.geometry(f"{window_width}x{window_height}+{new_x}+{new_y}")


def putie(event):
    global label, photo
    if time_apr == "day":
        image_path = "images/Mokaday.png"

    else:
        image_path = "images/Mokanight.png"

    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)
    label.configure(image=photo)



root = Tk()
root.overrideredirect(True)
root.attributes("-topmost", True)
root.config(bg="blue")
root.attributes("-transparentcolor", "blue")

# get screen size
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()   

# set window size
window_width = 94
window_height = 94 

# move window to right bottom
x = screen_width - window_width     
y = screen_height - window_height 

root.geometry(f"{window_width}x{window_height}+{x}+{y}")

image_path = "images/Mokaday.png"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)

label = Label(root, image=photo, bg="blue")
label.pack()

label.bind("<B1-Motion>", move)
label.bind("<ButtonRelease-1>", putie)

# multiprocessing activation
threading.Thread(target=tray_app, daemon=True).start()

root.mainloop()
