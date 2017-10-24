from random import randint
from Tkinter import *
class PuzzleGame(Canvas):                    
    def __init__(self , master):
        Canvas.__init__(self, master)
        self.pack(fill = BOTH, expand = 1)
        self.master = master
        
        
    def Puzzle1(self): 
        b1= []
        b2=[]
        for i in range (0,9):
            b1.append(str(randint(0,1)))
            b2.append(str(randint(0,1)))
        z = ''.join(b1)     #binary number 1
        y = ''.join(b2)      #binary number 2
            
        x = int(z,2) + int(y,2)     #sum (answer)
        ins = window.create_text((0,0))
        ins.insert(linestart,"Please add the two binary numbers {} + {} and enter the decimal \n representation.".format(z,y))
        ins.pack()
        
    
        



#main
window = Tk()
window.geometry('800x800')
window.title("Puzzle Game")

s = PuzzleGame(window)
s.Puzzle1()

window.mainloop()
