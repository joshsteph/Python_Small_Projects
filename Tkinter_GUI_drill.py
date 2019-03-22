import tkinter
from tkinter import *


class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(700,250))
        self.master.title('Check Files')
        self.master.config(bg='lightgray')


        self.txtBrowse = Entry(self.master, text = self.varBrowse, font=('Helvetica',16), fg = 'black', bg= 'white', width = 55)
        self.txtBrowse.grid(row= 0, column= 1, padx = (25, 0), pady = (50, 20))

        self.txtBrowse2 = Entry(self.master, text=self.varBrowse2, font=('Helvetica', 16), fg='black', bg='white', width = 55)
        self.txtBrowse2.grid(row= 1, column= 1, padx = (25, 0))

        self.btnBrowse = Button(self.master,text = 'Browse...', width = 13, height = 2, highlightbackground= 'lightgray')
        self.btnBrowse.grid(row= 0, column= 0, padx = (25, 0), pady = (50, 20))

        self.btnBrowse2 = Button(self.master,text = 'Browse...', width = 13, height = 2, highlightbackground= 'lightgray')
        self.btnBrowse2.grid(row= 1, column= 0, padx = (25, 0))

        self.btnCheck = Button(self.master,text = 'Check for files...', width = 13, height = 3, highlightbackground= 'lightgray')
        self.btnCheck.grid(row= 2, column= 0, padx =(25, 0), pady = (20, 0))

        self.btnClose = Button(self.master,text = 'Close Program', width = 13, height = 3, highlightbackground= 'lightgray')
        self.btnClose.grid(row= 2, column= 1, pady = (20, 0), sticky = NE)














if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()