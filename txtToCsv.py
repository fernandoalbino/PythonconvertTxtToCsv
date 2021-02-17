import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import pandas as pd

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 350, height = 350, bg = '#000', relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='TXT to CSV Conversion Tool', bg = '#c1c1c1', fg='#000')
label1.config(font=('roboto', 18))
canvas1.create_window(175, 50, window=label1)

def getTxt ():
    global read_file
    
    importPath = filedialog.askopenfilename()
    read_file = pd.read_csv(importPath)
    
buttonTxt = tk.Button(text="      Importar o arquivo .txt      ", command=getTxt, bg='blue', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(175, 130, window=buttonTxt)

def convertToCsv ():
    global read_file
    
    export_file_path = filedialog.asksaveasfilename(defaultextension='.csv')
    read_file.to_csv (export_file_path, index = None)

exportAsButtonCsv = tk.Button(text='Exportar Texto para .csv', command=convertToCsv, bg='blue', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(175, 200, window=exportAsButtonCsv)

def exitApplication():
    BoxMsg = tk.messagebox.askquestion ('Exit Application','Tem certeza que desja sair da aplicação',icon = 'warning')
    if BoxMsg == 'yes':
       root.destroy()
     
exitButton = tk.Button (root, text='     Sair     ',command=exitApplication, bg='brown', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(175, 280, window=exitButton)

root.mainloop()