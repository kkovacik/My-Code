#Assignment 4; Kevin Kovacik ; 1376820; Osmar Zaiane

class BattleshipGame:
    def __init__(self):
        import random
        #User Board
        self.__userBoard=[[" "]*10, [" "]*10, [" "]*10, [" "]*10, [" "]*10, [" "]*10, [" "]*10, [" "]*10, [" "]*10, [" "]*10]
        #Computer's Board
        self.__compBoard=[[" "]*10, [" "]*10, [" "]*10, [" "]*10, [" "]*10, [" "]*10, [" "]*10, [" "]*10, [" "]*10, [" "]*10]
        # This board is the board that the user uses to keep track of his/her moves. 
        self.__trackBoard=[[" "]*10, [" "]*10, [" "]*10, [" "]*10, [" "]*10, [" "]*10, [" "]*10, [" "]*10, [" "]*10, [" "]*10]
        
        self.__userShips={"A":5, "B":4, "D":3, "S":3, "P":2}
        self.__compShips={"A":5, "B":4, "D":3, "S":3, "P":2}
    
    def whatShip(self, char):
        if char=="A":
            return "Aircraft Carrier"
        elif char=="B":
            return "Battleship"
        elif char=="D":
            return "Destroyer"
        elif char=="P":
            return "Patrol Boat"
        elif char=="S":
            return "Submarine"
        else:
            return "Invalid Ship"    
    
    def whatRow(self, char):
        chars=["A","B","C","D","E","F","G","H","I","J"]
        if char in chars:
            return int(chars.index(char))
        else:
            return int(char)
        
    def drawBoards(self, hide):
        if hide==True:
            print("   Computer's board:         User's board: ")
            print("   1 2 3 4 5 6 7 8 9 10      1 2 3 4 5 6 7 8 9 10")
            print("A |"+str("|".join(self.__trackBoard[0]))+"|   A |"+str("|".join(self.__userBoard[0]))+"|")
            print("B |"+str("|".join(self.__trackBoard[1]))+"|   B |"+str("|".join(self.__userBoard[1]))+"|")
            print("C |"+str("|".join(self.__trackBoard[2]))+"|   C |"+str("|".join(self.__userBoard[2]))+"|")
            print("D |"+str("|".join(self.__trackBoard[3]))+"|   D |"+str("|".join(self.__userBoard[3]))+"|")
            print("E |"+str("|".join(self.__trackBoard[4]))+"|   E |"+str("|".join(self.__userBoard[4]))+"|")
            print("F |"+str("|".join(self.__trackBoard[5]))+"|   F |"+str("|".join(self.__userBoard[5]))+"|")
            print("G |"+str("|".join(self.__trackBoard[6]))+"|   G |"+str("|".join(self.__userBoard[6]))+"|")
            print("H |"+str("|".join(self.__trackBoard[7]))+"|   H |"+str("|".join(self.__userBoard[7]))+"|")
            print("I |"+str("|".join(self.__trackBoard[8]))+"|   I |"+str("|".join(self.__userBoard[8]))+"|")
            print("J |"+str("|".join(self.__trackBoard[9]))+"|   I |"+str("|".join(self.__userBoard[9]))+"|")
        else:
            print("   Computer's board:         User's board: ")
            print("   1 2 3 4 5 6 7 8 9 10      1 2 3 4 5 6 7 8 9 10")
            print("A |"+str("|".join(self.__compBoard[0]))+"|   A |"+str("|".join(self.__userBoard[0]))+"|")
            print("B |"+str("|".join(self.__compBoard[1]))+"|   B |"+str("|".join(self.__userBoard[1]))+"|")
            print("C |"+str("|".join(self.__compBoard[2]))+"|   C |"+str("|".join(self.__userBoard[2]))+"|")
            print("D |"+str("|".join(self.__compBoard[3]))+"|   D |"+str("|".join(self.__userBoard[3]))+"|")
            print("E |"+str("|".join(self.__compBoard[4]))+"|   E |"+str("|".join(self.__userBoard[4]))+"|")
            print("F |"+str("|".join(self.__compBoard[5]))+"|   F |"+str("|".join(self.__userBoard[5]))+"|")
            print("G |"+str("|".join(self.__compBoard[6]))+"|   G |"+str("|".join(self.__userBoard[6]))+"|")
            print("H |"+str("|".join(self.__compBoard[7]))+"|   H |"+str("|".join(self.__userBoard[7]))+"|")
            print("I |"+str("|".join(self.__compBoard[8]))+"|   I |"+str("|".join(self.__userBoard[8]))+"|")
            print("J |"+str("|".join(self.__compBoard[9]))+"|   J |"+str("|".join(self.__userBoard[9]))+"|")
    
    def cpu_Placement(self, ship, size, x, y, orientation):
        x=int(x)
        y=self.whatRow(y)
        empty=False
        i=0 
        if orientation=="h" or orientation=="H":
            for j in range(0, size):
                k=int(x+j)
                if int(k)>=10:
                    return False
                elif self.__compBoard[y][k]!=" ":
                    return False
                else:
                    empty=True
                
            while i<size and empty==True:
                if self.__compBoard[y][x]==" ":
                    self.__compBoard[y].insert(int(x), ship)
                    self.__compBoard[y].pop(int(x)+1)
                    x=int(x)+1
                    i+=1
                else:
                    return False
                    
        else:
            for j in range(0, size):
                k=int(y+j)
                if int(k)>=10:
                    return False
                elif self.__compBoard[k][x]!=" ":
                    return False
                else:
                        empty=True 
                
            while i<size and empty==True:
                if self.__compBoard[y][x]==" ":
                    self.__compBoard[y].insert(int(x), ship)
                    self.__compBoard[y].pop(int(x)+1)
                    y=int(y)+1
                    i+=1
                else:
                    return False
        return True  
    
    
    def validatePlacement(self, ship, size, x, y, orientation):
        x=int(x)-1
        y=self.whatRow(y)
        empty=False    
        try:    
            i=0
            if orientation=="h" or orientation=="H":
                for j in range(0, size):
                    k=int(x+j)
                    if int(k)>=10:
                        return False
                    elif self.__compBoard[y][k]!=" ":
                        return False
                    else:
                        empty=True
                            
                while i<size and empty==True:
                    if self.__userBoard[y][x]==" ":
                        self.__userBoard[y].insert(int(x), ship)
                        self.__userBoard[y].pop(int(x)+1)
                        i+=1
                        x+=1
                    else:
                        raise
            else:
                for j in range(0, size):
                    k=int(y+j)
                    if int(k)>=10:
                        return False
                    elif self.__compBoard[k][x]!=" ":
                        return False
                    else:
                        empty=True 
                    
                while i<size and empty==True:
                    if self.__userBoard[y][x]==" ":
                        self.__userBoard[y].insert(int(x), ship)
                        self.__userBoard[y].pop(int(x)+1)
                        i+=1
                        y+=1
                    else:
                        raise
            return True
        except:
            print("Cannot place a", self.whatShip(ship),"there. Stern is out of board or collides with another ship.")
            print("Please take a look at the board and try again.")
            input("Hit ENTER to continue")
            return False
        
    
    def getEnemyFleet(self, computer):
        self.__afloat=[]
        self.__sunk=[]        
        if computer==True:
            for ship, hits in self.__userShips.items():
                if hits==0:
                    self.__sunk.append(self.whatShip(ship))
                else:
                    self.__afloat.append(self.whatShip(ship))
            self.__afloat.sort()
            self.__sunk.sort()
            return [self.__afloat, self.__sunk]
        else:
            for ship, hits in self.__compShips.items():
                if hits==0:
                    self.__sunk.append(self.whatShip(ship))
                else:
                    self.__afloat.append(self.whatShip(ship))
            self.__afloat.sort()
            self.__sunk.sort()            
            return [self.__afloat, self.__sunk]          
    
    def checkWinning(self, computer):
        if computer==True:
            for ship, hits in self.__userShips.items():
                if hits==0:
                    pass
                else:
                    return False
            return True           
        else:
            for ship, hits in self.__compShips.items():
                if hits==0:
                    pass
                else:
                    return False
            return True                
    
    def makeA_Move(self, computer, x, y):
        if computer==True:
            x=int(x)
            self.__y2=y
            y=self.whatRow(y)            
            if self.__userBoard[y][int(x)]==" ":
                print("Miss at", self.__y2, x)
                self.__userBoard[y].insert(int(x)-1, "*")
                return self.__userBoard[y].pop(int(x))
            elif self.__userBoard[y][int(x)] in ["A", "B", "D", "P", "S"]:
                print("Hit at ", self.__y2, x)
                self.__userBoard[y].insert(int(x)-1, "#")
                return self.__userBoard[y].pop(x)                
            elif self.__userBoard[y][x]=="*":
                return "*"
            elif self.__userBoard[y][x]=="#":
                return "#"                
            else:
                return False
        else:
            x=int(x)-1
            self.__y2=y
            y=self.whatRow(y)            
            if self.__compBoard[y][x]==" " and self.__trackBoard[y][x]!="*" and self.__trackBoard[y][x]!="#":
                print("Miss at", self.__y2, int(x+1))
                self.__trackBoard[y].insert(int(x), "*")
                return self.__trackBoard[y].pop(int(x)+1)
            elif self.__compBoard[y][x] in ["A", "B", "D", "P", "S"] and self.__trackBoard[y][x]!="#":
                print("Hit at ", self.__y2, int(x+1))
                self.__trackBoard[y].insert(int(x), "#")
                self.__trackBoard[y].pop(int(x)+1)
                return self.__compBoard[y][x]
            elif self.__trackBoard[y][x]=="*":
                print("Sorry,", self.__y2, int(x+1),"was already played. Try again.")
                return "*"
            elif self.__trackBoard[y][x]=="#":
                print("Sorry,", self.__y2, int(x+1),"was already played. Try again.")
                return "#"                
            else:
                return False         
        
    
    def checkIfSunk(self, computer, ship):
        if computer==True:
            if ship in ["A", "B", "D", "P", "S"]:
                self.__userShips[ship]=int(self.__userShips.get(ship))-1
                if self.__userShips[ship]==0:
                    print(game.whatShip(ship), "sunk")
                    return True
                else:
                    return False
            else: 
                return False
        else:
            if ship in ["A", "B", "D", "P", "S"]:
                self.__compShips[ship]=int(self.__compShips.get(ship))-1
                if self.__compShips[ship]==0:
                    print(game.whatShip(ship), "sunk")
                    return True
                else:
                    return False       
            else:
                    return False
    
