import os
import tkinter as tk
from tkinter import messagebox


class Txt(object):
    def SetValue(data): pass
    def GetValue(self): pass
txt = Txt()
####

def startStatusAnalysis():
    os.system('python StatusAnalysis.py')




mainPanel= tk.Tk()
mainPanel.title('')
mainPanel.geometry('400x500')
mainPanel.configure(background='grey')



w = tk.Label(mainPanel, text="CHOOSE ANALYSIS", font=("Helvetica", 14),background='grey')
w.pack()

w = tk.Label(mainPanel, text="", font=("Helvetica", 16),background='grey')
w.pack()



# create button to open file
openBtn = tk.Button(mainPanel, text='STATUS ANALYSIS', command=startStatusAnalysis, highlightbackground='#3E4149')
openBtn.pack(expand=tk.FALSE, fill=tk.X, side=tk.TOP)




mainPanel.mainloop()