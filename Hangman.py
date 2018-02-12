# Not my most polished code, but this is a simple hangman program, so it should be easy enough to follow

# Set of words we're using in this game
words=['cow','horse','deer','elephant','lion','tiger','baboon','donkey','fox','giraffe']

#User greeting
print("Welcome to Hangman! Guess the mystery word with less than 6 mistakes!")

word_select=False
while word_select==False:
    try:
        prompt=input("Please enter a number between 1 and 10 to start the game: ")
        
        if 0<=int(prompt)<10:
            word_select=True
        
        elif int(prompt)>=10 or int(prompt)<0:
            print("Given number is out of range! Try again.")
            word_select=False
            
    except ValueError:
            if prompt=="":
                print("Empty input")
            else:
                print("Input must be an integer!")
            word_select=False

#Initial variable settings, helps set up the game
word=words[int(prompt)]
word.split()
solution=list(word)

# So the player doesn't go into the game blind
print("The length of the word is:", len(word))

# More initial variable settings, are some redundant? I hope not.
# "valid_char" is used to test for input errors while "win_con" is used for the victory condition
valid_char=False
win_con=False
count=0
word_board=[]

answer=list(word)
answer.sort()
underscores=len(list(word))*"_"
feedback=list(underscores)

# Game loop
while count!=6 and win_con!=True:
    # Checks if the guessed letter is valid or not
    while valid_char==False:
        try:
            guess=input("Please enter the letter you guess: ")
            if len(guess)!=1 or guess.isalpha()==False:
                raise ValueError
            else:
                valid_char=True
        except:
            print("You need to input a single alphabetic character!")
            valid_char=False
            
# Protocol if the letter is part of the solution
    if guess in solution:
        print("The letter is in the word.")
        instances=answer.count(guess)
        while word_board.count(guess) < instances:
            word_board.append(guess)
        for index, letter in enumerate(solution):
            if letter==guess:
                feedback.insert(index, guess)
                feedback.pop(index+1)
        word_board.sort()
        print("Letters guessed so far", ''.join(feedback))
        # Victory condition
        if word_board==answer:
            print("You have found the mystery word. You win!")
            win_con=True
    
# Protocol if the guessed letter is not part of the solution    
    if guess not in solution:
        count=count+1
        print("The letter is not in the word")
        print("Letters guessed so far", ''.join(feedback))
        if count==1:
            print("------------")
        elif count==2:
            print("------------")
            print("|          | ")            
        elif count==3:
            print("------------")
            print("|          | ")
            print("|           O")            
        elif count==4:
            print("------------")
            print("|          | ")
            print("|           O")
            print("|          / |")            
        elif count==5:
            print("------------")
            print("|          | ")
            print("|           O")
            print("|          / |")
            print("|           |")            
        elif count==6:
            print("------------")
            print("|          | ")
            print("|           O")
            print("|          / |")
            print("|           |")
            print("|          / |")
            print("|")
            print("|")
            print("Too many incorrect guesses. You lost!")
            print("The word was:",word)

# Game Over
print("Game Over!")
input("Press any key to end game.")