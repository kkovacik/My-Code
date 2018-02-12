import random

class OceanTreasures:
    # constructor method
    def __init__(self):
        self.__board0=["~"]*60
        self.__board1=["~"]*60
        self.__board2=["~"]*60
        self.__board3=["~"]*60
        self.__board4=["~"]*60
        self.__board5=["~"]*60
        self.__board6=["~"]*60
        self.__board7=["~"]*60
        self.__board8=["~"]*60
        self.__board9=["~"]*60
        self.__board10=["~"]*60
        self.__board11=["~"]*60
        self.__board12=["~"]*60
        self.__board13=["~"]*60
        self.__board14=["~"]*60
        
        self.__chests=[]
        while len(self.__chests)!=3:
            # the method here randomly selects the coordinates of the chests
            x=random.randint(0,59)
            y=random.randint(0,14)
            chest=[x, y]
            if chest not in self.__chests:
                self.__chests.append(chest)
    
    # returns the list of chests
    def getChests(self):
        return self.__chests
    
    # returns the number of chests left to find in-game
    def getTreasuresLeft(self):
        return len(self.__chests)
    
    # this method places the sonars so the board is drawn correctly
    def dropSonar(self, x, y, sonar):
        if int(y)==0:    
            self.__board0.insert(int(x), sonar)
            self.__board0.pop(int(x)+1)
        elif int(y)==1:    
            self.__board1.insert(int(x), sonar)
            self.__board1.pop(int(x)+1)
        elif int(y)==2:    
            self.__board2.insert(int(x), sonar)
            self.__board2.pop(int(x)+1)
        elif int(y)==3:    
            self.__board3.insert(int(x), sonar)
            self.__board3.pop(int(x)+1)
        elif int(y)==4:    
            self.__board4.insert(int(x), sonar)
            self.__board4.pop(int(x)+1)
        elif int(y)==5:    
            self.__board5.insert(int(x), sonar)
            self.__board5.pop(int(x)+1)
        elif int(y)==6:    
            self.__board6.insert(int(x), sonar)
            self.__board6.pop(int(x)+1)
        elif int(y)==7:    
            self.__board7.insert(int(x), sonar)
            self.__board7.pop(int(x)+1)
        elif int(y)==8:    
            self.__board8.insert(int(x), sonar)
            self.__board8.pop(int(x)+1)
        elif int(y)==9:    
            self.__board9.insert(int(x), sonar)
            self.__board9.pop(int(x)+1)
        elif int(y)==10:    
            self.__board10.insert(int(x), sonar)
            self.__board10.pop(int(x)+1)
        elif int(y)==11:    
            self.__board11.insert(int(x), sonar)
            self.__board11.pop(int(x)+1)
        elif int(y)==12:    
            self.__board12.insert(int(x), sonar)
            self.__board12.pop(int(x)+1)
        elif int(y)==13:    
            self.__board13.insert(int(x), sonar)
            self.__board13.pop(int(x)+1)
        elif int(y)==14:    
            self.__board14.insert(int(x), sonar)
            self.__board14.pop(int(x)+1)
        
    # Returns a variety of values depending on the arithmetic between the sonars and the chests 
    def checkDistance(self, x, y):
        self.__smallest=62
        self.__location=[]
        # The for loop here iterates until the smalles euclidean distance is found between the sonar and all chests
        for item in self.__chests:
            self.__base=int(abs(item[0]-int(x)))
            self.__height=int(abs(item[1]-int(y)))
            self.__distance=float(((self.__base**2)+(self.__height**2))**(0.5))
            if self.__distance < self.__smallest:
                self.__smallest=self.__distance
                self.__location=item
        
        self.__dist_x=int(abs(self.__location[0]-int(x)))
        self.__dist_y=int(abs(self.__location[1]-int(y)))
        
        # Chest found
        if self.__smallest==0:
            if self.__location in self.__chests:
                self.__chests.remove(self.__location)
                return "0"
        
        # if x is the smaller euclidean distance
        elif int(self.__dist_x) <= int(self.__dist_y):
            # if x is 0 the y distance is returned instead
            if self.__dist_x==0 and int(self.__dist_y) <=5:
                return -int(self.__dist_y)
            # if x coordinate is not 0
            elif self.__dist_x in range(1, 10) and int(self.__dist_y) <=5:
                return int(self.__dist_x)
            # if both are out of range
            else:
                return False 
        
        # same as above elif statement
        elif int(self.__dist_y) <= int(self.__dist_x):
            if self.__dist_y==0 and int(self.__dist_x)<=9:
                return int(self.__dist_x)
            elif self.__dist_y in range(1, 6) and int(self.__dist_x)<=9:
                return -int(self.__dist_y)
            else:
                return False
        
        # for whatever other input a user may try
        else:
            return False
    
    def getDist(self, entry):
        value=self.checkDistance(int(entry[0]), int(entry[1]))
        if value=="0":
            return "X"
        elif value>0:
            return str(value)
        elif value<0:
            if value==-1:
                return "a"
            elif value==-2:
                return "b"
            elif value==-3:
                return "c"
            elif value==-4:
                return "d" 
            elif value==-5:
                return "e"
            else:
                return "O"
        else:
            return "O"    
    
    # draws the game board along with coordinates
    def drawBoard(self):
        print("             1         2         3         4         5         ")
        print("   012345678901234567890123456789012345678901234567890123456789")
        print(" 0 "+"".join(self.__board0)+" 0")
        print(" 1 "+"".join(self.__board1)+" 1")
        print(" 2 "+"".join(self.__board2)+" 2")
        print(" 3 "+"".join(self.__board3)+" 3")
        print(" 4 "+"".join(self.__board4)+" 4")
        print(" 5 "+"".join(self.__board5)+" 5")
        print(" 6 "+"".join(self.__board6)+" 6")
        print(" 7 "+"".join(self.__board7)+" 7")
        print(" 8 "+"".join(self.__board8)+" 8")
        print(" 9 "+"".join(self.__board9)+" 9")
        print("10 "+"".join(self.__board10)+" 10")
        print("11 "+"".join(self.__board11)+" 11")
        print("12 "+"".join(self.__board12)+" 12")
        print("13 "+"".join(self.__board13)+" 13")
        print("14 "+"".join(self.__board14)+" 14")
        print("             1         2         3         4         5         ")
        print("   012345678901234567890123456789012345678901234567890123456789")
        
    def help(self):
        print("Welcome to Ocean Treasures!\n")
        print("The objective of this game is to locate the 3 sunken treasures using the 20 given sonars.\n")
        print("First, you will be asked at which coordinates you would like to drop a sonar, x[0-59] followed by y[0-14].")
        print("Once the sonar is dropped, a gameboard will appear, and a character will appear at the selected location")
        print("pointing you towards the location of the nearest treasure. (x-axis=0-9 units) (y-axis=a-e units; a=1, b=2, c=3, etc.)")
        print("It should be noted that which the character the sonar will display will be that of the smaller distance between axes.\n")
        print("This process will repeat until all 3 treasures have been found and/or all 20 sonars have been used.")
        print("You may end the game at any time by selecting inputting 'Q' in the prompt.\n")