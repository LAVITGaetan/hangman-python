import random
import datetime
import os
import UI

# Get random word from file
def getRandomWord():
    try:
        with open("words.txt", "r") as file:
            random_word = random.choice([line.strip() for line in file]).upper()
            return random_word
    except FileNotFoundError as e:
        print(e)
        return False

# Create Word with _
def createPairsWord(random_word):
    pairString = ""
    for _ in random_word:
        pairString += '_ '
    return pairString

def checkInput( letter, random_word, attempts, dashed_word, penalties):
    UIattemptText = UI.default_font.render(f"Attempts : {attempts}", True, (255, 255,255),(58,120,97))
    UI.screen.blit(UIattemptText,(50,25))
    if letter in random_word:
            for i in range(len(random_word)):
                if(letter == random_word[i]):
                    dashed_word = dashed_word.split(' ')
                    dashed_word[i] = letter
                    dashed_word = ' '.join(dashed_word)
                    UIword = UI.medium_font.render(f"{dashed_word}", True, (255, 255,255),(16,5,24))
                    UI.screen.blit(UIword,(500,300))
    else :
        UIpenaltiesText = UI.default_font.render(f"Penalties : {penalties + 1}", True, (255, 255,255),(58,120,97))
        UI.screen.blit(UIpenaltiesText,(500,25))
    return dashed_word

# Write best score
def writeBestScore(attempts):
    with open("best_scores.txt", "a+") as scoreFile:
        currentDate = datetime.datetime.now()
        formatedScore = f"{attempts} {currentDate}\n"
        scoreFile.write(formatedScore)
        
        
def getBestScore():
    try:
        with open("best_scores.txt", "r") as scoreFile:
            file_size = os.stat("best_scores.txt").st_size
            if file_size == 0:
                return 0
            else:
                currentBest = None
                for line in scoreFile:
                    if currentBest == None:
                        currentBest = line.split(' ')
                    elif int(currentBest[0]) > int(line.split(' ')[0]):
                        currentBest = line.split(' ')
                return currentBest[0]
    except FileNotFoundError as e:
        print(e)
        return 0

# Check Best Score
def checkBestScore(attempts):
    best_score = 0
    try:
        with open("best_scores.txt", "r") as scoreFile:
            file_size = os.stat("best_scores.txt").st_size
            if file_size == 0:
                writeBestScore(attempts)
                return attempts
            else:
                currentBest = None
                for line in scoreFile:
                    if currentBest == None:
                        currentBest = line.split(' ')
                    elif int(currentBest[0]) > int(line.split(' ')[0]):
                        currentBest = line.split(' ')
                if attempts < int(currentBest[0]):  
                    print(str(attempts) + '222')
                    writeBestScore(attempts)
                    return attempts  
                else:
                    return currentBest[0]
    except FileNotFoundError as e:
        print(e)
        return best_score
        
# Win & Lose logic
def playerWon(random_word, attempts):
    UI.displayMessage("win", random_word, attempts)
    if attempts < int(getBestScore()) or int(getBestScore()) == 0:
        writeBestScore(attempts)

def playerLost(random_word, attempts):
    UI.displayMessage("lose", random_word, attempts)
    
def checkGameStatus(penalties, random_word, attempts, dashed_word):
        if dashed_word.count('_') == 0:
            playerWon(random_word, attempts)
            return True
            
        if penalties > 11:
            playerLost(random_word, attempts)
            return True
            
        return False