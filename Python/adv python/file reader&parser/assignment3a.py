# This program takes in a text file and parses it to a more readable format

import os.path

# prints animal and their visit separated by the respective stations
def printsection1(animals, station1, station2):
    for animal in animals:
        print(animal,'               ',station1.get(animal, 0),'                  ',station2.get(animal, 0))

# prints animals that have visited the stations more than 4 times    
def printsection2(animals, station1, station2):
    for animal in animals:
        if station2.get(animal, 0)+station1.get(animal, 0) >= 4:
            print(animal)

# prints total visits an animal has made to a station
def printsection3(animals, station1, station2):
    for animal in animals:
        print(animal,'                  ',int(station1.get(animal, 0))+int(station2.get(animal, 0)))

# prints month with most station visits
def printsection4(items):
    import statistics
    most_visits=[]
    for animal, date, station in items:
        most_visits.append(date[0:2]) 

    print(statistics.mode(most_visits))
    
def open_file():
    try:
        filename_in=input("Enter name of the input file: ")
        if os.path.exists(filename_in)==False:
            raise IOError
        filename_out=input("Enter name of the output file: ")
            
        while os.path.exists(filename_out)==True:
            filename_out=input("File exists. Enter name of the output file again: ")
            
        infile=open(filename_in, "r")
        outfile=open(filename_out,'w')
        return infile, outfile
        
    except IOError:
        print("Error opening file - File does not exist - End of program")
        endofprogram = True
        infile.close()
        outfile.close()    
            
    except:
        print("Error opening file - End of program")
        endofprogram = True
        infile.close()
        outfile.close()
        raise    

def write_file(outfile, items, animals, station1, station2):
    # Data gets written to file here
    # Section 1
    outfile.write("Number of times each animal visited each station:\n")
    outfile.write("Animal ID           Station 1           Station 2 \n")        
    printsection1(animals, station1, station2)
    outfile.write("============================================================ \n")
        
    # Section 2
    outfile.write("Animals that visited both stations at least 4 times \n")
    printsection2(animals, station1, station2)
    outfile.write("============================================================ \n")
        
    # Section 3    
    outfile.write("Total number of visits for each animal \n")
    printsection3(animals, station1, station2)
    outfile.write("============================================================ \n")
        
    # Section 4
    outfile.write("Month that has the highest number of visits to the stations \n")
    printsection4(items)
    
def main():
    endofprogram = False
    #Try/except function that opens the program and checks if there is a file with the same name; assigns infile/outfile variables if successful
    infile, outfile = open_file()
    
    # Creation of the required data structures
    station1={}
    station2={}
    items=[]
    animals=[]
    
    # The data structures created here help simplify some code
    animal_s1=[]
    animal_s2=[]
    
    #The following code reads the given file and puts certain output into the required data structures 
    for line in infile:
        if line=='\n' or line[0]=="#":
            continue
        
        data=line.split(":")
        record=tuple(data)
        
        if record[2]=='s1\n':
            animal_s1.append(record[0])
        if record[2]=='s2\n':
            animal_s2.append(record[0])
        
        if record[0] not in animals:
            animals.append(record[0])
        
        items.append(record)
    
    animals.sort()
    
    #the following code is for the dictionaries
    for animal, date, station in items:
        if station=='s1\n':
            station1[animal]=animal_s1.count(animal)
            
        if station=='s2\n':
            station2[animal]=animal_s2.count(animal)
    
    # Redirects print functions as outfile.write functions
    import sys
    sys.stdout=outfile
    
    write_file(outfile, items, animals, station1, station2)
    
    # Closes files
    infile.close()
    outfile.close()    
    
main()