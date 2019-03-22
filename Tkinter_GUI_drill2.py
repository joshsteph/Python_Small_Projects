import tkinter
from tkinter import *
import tkinter as tk
import os, sys
from tkinter.filedialog import askdirectory


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, *kwargs)

        self.master = master
        self.master.resizable(width=True, height=False)
        self.master.geometry('{}x{}'.format(600,200))
        self.master.title('Select Directory')
        self.master.config(bg='lightgray')


        self.lblDisplay = Label(self.master,text='Click below to choose your directory', font=('Helvetica',14),fg = 'black', bg= 'lightgray')
        self.lblDisplay.pack(pady= (40,20))

        self.btnBrowse = Button(self.master,text = 'Browse...', width = 10, height = 2, command = self.btnBrowseClk)
        self.btnBrowse.pack()

        self.lblDisplay2 = Label(self.master, text='', font=('Helvetica', 14), fg='black', bg='lightgray')
        self.lblDisplay2.pack(pady=(20, 0))

    def btnBrowseClk(self):
        dirname = askdirectory(initialdir=os.getcwd(), title='Please select a directory')
        if len(dirname) > 0:
            self.lblDisplay2.config(text = 'You selected: {}'.format(dirname))

        else:
            dirname = os.getcwd()
            self.lblDisplay2.config(text='No directory selected. Click "Browse..." to choose.')













if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()