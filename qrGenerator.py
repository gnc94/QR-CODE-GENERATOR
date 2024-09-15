import qrcode
from tkinter import *
from tkinter import filedialog
import os

def get_code():
    data_var = data.get()
    format_type = format_choice.get()
    
    if data_var and format_type:
        qr = qrcode.make(str(data_var))
        loc = filedialog.askdirectory()
        if loc:
            try:
                os.chdir(loc)
                file_path = f"{data_var}.{format_type.lower()}"
                if os.path.exists(file_path):
                    response = filedialog.askokcancel("File Exists", "File already exists. Do you want to overwrite it?")
                    if not response:
                        return
                qr.save(file_path)
                label_result.config(text="QR Code generated and saved!", fg="green")
            except Exception as e:
                label_result.config(text=f"Error: {str(e)}", fg="red")
        else:
            label_result.config(text="No folder selected", fg="red")
    else:
        label_result.config(text="Please enter data and select a format.", fg="red")

base = Tk()
base.geometry("400x250")
base.title("QR Code Generator")
base.config(bg="#e6f7ff")

data = StringVar()
format_choice = StringVar(value="PNG")

label_format_type = Label(base, text="Select Format Type:", bg="#e6f7ff", font=("Arial", 12))
label_format_type.place(x=80, y=20)

formats = ["PNG", "JPEG", "BMP", "GIF"]
format_menu = OptionMenu(base, format_choice, *formats)
format_menu.config(width=15, font=("Arial", 10), bg="#cce7ff")
format_menu.place(x=220, y=20)

label_inside_qrcode = Label(base, text="QR Code Content:", bg="#e6f7ff", font=("Arial", 12))
label_inside_qrcode.place(x=80, y=60)
data_entry = Entry(base, textvariable=data, width=30, font=("Arial", 10))
data_entry.place(x=220, y=60)

button_generate = Button(base, text="Generate QR Code", command=get_code, width=25, height=2, 
                         bg="#4CAF50", fg="white", font=("Arial", 10))
button_generate.place(x=110, y=110)

label_result = Label(base, text="", bg="#e6f7ff", font=("Arial", 10))
label_result.place(x=110, y=180)

base.mainloop()
