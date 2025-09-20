import pygame
from pygame.locals import *

pygame.init()
pygame.display.set_caption("Hangman")
screen = pygame.display.set_mode((1200, 800))
bg_image = pygame.image.load('./assets/game-background.jpg')
screen.blit(bg_image, (0,0))

default_font = pygame.font.Font(None, 35)
medium_font = pygame.font.Font(None, 70)
keyboard_font = pygame.font.Font(None, 50)

dark = (16,5,24)
white = (255,255,255)
green = (58,120,97)

def drawWord(dashed_word):
    WordSurface = pygame.Surface((330,75))
    WordSurface.fill(dark)
    UIword = medium_font.render(dashed_word, True, white,dark)
    UIword_width = UIword.get_rect().width
    UIword_height = UIword.get_rect().height
    WordSurface = pygame.Surface((UIword_width + 50,UIword_height + 50))
    WordSurface.fill(dark)
    WordSurface.blit(UIword,(20,20))
    screen.blit(WordSurface, (450,300))
    
def drawScore(best_score):
    UIattemptText = default_font.render(f"Attempts : 0", True, white)
    UIpenaltiesText = default_font.render(f"Penalties : 0", True, white)
    UIscoreText = default_font.render(f"Best : {best_score}", True, white)
    ScoreSurface = pygame.Surface((1200,75))
    ScoreSurface.fill(green)
    ScoreBorder = pygame.Surface((1200,10))
    ScoreBorder.fill(dark)
    screen.blit(ScoreBorder,(0,75))
    screen.blit(ScoreSurface,(0,0))
    screen.blit(UIattemptText,(50,25))
    screen.blit(UIpenaltiesText,(500,25))
    screen.blit(UIscoreText,(950,25))

def drawUI(dashed_word, best_score):
    drawScore(best_score)
    drawWord(dashed_word)
    UIletterContainer = pygame.Rect(0, 610, 1200, 400)
    pygame.draw.rect(screen, green, UIletterContainer)
    
def drawAlphabet():
    letters = {}
    alphabet = 'abcdefghijklmnopqrstuvwxyz'.upper()
    x = 100
    y = 640
    for letter in alphabet:
        letterSurface = pygame.Surface((60,60))
        letterSurface.fill(dark)
        UIletter = keyboard_font.render(letter, True, white, dark)
        button_rect = pygame.Rect(x, y, 60, 60)
        letters[letter] = {"clicked" : False, "UI": UIletter, "surface" : button_rect, "xpos":x, "ypos":y}
        letterSurface.blit(UIletter, (15,15))
        screen.blit(letterSurface, (x,y))
        x += 75
        if letter == "M" :
            y = 715
            x = 100
    return letters

def replaceLetter(letter, xpos, ypos):
    button_surface = pygame.Surface((60, 60))
    button_surface.fill(green)
    letter_render = keyboard_font.render(letter, True, dark)
    letter_rect = letter_render.get_rect(center=(30, 30))
    button_surface.blit(letter_render, letter_rect)
    screen.blit(button_surface, (xpos, ypos))
    return button_surface

def displayMessage(status, random_word, attempts):
    if status == "win" :
        UImodalText = default_font.render(f"YOU WON! You guessed the word : {random_word} in {attempts} attempts.",True, white)
    else :
        UImodalText = default_font.render(f"You LOST! The correct word is: {random_word}",True, white)
    modalSurface = pygame.Surface((800, 200))
    modalSurface.fill(dark)
    modalSurface.blit(UImodalText, (50,50))
    screen.blit(modalSurface, (200,200))

def createButton(text, xpos, ypos):
    button_text = medium_font.render(text, True, white)
    text_rect = button_text.get_rect()
    button_width = text_rect.width + 20
    button_height = text_rect.height + 20
    button_surface = pygame.Surface((button_width,button_height))
    button_surface.fill(dark)
    button_surface.blit(button_text, ((10,10)))
    screen.blit(button_surface, (xpos,ypos))