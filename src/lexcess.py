# Copyright 2008 Garrison Benson
#
#    This file is part of Lexcess.
#
#    Lexcess is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Lexcess is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Lexcess.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import with_statement
import random,copy,pickle,datetime


PREPLAY = 0
ACTIVE = 1
PAUSED = 2
DEAD = 3

NUMSCORES = 10

MINWORDLENGTH = 3
MAXLETTERS = 30
INITIALLETTERS = 0
MAXDELAY = 2200 # ms
MINDELAY = 750 # ms
DELAYDIFF = MAXDELAY - MINDELAY
MAXSPEEDSCORE = 400 # number of letters when speed maxes out


letterDist = [('A',9),('B',2),('C',2),('D',4),
              ('E',12),('F',2),('G',3),('H',2),
              ('I',9),('J',1),('K',1),('L',4),
              ('M',2),('N',6),('O',8),('P',2),
              ('Q',1),('R',6),('S',4),('T',6),
              ('U',4),('V',2),('W',2),('X',1),
              ('Y',2),('Z',1)]

def generateLetterBag():
    letterBag = []
    for pair in letterDist:
        letterBag += ([pair[0]]*pair[1])
    return letterBag

def compareScores(s1,s2):
    return s2.score - s1.score

def saveScores():
    with open("scores.dat",'w') as f:
        pickle.dump(SCORELIST,f)




class LexcessGame:
    def __init__(self,gui):
        self.letterList = self.generateLetters(INITIALLETTERS)
        self.letterBag = generateLetterBag()
        self.gui = gui
        self.timedEventId = None
        self.state = PREPLAY
        self.score = 0
        self.letters = 0
        self.letterToggle = True
        self.updateDelay()
    
    
    def tick(self):
        self.timedEventId = None
        self.gui.playTone()
        if self.letterToggle:
            self.addLetter()
        self.letterToggle = not self.letterToggle
        if self.state == ACTIVE: # State may have changed in addLetter
            self.startTimer()
            
    
    def addLetter(self):
        if len(self.letterList) == MAXLETTERS:
            self.lose()
        else:
            letter = random.choice(self.letterBag)
            self.letterList.append(letter)
            self.letterBag.remove(letter)
            
            self.gui.updateGame()
            
    
    def start(self):
        self.state = ACTIVE
        self.gui.updateGame()
        self.startTimer()
    
    def pause(self):
        self.stopTimer()
        self.state = PAUSED
        self.gui.updateGame()
    
    def unpause(self):
        if self.state == PAUSED:
            self.startTimer()
            self.state = ACTIVE
            self.gui.updateGame()
    
    def startTimer(self):
        self.stopTimer()
        self.timedEventId = self.gui.addTimedEvent(self.delay,self.tick)
        #self.timer = Timer(self.delay,self.addLetter)
        #self.timer.start()
            
    def stopTimer(self):
        if self.timedEventId:
            self.gui.cancelTimedEvent(self.timedEventId)
            #self.timer.cancel()
        self.timedEventId = None
    
    def lose(self):
        self.state = DEAD
        self.stopTimer()
        self.gui.endGameSound()
        self.gui.updateGame()
        if len(SCORELIST) < NUMSCORES or self.score > SCORELIST[-1].score:
            name = self.gui.getName()
            if name:
                scoreObject = Score(name,self.score,self.letters)
                SCORELIST.append(scoreObject)
                SCORELIST.sort(compareScores)
                if len(SCORELIST) > NUMSCORES:
                    SCORELIST.pop()
                saveScores()
                self.gui.showScores(scoreObject)
                
    
    # TODO: Clean this method up!
    def enterWord(self,word):
        if (self.state != ACTIVE) or len(word) < MINWORDLENGTH:
            return False
        word = word.upper()
        letterListCopy = copy.copy(self.letterList)
        letterBagCopy = copy.copy(self.letterBag)
        try:
            for letter in word:
                letterListCopy.remove(letter)
                letterBagCopy.append(letter)
        except ValueError,detail:
            return False
        else:
            if word in wordSet:
                self.letterList = letterListCopy
                self.letterBag = letterBagCopy
                numLetters = len(word)
                self.letters += numLetters
                self.score += (numLetters*numLetters)
                self.updateDelay()
                return True
            else:
                return False
    
    def updateDelay(self):
        self.delay = MAXDELAY - ((self.letters*DELAYDIFF)/MAXSPEEDSCORE)
        if self.delay < MINDELAY:
            self.delay = MINDELAY
        self.delay = self.delay / 2
    
    def generateLetters(self,num):
        letterList = []
        for i in range(0,num):
            letterList.append(random.choice(letterBag))
        return letterList


class Score:
    def __init__(self,name,score,letters):
        self.name = name
        self.score = score
        self.letters = letters
        #self.time = time
        self.date = datetime.date.today()


try:
    f = open("scores.dat")
    SCORELIST = pickle.load(f)
    f.close()
    SCORELIST.sort(compareScores)
except IOError:
    SCORELIST = []

with open("wordset.dat") as f:
    wordSet = pickle.load(f)
    