# Game initialization
game=BattleshipGame()

import random

# these become valuable later on aas they help with some parts of the game
letters=["A","B","C","D","E","F","G","H","I","J"]
ships=["A", "B", "D", "P", "S"]
s_helper=[["A", 5], ["B", 4], ["D", 3], ["S", 3], ["P", 2]]

# Computer move list, pops the move it made so it doesn't do it again
move_list=[]
place_list=[]
for letter in letters:
    for i in range(0, 10):
        move=[letter, i]
        move_list.append(move)
        place_list.append(move)

print("Welcome to Battleships!")
game.drawBoards(True)

#Player Ship placement
print("Place your ships on the game board by following instructions")
for ship, size in s_helper:
    print("Place", game.whatShip(ship), "of size", size)
    prompt=0
    valid=False 
    #input validation
    while valid==False:    
        prompt=input("Enter coordinates x y (x in [1..10] and y in [A..J]): ")
        entry=prompt.split()
        if len(entry)==2 and (int(entry[1]) in range(1, 11)) and (entry[0] in letters):
            valid=True
        else:
            print("Invalid Input")
    y=entry[0]
    x=entry[1]
    orientation=0
    #input validation again
    while orientation not in ["v","V", "h", "H"]:
        orientation=input("This ship is vertical or horizontal (v,h)? ")
        if orientation not in ["v","V", "h", "H"]:
            print("Invalid input")
    game.validatePlacement(ship, size, x, y, orientation)
    game.drawBoards(True)

