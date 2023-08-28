import tkinter as tk
from tkinter import ttk
from soundOutput import put_test

class Window():
    def __init__(self,IO:set) -> None:
        # Create the main window
        self.root = tk.Tk()
        self.root.title("Text-to-Speech GUI")
        self.root.geometry("500x500")

        

        self.root.mainloop()



InputOutput:set = (["Microphone", "Laptop"],["Speakers", "Headset"])

if __name__ == "__main__":
    main = Window(InputOutput)