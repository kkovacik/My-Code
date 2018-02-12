# Name : Kevin Kovacik
# Id : 1376820
import os.path

# prints animal and their visit separated by the respective stations
def printsection1(animals, station1, station2):
    for animal in animals:
        print(animal,'                ',station1.get(animal, 0),'                  ',station2.get(animal, 0))

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


def main():
    #Try/except block that opens the program and checks if there is a file with the same name
    endofprogram = False
    try:
        filename_in=input("Enter name of the input file: ")
        if os.path.exists(filename_in)==False:
            raise IOError
    
        infile=open(filename_in, "r")    
    
    except IOError:
        print("Error opening file - End of program")
        endofprogram = True
        infile.close()
        outfile.close()    
        
    
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
    
    # Data gets written to file here
    print("Number of times each animal visited each station:")
    print("Animal ID           Station 1           Station 2 ")        
    printsection1(animals, station1, station2)
    print("============================================================ ")
    print("Animals that visited both stations at least 4 times ")
    printsection2(animals, station1, station2)
    print("============================================================ ")
    print("Total number of visits for each animal ")
    printsection3(animals, station1, station2)
    print("============================================================ ")
    print("Month that has the highest number of visits to the stations ")
    printsection4(items)
    
    # Closes files
    infile.close()    
    
main()