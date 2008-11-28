from Tkinter import *
from tkSimpleDialog import Dialog
import Tix

HEADINGFONT = ("Helvetica","10","bold")
SCOREFONT = ("Helvetica","10")
HIGHLIGHTEDFONT = ("Helvetica","10","bold")

class NamePrompter(Dialog):
    
    def body(self, master):
        Label(master, text="Enter your name:").grid(row=0,sticky=W)
        self.entry = Entry(master)
        self.entry.grid(row=1,sticky=W)
        return self.entry # initial focus
    
    def buttonbox(self):
        box = Frame(self)
        w = Button(box, text="OK", width=10, command=self.ok, default=ACTIVE)
        w.pack(side=LEFT, padx=5, pady=5)
        self.bind("<Return>", self.ok)
        box.pack()

    def apply(self):
        self.result = self.entry.get()


class ScoreWindow(Dialog):
    def __init__(self,parent,scores,cols,highlighted=None):
        self.scores = scores
        self.cols = cols
        self.highlighted = highlighted
        Dialog.__init__(self,parent,"High Scores")
        
    
    def body(self,master):
        
        master.bind("<KeyPress-Escape>",self.close)
                
        for i,col in enumerate(self.cols):
            Label(master,text=col.capitalize(),font=HEADINGFONT).grid(row=0,column=i+1,sticky=W)
        
        for i,score in enumerate(self.scores):
            if score == self.highlighted:
                font=HIGHLIGHTEDFONT
            else:
                font=SCOREFONT
            Label(master,text=str(i+1),font=font).grid(row=i+1,column=0,sticky=W)
            
            for j,col in enumerate(self.cols):
                Label(master,text=str(getattr(score,col)),font=font).grid(row=i+1,column=j+1,sticky=W)
                
        return master
    
    def close(self,event=None):
        self.destroy()
    
    def buttonbox(self):
        pass
