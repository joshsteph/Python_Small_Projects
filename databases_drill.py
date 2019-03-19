import sqlite3

conn = sqlite3.connect('drill1.db')

fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

with conn:
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS tbl_txtFiles(\
                ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                col_txtFile TEXT)')
    conn.commit()
conn.close()


conn = sqlite3.connect('drill1.db')

with conn:
    cur = conn.cursor()
    for i in fileList:
        name = (i,)
        if '.txt' in i:
            cur.execute('INSERT INTO tbl_txtFiles (col_txtFile) VALUES (?)', name)
            conn.commit()
conn.close()

conn = sqlite3.connect('drill1.db')

with conn:
    cur = conn.cursor()
    cur.execute('SELECT col_txtFile FROM tbl_txtFiles')
    rows = cur.fetchall()
    for row in rows:
        print(row)
conn.close()