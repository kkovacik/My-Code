import random
from OTmethods import *

def main():    
    game=OceanTreasures()              
    prompt=''
    sonars=0
    done=False
    print(game.getChests())
    while done==False:
        prompt=input("Enter coordinates x y (x in[0..59] and y in [0..14]) (or Q to quit and H for help): ")
        print("\n")
        # Help statement
        if prompt=="H" or prompt.upper=="H":
            game.help()
                    
        # Quit game
        elif prompt=="Q" or prompt.upper=="Q":
            print("The chests were in:", game.getChests())
            print("Thank you for playing Ocean Treasures")
            break          
        
        elif prompt!="Q" or prompt.upper!="Q" or prompt!="H" or prompt.upper!="h":
            entry=prompt.split()
            if len(entry)==2:
                if int(entry[0])>=0 and int(entry[0])<60 and int(entry[1])>=0 and int(entry[1])<15:
                    char=game.getDist(entry)
                    # Sonar gets dropped, gameboard is drawn and a sonar is removed from the players inventory
                    game.dropSonar(entry[0], entry[1], char)
                    game.drawBoard()
                    sonars+=1
                    # Win condition
                    if game.getTreasuresLeft()==0:
                        print("Well Done! you found all the 3 treasure chests using", sonars,"out of 20 sonar devices.")
                        done=True
                    # Loss condition
                    elif sonars==20 and game.getTreasuresLeft()!=0:
                        print("You lost all your sonar devices.")
                        print("The remaining chests were in: ", game.getChests())
                        done=True                   
            else:
                print("Invalid input, try again")        
                
        if done==False:
            print("You have", 20-sonars, "sonar devices available. Treasures found:", int(3-len(game.getChests())), "Still to be found:", len(game.getChests()))
    
main()