import Tkinter
import scorewindow

root = Tkinter.Tk()
name = scorewindow.NamePrompter(root).result
root.withdraw()

print name