ship_check=input("Done placing user ships, hit ENTER to continue")

#Computer Ship placement
for ship, size in s_helper:
    ship_dir=["v", "h"]
    orientation=random.choice(ship_dir)
    size=int(size)
    place=random.choice(place_list)
    x=place[1]
    y=place[0]         
    while game.cpu_Placement(ship, size, x, y, orientation)==False:
        ship_dir=["v", "h"]
        orientation=random.choice(ship_dir)
        size=int(size)
        place=random.choice(place_list)
        x=place[1]
        y=place[0]         
    game.drawBoards(True)
    
while game.checkWinning(False)==False and game.checkWinning(True)==False:
#Where the user makes a move
    prompt=0
    valid=False     
    while valid==False:
        prompt=input("Enter coordinates x y (y in [A..J] and x in [1..10]): ")
        entry=prompt.split()
        if len(entry)==2 and (int(entry[1]) in range(1, 11)) and (entry[0] in letters):
            x=entry[1]
            y=entry[0]
            game.checkIfSunk(False, game.makeA_Move(False, x, y))
            valid=True
        else:
            print("Invalid input, try again")
            valid=False
    game.drawBoards(True)
    print("Ships left:",game.getEnemyFleet(False)[0], "Ships sunk:", game.getEnemyFleet(False)[1])
    
#Computer makes move
    move=random.choice(move_list)
    x=move[1]
    y=move[0]
    game.checkIfSunk(True, game.makeA_Move(True, x, y))
    move_list.remove(move)
    game.drawBoards(True)
    print("Ships left: ", game.getEnemyFleet(False)[0], "Ships sunk:", game.getEnemyFleet(False)[1])   
    
if game.checkWinning(True)==True:
    print("The computer won!")
else:
    print("Congratulations, User won!")