
import shutil
import sqlite3
from tkinter import *
import os
from tkinter.filedialog import askdirectory

#---CREATE WIDGET---
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, *kwargs)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(600,300))
        self.master.title('.txt collector')
        self.master.config(bg='lightgray')

        self.lblDisplay = Label(self.master,text ='Pull out .txt files from a source directory and \nplace them in a new directory of your choice.',font =('Helvetica', 14), fg ='black', bg ='lightgray')
        self.lblDisplay.grid(row = 0, column = 1, padx = (30,0), pady = (15, 0), sticky = NW)

        self.txtBrowse = Entry(self.master, text= 'Choose your source directory', font = ('Helvetica',12, 'italic'), bg = 'white', width = 55)
        self.txtBrowse.grid(row = 1, column = 1, padx = (25, 0), pady = (20, 20))
        self.txtBrowse.insert(0, 'Choose source directory...')
        self.txtBrowse.config (fg='grey')


        self.txtBrowse2 = Entry(self.master, text = '', font =('Helvetica', 12, 'italic'), bg ='white', width = 55)
        self.txtBrowse2.grid(row = 2, column = 1, padx = (25, 0))
        self.txtBrowse2.insert(0, 'Choose destination directory...')
        self.txtBrowse2.config(fg='grey')

        self.btnBrowse = Button(self.master,text = 'Browse...', width = 13, height = 2, highlightbackground = 'lightgray', command = self.btnBrowseClk)
        self.btnBrowse.grid(row = 1, column = 0, padx = (25, 0), pady = (20, 20))

        self.btnBrowse2 = Button(self.master,text = 'Browse...', width = 13, height = 2, highlightbackground = 'lightgray', command = self.btnBrowseClk2)
        self.btnBrowse2.grid(row = 2, column= 0, padx = (25, 0))

        self.btnMove = Button(self.master,text = 'Move .txt files...', width = 13, height = 3, highlightbackground = 'lightgray', command = self.moveTxt)
        self.btnMove.grid(row = 3, column = 0, padx = (25, 0), pady = (20, 0))


#---GET SOURCE DIRECTORY---
    def btnBrowseClk(self):
        global srcDir
        srcDir = askdirectory(initialdir=os.getcwd())
        if len(srcDir) > 0:
            self.txtBrowse.delete(0, 'end')
            self.txtBrowse.insert(0, srcDir)
            print('Source directory: ',srcDir)
            return srcDir

        else:
            srcDir = os.getcwd()
            self.txtBrowse.delete(0, 'end')
            self.txtBrowse.insert(0, 'No source directory selected. Click "Browse..." to choose.')



#---GET DESTINATION DIRECTORY---
    def btnBrowseClk2(self):
        global destDir
        destDir = askdirectory(initialdir=os.getcwd())
        if len(destDir) > 0:
            self.txtBrowse2.delete(0, 'end')
            self.txtBrowse2.insert(0, destDir)
            print('Destination directory: ', destDir)

        else:
            destDir = os.getcwd()
            self.txtBrowse2.delete(0, 'end')
            self.txtBrowse2.insert(0,'No destination directory selected. Click "Browse..." to choose.')



#---CREATE DATABASE FOR FILES MOVED TO TRACK AND DISPLAY TO CONSOLE---
    def moveTxt(self):
        conn = sqlite3.connect('final_drill.db')
        with conn:
            cur = conn.cursor()
            cur.execute('CREATE TABLE IF NOT EXISTS tbl_txtFiles(\
                            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                            col_txtFile TEXT, \
                            col_mTimeStamp TEXT)')
            conn.commit()

        path = destDir
        dirs = os.listdir(path)

        with conn:
            cur = conn.cursor()
            for file in dirs:
                if '.txt' in file:
                    fPath = os.path.join(path, file)
                    cur.execute('INSERT INTO tbl_txtFiles (col_txtFile, col_mTimeStamp) VALUES (?, ?)', (file, os.path.getmtime(fPath)))
                    conn.commit()

        with conn:
            cur = conn.cursor()
            cur.execute('SELECT * FROM tbl_txtFiles')
            rows = cur.fetchall()
            for row in rows:
                print(row)
        conn.close()

#---MOVE TXT FILES FROM SOURCE DIRECTORY TO DESTINATION CHOSEN BY USER---
        path = srcDir
        dirs = os.listdir(path)
        destination = destDir

        for file in dirs:
            if '.txt' in file:
                source = os.path.join(path, file)
                shutil.move(source,destination)











if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()