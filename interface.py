import pygame
from pygame.locals import *
import random
import datetime
import os

# Get random word from file
try:
    with open("words.txt", "r") as file:
        randomWord = random.choice([line.strip() for line in file]).upper()
        print(randomWord)
except FileNotFoundError as e:
    print(e)

# Create Word with _
def createPairsWord():
    pairString = ""
    for _ in randomWord:
        pairString += '_ '
    return pairString

attempts = 0
penalties = 0
bestscore = 0
currentWord = createPairsWord()

pygame.init()
pygame.display.set_caption("Hangman")

bg_image = pygame.image.load('./assets/game-background.jpg')
screen = pygame.display.set_mode((1200, 800))
screen.blit(bg_image, (0,0))
default_font = pygame.font.Font(None, 35)
medium_font = pygame.font.Font(None, 70)
keyboard_font = pygame.font.Font(None, 50)

UIattemptText = default_font.render(f"Attempts : {attempts}", True, (255, 255,255))
UIpenaltiesText = default_font.render(f"Penalties : {penalties}", True, (255, 255,255))
UIscoreText = default_font.render(f"Best : {bestscore}", True, (255, 255,255))
UIword = medium_font.render(f"{currentWord}", True, (255, 255,255),(16,5,24))
UIletterContainer = pygame.Rect(0, 550, 1200, 400)

def drawUI():
    ScoreSurface = pygame.Surface((1200,75))
    ScoreSurface.fill((58,120,97))
    ScoreBorder = pygame.Surface((1200,10))
    ScoreBorder.fill((0,0,0))
    screen.blit(ScoreBorder,(0,75))
    screen.blit(ScoreSurface,(0,0))
    screen.blit(UIattemptText,(50,25))
    screen.blit(UIpenaltiesText,(500,25))
    screen.blit(UIscoreText,(950,25))
    WordSurface = pygame.Surface((300,100))
    WordSurface.fill((16,5,24))
    screen.blit(UIword,(500,300))
    pygame.draw.rect(screen, (58,120,97), UIletterContainer)
drawUI()

letters = {}
def checkInput(letter):
    global attempts
    attempts += 1
    UIattemptText = default_font.render(f"Attempts : {attempts}", True, (255, 255,255),(58,120,97))
    screen.blit(UIattemptText,(50,25))
    if letter in randomWord:
            for i in range(len(randomWord)):
                if(letter == randomWord[i]):
                    global currentWord
                    currentWord = currentWord.split(' ')
                    currentWord[i] = letter
                    currentWord = ' '.join(currentWord)
                    UIword = medium_font.render(f"{currentWord}", True, (255, 255,255),(16,5,24))
                    screen.blit(UIword,(500,300))
    else :
        global penalties
        penalties += 1
        UIpenaltiesText = default_font.render(f"Penalties : {penalties}", True, (255, 255,255),(58,120,97))
        screen.blit(UIpenaltiesText,(500,25))

def drawAlphabet():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'.upper()
    x = 100
    y = 600
    for letter in alphabet:
        letterSurface = pygame.Surface((60,60))
        letterSurface.fill((16,5,24))
        UIletter = keyboard_font.render(letter, True, (255,255,255), (16,5,24))
        button_rect = pygame.Rect(x, y, 60, 60)
        letters[letter] = {"clicked" : False, "UI": UIletter, "surface" : button_rect, "x":x, "y":y}
        letterSurface.blit(UIletter, (15,15))
        screen.blit(letterSurface, (x,y))
        x += 75
        if letter == "M" :
            y = 700
            x = 100
drawAlphabet()

def displayMessage(status):
    if status == "win" :
        UImodalText = default_font.render(f"YOU WON! You guessed the word : {randomWord} in {attempts} attempts.",True, (255,255,255))
    else :
        UImodalText = default_font.render(f"You LOST! The correct word is: {randomWord}",True, (255,255,255))
        
    modalSurface = pygame.Surface((800, 200))
    modalSurface.fill((16,5,24))
    modalSurface.blit(UImodalText, (50,50))
    screen.blit(modalSurface, (200,200))

def writeBestScore():
    with open("best_scores.txt", "a+") as scoreFile:
        currentDate = datetime.datetime.now()
        formatedScore = f"{attempts} {currentDate}\n"
        scoreFile.write(formatedScore)

# Check Best Score
def checkBestScore():
    try:
        with open("best_scores.txt", "r") as scoreFile:
            file_size = os.stat("best_scores.txt").st_size
            if file_size == 0:
                writeBestScore()
            else:
                currentBest = None
                for line in scoreFile:
                    if currentBest == None:
                        currentBest = line.split(' ')
                    elif int(currentBest[0]) > int(line.split(' ')[0]):
                        currentBest = line.split(' ')
                if attempts < int(currentBest[0]):
                    writeBestScore()
    except FileNotFoundError as e:
        print(e)

# Winning Logic
def playerWon():
    displayMessage("win")
    checkBestScore()

# Losing Logic
def playerLost():
    displayMessage("lose")

isRunning = True
while isRunning :
# Check game status
    if currentWord.count('_') == 0:
        playerWon()
    if penalties > 11:
        playerLost()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            for letter, data in letters.items() :
                if data["surface"].collidepoint(event.pos) and not data["clicked"]:
                    button_surface = pygame.Surface((60, 60))
                    button_surface.fill((58, 120, 97))
                    letter_render = keyboard_font.render(letter, True, (16, 5, 24))
                    letter_rect = letter_render.get_rect(center=(30, 30))
                    button_surface.blit(letter_render, letter_rect)
                    screen.blit(button_surface, (data["x"], data["y"]))
                    data["UI"] = button_surface
                    data["clicked"] = True
                    checkInput(letter)
        pygame.display.update()
        if event.type == QUIT:
            isRunning = False
    pygame.display.flip()
    
pygame.quit()