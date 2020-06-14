import numpy as np
import cv2
import os

import glob

# Install tkinter:  sudo apt install python3-tk
import tkinter
from PIL import ImageTk, Image

from tkinter import filedialog


class Interface:

    def __init__(self):
        self.init_ui()
        self.index = 0

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

        self.frame = tkinter.Frame(self.window, width=400, height=400)
        self.frame.grid()

        self.lmain = tkinter.Label(self.frame, image=self.image)
        self.lmain.image = self.image
        self.lmain.grid()

        self.render_image(self.image)
        # self.window.mainloop()


    def render_image(self, image):
        self.lmain.configure(image=image)
        self.window.mainloop()

    def prev_callback(self):
        if self.index > 0:
            self.index -= 1

        print("prev called: Load:" + self.filelist[self.index])
        print(self.index)

        image_path = self.filelist[self.index]
        self.render_image(self.load_image(image_path))
        return

    def next_callback(self):
        if len(self.filelist) > self.index + 1:
            self.index += 1
        print("next called: Load:" + self.filelist[self.index])
        print(self.index)

        image_path = self.filelist[self.index]
        self.render_image(self.load_image(image_path))

        return

    def open_folder_callback(self):
        directory = filedialog.askdirectory()

        if directory is not ():
            print(directory)
            self.generate_glob(directory)

        else:
            print("empty")
        print("open folder called for dir:", directory)
        return

    def load_image(self, image_path):

        try:
            image = Image.open(image_path)
        except FileNotFoundError:
            return self.get_error_loading_frame(image_path)

        image = Image.Image.resize(image, (300, 300))
        # image = Image.fromarray(image)
        image = ImageTk.PhotoImage(image)

        return image

    def generate_glob(self, directory):
        self.filelist = []
        for name in glob.glob(os.path.join(directory, "*.jpg")):
            print(name)
            self.filelist.append(name)
        self.index = 0
        print(self.filelist)

    def get_default_frame(self):
        frame = np.zeros([300, 300, 3], dtype=np.uint8)
        frame = cv2.putText(frame, "No Image to display", (40, 150), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255, 255, 255))
        image = Image.fromarray(frame)
        # image = Image.open("sample.jpeg")
        image = ImageTk.PhotoImage(image)
        return image

    def get_error_loading_frame(self, path):
        frame = np.zeros([300, 300, 3], dtype=np.uint8)
        frame = cv2.putText(frame, "Error Loading Image:", (60, 150), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255, 255, 255))
        frame = cv2.putText(frame, path, (10, 150), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
        image = Image.fromarray(frame)
        # image = Image.open("sample.jpeg")
        image = ImageTk.PhotoImage(image)
        return image


if __name__ == "__main__":
    interface = Interface()
