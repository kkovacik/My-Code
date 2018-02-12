import sqlite3
import sys
from vgmethods import *

conn = sqlite3.connect('VG.db')
conn.text_factory = str
c = conn.cursor()

running=True

def main():
    print("Welcome! Please select an option:")
    print("1) Lookup game title info")
    print("2) Search games by console")
    print("3) Search games by rating")
    print("4) Search games by year")
    print("5) Quit")    

    while running:
        prompt = input('--> ')
        if prompt=='1':
            title = input("Enter the full title of the game: ")
            title_srch(c, title)
            
        elif prompt=='2':
            console = input("Select a console [PC / PS4 / XB1 / Wii]: ")
            console_srch(c, console)
            
        elif prompt=='3':
            rating = input("Enter a number (0-5):")
            rating_srch(c, rating)
            
        elif prompt=='4':
            year = input("Enter a year: ")
            year_srch(c, year)
            
        elif prompt=='5':
            break
        
        else:
            print("Invalid input, try again\n")
            
main()