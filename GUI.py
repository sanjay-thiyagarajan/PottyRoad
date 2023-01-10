from tkinter import *
from tkinter import filedialog
import numpy as np
import argparse
import os
import tensorflow as tf
import cv2
from PIL import Image, ImageTk
from util import label_map_util
from util import visualization_utils as vis_util
import os
from classifier import classify
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1' 

def browseFile():
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("MP4 file",
                                                        "*.mp4"),
                                                        ("MOV file",
                                                        "*.mov"),
                                                        ("AVI file",
                                                        "*.avi"),
                                                        ("WMV file",
                                                        "*.wmv"),
                                                        ("MKV file",
                                                        "*.mkv"),
                                                    ))
      
    filePathLabel.configure(text=filename)

def submitFile():
    path = filePathLabel.cget('text')
    if path != '':
        classify(path)
    else:
        filePathLabel.configure(text='Please select a video for processing !', font=('Arial'), foreground='red')


window = Tk()
window.geometry('800x400')

productName = Label(window, text='POTTY ROAD', font=('Arial', 30, 'bold'))
productName.place(relx=0.5, rely=0.3, anchor='center')

filePathLabel = Label(window, text='')
filePathLabel.place(rely=0.45, relx=0.25)

browseButton = Button(window, text='Select Video', command=browseFile)
browseButton.place(relx=0.4, rely=0.55)


nextButton = Button(window, text='Try Now', command=submitFile)
nextButton.place(relx=0.4, rely=0.65)

videoContainerLabel = Label(window)
videoContainerLabel.place(relx=0.2, rely=0.7)


window.mainloop()