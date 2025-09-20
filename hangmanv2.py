import random
import datetime
import os

attempts = 0

# Get random word from file
try:
    with open("words.txt", "r") as file:
        randomWord = random.choice([line.strip() for line in file]).upper()
        print(randomWord)
except FileNotFoundError as e:
    print(e)
    
def writeBestScore():
    with open("best_scores.txt", "a+") as scoreFile:
        currentDate = datetime.datetime.now()
        formatedScore = f"{attempts} {currentDate}\n"
        scoreFile.write(formatedScore)
        print(f"Best ever!!! You've guessed {randomWord} in {attempts} attempts.")

# Check Best Score
def checkBestScore():
    try:
        with open("best_scores.txt", "r") as scoreFile:
            file_size = os.stat("best_scores.txt").st_size
            if file_size == 0:
                print("File is empty")
                writeBestScore()                
            else:
                print("File is not empty")
                currentBest = None
                for line in scoreFile:
                    if currentBest == None:
                        currentBest = line.split(' ')
                    elif int(currentBest[0]) > int(line.split(' ')[0]):
                        currentBest = line.split(' ')
                print(f"Current best score is {currentBest}")
                print(f"You've guessed {randomWord} in {attempts} attempts. The record is {currentBest[0]} attempts.")
                if attempts < int(currentBest[0]):
                    writeBestScore()
                else :
                    print("You didnt beat the record, try again")
    except FileNotFoundError as e:
        print(e)
        
# Create Word with _
def createPairsWord():
    pairString = ""
    for _ in randomWord:
        pairString += '_ '
    return pairString

# Ask for input until it's correct
def getInput():
    userInput = input("Guess : ").upper()
    if len(userInput) > 0 and userInput.isalpha():
        global attempts
        attempts += 1
        return userInput
    else:
        print("Entrez un charactère valide")
        return getInput()

# Winning Logic
def playerWon():
    print('You won the game')
    print(f"Correct word : {randomWord}")
    checkBestScore()    
    
# Losing Logic
def playerLost():
    print('You lost the game')
    print(f'The correct word is {randomWord}')
    
# Game Logic
def playGame():
    hiddenWord = createPairsWord()
    penalties = 0
    while True:
        # Check game status
        if hiddenWord.count('_') == 0:
            playerWon()
            break
        if penalties > 11:
            playerLost()
            break
        # Check penalties syntax
        if(penalties < 2):
            print(f"{hiddenWord} / {penalties} penalty")
        else:
            print(f"{hiddenWord} / {penalties} penalties")
        # Ask for input
        userInput = getInput()
        
        # Check input size
        if len(userInput) > 1 :
            if userInput == randomWord:
                playerWon()
                break
            else:
                penalties += 5
                print(f"{userInput} is not correct")
        else:
            if(userInput in randomWord):
                print(f"Found {randomWord.count(userInput)} '{userInput}'")
                for i in range(len(randomWord)):
                    if(userInput == randomWord[i]):
                        hiddenWord = hiddenWord.split(' ')
                        hiddenWord[i] = userInput
                        hiddenWord = ' '.join(hiddenWord)
            else :
                penalties += 1
                print(f"No '{userInput}' found")
playGame()