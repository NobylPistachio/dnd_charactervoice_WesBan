#!/usr/bin/python
#was watching this
#https://www.youtube.com/watch?v=ibf5cx221hk&t=625s


import tkinter as tk

#thinking about what i want the gui to do.
    #1) input area for tts
    #2) area for tts history
    #3) button for vttts
    #4) buttons for pre-recorded phrases (maybe make a scrollable list)
    #5) a way to save new pre-recorded messages


class vttts_gui():
    def __init__(self):
        self.root = tk.Tk()

        self.label = tk.Label(self.root, text="Your Message", font=('Arial', 18))
        self.label.pack(padx=10,pady=10)

        self.textbox = tk.Text(self.root, height=5, font=('Arial', 16))
        self.label.pack(padx=10,pady=10)

        self.check_state = tk.IntVar()

        self.check = tk.Checkbutton(self.root, text="Show Messagebox", font=('Arial', 16), variable=self.check_state)
        self.check.pack(padx=10,pady=10)

        self.button = tk.Button(self.root, text="Show Message", font=('Arial', 18))
        self.button.pack(padx=10,pady=10)

        self.root.mainloop()

    def show_message(self):
        pass


# root = tk.Tk()
# root.geometry("500x500")
# root.title("AEIOU TTS")

# label = tk.Label(root, text="Hello World!", font=('Arial', 18))
# label.pack(padx=20,pady=20)

# textbox = tk.Text(root, height=3, font=('Arial', 16))
# textbox.pack(padx=10)

# myentry = tk.Entry(root)
# myentry.pack(padx=10,pady=10)

# button = tk.Button(root, text="Click Me!", font=('Arial', 18))
# button.pack(padx=10, pady=10)

# def helloCallBack():
#     # tkinter.tkMessageBox.showinfo()
#     pass
# # Code to add widgets will go here...

vttts_gui()

print(dir(tk))