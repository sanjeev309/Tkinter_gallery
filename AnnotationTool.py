import numpy as np
import cv2
import os

# Install tkinter:  sudo apt install python3-tk
import tkinter
from PIL import ImageTk, Image


class Interface:

    def __init__(self):
        self.init_ui()

    def init_ui(self):
        self.window = tkinter.Tk()
        self.window.minsize(300, 300)
        self.window.title("Annotation tool")

        tkinter.Button(self.window, text="Previous", command=self.prev_callback).grid(column=0, row=0, sticky="NW")
        tkinter.Button(self.window, text="Select Folder", command=self.open_folder_callback).grid(column=0, row=0,
                                                                                                  sticky="N")
        tkinter.Button(self.window, text="Next", command=self.next_callback).grid(column=0, row=0, sticky="NE")
        # app = tkinter.Frame(self.window, bg="white")
        # # Create a label in the frame
        self.image = self.get_default_frame()

        frame = tkinter.Frame(self.window, width=400, height=400)
        frame.grid()

        lmain = tkinter.Label(frame, image=self.image)

        lmain.image = self.image
        lmain.grid()

        self.render_image()

    def render_image(self):
        self.window.mainloop()

    def prev_callback(self):
        print("prev called")
        return

    def next_callback(self):
        print("next called")
        return

    def open_folder_callback(self):
        print("open folder called")
        return

    def get_default_frame(self):
        frame = np.zeros([300, 300, 3], dtype=np.uint8)
        frame = cv2.putText(frame, "No Image to display", (40, 150), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255, 255, 255))
        image = Image.fromarray(frame)
        # image = Image.open("sample.jpeg")
        image = ImageTk.PhotoImage(image)
        return image

if __name__ == "__main__":
    interface = Interface()
