from __future__ import with_statement
from Tkinter import *
import tkMessageBox
from winsound import *
import webbrowser
import scorewindow
import tkSimpleDialog

from lexcess import *

ABOUTMESSAGE = u"Lexcess v0.5\n\u00A9 2008 Garrison Benson\n\nhttp://www.bensonbasement.com"

LETTERFONT = ("Courier","16","bold")
INPUTFONT = ("Helvetica","18")
SCOREFONT = ("Helvetica","10","bold")
SCORETEXT = "Score: "
LETTERSTEXT = "    Letters: "

GOODSOUND = "ding.wav"
BADSOUND = "buzzer.wav"
HIGHTONE = "hightone.wav"
LOWTONE = "lowtone.wav"
LOSESOUND = "gameover.wav"

SCORECOLS = ["name","score","letters"]

class LexcessWindow:
    def __init__(self,master):
        
        self.master = master
        master.title("Lexcess")
        master.resizable(width=FALSE,height=FALSE)
        
        self.letterList = StringVar()
        self.typedWord = StringVar()
        self.score = StringVar()
        #self.letters = StringVar()
        self.effectsOn = IntVar()
        self.effectsOn.set(1)
        self.musicOn = IntVar()
        
        self.toneToggle = False # False is low, True is high
        
        self.frame = Frame(master)
        self.frame.pack()
        
        
        self.scoreLabel = Label(self.frame,textvariable=self.score,font=SCOREFONT,anchor=W)
        #self.lettersLabel = Label(self.frame,textvariable=self.letters,font=SCOREFONT,anchor=W)
        
        self.pauseButton = Button(self.frame,text="Pause",font=SCOREFONT,command=self.pause,width=7)
        
        self.frame.bind("<Destroy>", self.onQuit)
        
        self.lettersBox = Label (self.frame,width=MAXLETTERS,anchor=W,textvariable=self.letterList,font=LETTERFONT)
        
        self.wordBox = Entry(self.frame,textvariable=self.typedWord,font=INPUTFONT)
        self.wordBox.bind("<KeyPress-Return>",self.tryWord)
        
        menubar = Menu(master)
        gameMenu = Menu(menubar,tearoff=0)
        gameMenu.add_command(label="New Game",command=self.newGame)
        gameMenu.add_command(label="High Scores",command=self.showScores)
        gameMenu.add_command(label="Quit",command=master.destroy)
        menubar.add_cascade(label="Game", menu=gameMenu)
        
        soundMenu = Menu(menubar,tearoff=0)
        soundMenu.add_checkbutton(label="Effects",variable=self.effectsOn)
        soundMenu.add_checkbutton(label="Music",variable=self.musicOn)
        menubar.add_cascade(label="Sound", menu=soundMenu)
        
        helpMenu = Menu(menubar,tearoff=0)
        helpMenu.add_command(label="Website",command=self.showWebsite)
        helpMenu.add_command(label="About",command=self.showAbout)
        menubar.add_cascade(label="Help", menu=helpMenu)
        
        master.config(menu=menubar)
        
        
        # Layout:
        self.scoreLabel.grid(row=0,sticky=W,padx=5)
        #self.lettersLabel.grid(row=0,column=1,sticky=W)
        self.pauseButton.grid(row=0,column=2,padx=5,pady=5,sticky=E)
        self.lettersBox.grid(row=1,columnspan=3,sticky=W)
        self.wordBox.grid(row=2,columnspan=3,sticky=EW)
        
        self.loadConfig()
        
        self.newGame()
        self.updateGame()
    
    def loadConfig(self):
        try:
            f = open("config.dat")
            effects,music = pickle.load(f)
            f.close()
            self.effectsOn.set(effects)
            self.musicOn.set(music)
        except IOError:
            self.effectsOn.set(1)
            self.musicOn.set(1)
            
    def saveConfig(self):
        with open("config.dat",'w') as f:
            pickle.dump((self.effectsOn.get(),self.musicOn.get()),f)
        
    
    def newGame(self):
        self.game = LexcessGame(self)
        self.updateGame()
        self.typedWord.set("")
        self.toneToggle = False
        #self.game.start()
    
    def showWebsite(self):
        webbrowser.open_new_tab("http://www.bensonbasement.com")
    
    def showAbout(self):
        tkMessageBox.showinfo("About Lexcess",ABOUTMESSAGE)
        
    
    def startGame(self):
        self.game.start()
        self.wordBox.focus_set()
        
    def restart(self):
        self.newGame()
        self.startGame()
    
    def tryWord(self,event=None):
        success = self.game.enterWord(self.typedWord.get())
        if success:
            self.playSound(GOODSOUND)
        else:
            self.playSound(BADSOUND)
        self.typedWord.set("")
        self.updateGame()
    
    def fixPauseButton(self):        
        if self.game.state == ACTIVE:
            self.pauseButton.config(text="Pause",command=self.pause)
        elif self.game.state == PAUSED:
            self.pauseButton.config(text="Resume",command=self.unpause)
        elif self.game.state == PREPLAY:
            self.pauseButton.config(text="Start",command=self.startGame)
        elif self.game.state == DEAD:
            self.pauseButton.config(text="Restart",command=self.restart)
    
    def updateGame(self):
        if self.game:
            #self.score.set(SCORETEXT + str(self.game.score))
            #self.letters.set(LETTERSTEXT + str(self.game.letters))
            self.score.set(SCORETEXT + str(self.game.score) + LETTERSTEXT + str(self.game.letters))
            if self.game.state == ACTIVE:
                self.letterList.set(''.join(self.game.letterList))
                self.wordBox.config(state=NORMAL)
            else:
                if self.game.state == PAUSED:
                    self.letterList.set(self.makeMessage("paused"))
                elif self.game.state == DEAD:
                    self.letterList.set(self.makeMessage("game over"))
                elif self.game.state == PREPLAY:
                    self.letterList.set("")
                self.wordBox.config(state=DISABLED)
        else:
            self.score.set(SCORETEXT)
            #self.letters.set(LETTERSTEXT)
            self.lettersBox.set("")
            self.wordBox.config(state=DISABLED)
        self.fixPauseButton()
        
    def onQuit(self,event=None):
        self.game.stopTimer()
        self.saveConfig()
        
    def pause(self):
        self.game.pause()
        self.fixPauseButton()
        
    def unpause(self):
        self.game.unpause()
        self.fixPauseButton()
        self.wordBox.focus_set()
        
    def focusEntry(self):
        self.wordBox.focus_set()
    
    def playSound(self,filename):
        if self.effectsOn.get():
            PlaySound(filename,SND_ASYNC)
            
    def playTone(self):
        if self.musicOn.get():
            if self.toneToggle:
                PlaySound(HIGHTONE,SND_ASYNC)
            else:
                PlaySound(LOWTONE,SND_ASYNC)
        self.toneToggle = not self.toneToggle
    
    def makeMessage(self,message):
        result = ["-"]*MAXLETTERS
        mList = [char for char in message]
        sliceStart = (MAXLETTERS - len(message)) / 2
        sliceEnd = sliceStart + len(message)
        result[sliceStart:sliceEnd] = mList
        return ''.join(result)
    
    def getName(self):
        #return tkSimpleDialog.askstring("High Score!","Enter your name",parent=self.frame)
        return scorewindow.NamePrompter(self.master,title="High Score!").result
    
    def addTimedEvent(self,ms,funct):
        return self.master.after(ms,funct)
    
    def cancelTimedEvent(self,identifier):
        self.master.after_cancel(identifier)
    
    def showScores(self,highlighted=None):
        scorewindow.ScoreWindow(self.master,SCORELIST,SCORECOLS,highlighted)
        
    def endGameSound(self):
        self.playSound(LOSESOUND)

root = Tk()
app = LexcessWindow(root)
root.mainloop()
