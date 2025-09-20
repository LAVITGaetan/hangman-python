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

def drawUI(dashed_word):
    UIletterContainer = pygame.Rect(0, 550, 1200, 400)
    UIattemptText = default_font.render(f"Attempts : 0", True, (255, 255,255))
    UIpenaltiesText = default_font.render(f"Penalties : 0", True, (255, 255,255))
    UIscoreText = default_font.render(f"Best : 0", True, (255, 255,255))
    UIword = medium_font.render(dashed_word, True, (255, 255,255),(16,5,24))
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
    
def drawAlphabet():
    letters = {}
    alphabet = 'abcdefghijklmnopqrstuvwxyz'.upper()
    x = 100
    y = 600
    for letter in alphabet:
        letterSurface = pygame.Surface((60,60))
        letterSurface.fill((16,5,24))
        UIletter = keyboard_font.render(letter, True, (255,255,255), (16,5,24))
        button_rect = pygame.Rect(x, y, 60, 60)
        letters[letter] = {"clicked" : False, "UI": UIletter, "surface" : button_rect, "xpos":x, "ypos":y}
        letterSurface.blit(UIletter, (15,15))
        screen.blit(letterSurface, (x,y))
        x += 75
        if letter == "M" :
            y = 700
            x = 100
    return letters

def replaceLetter(letter, xpos, ypos):
    button_surface = pygame.Surface((60, 60))
    button_surface.fill((58, 120, 97))
    letter_render = keyboard_font.render(letter, True, (16, 5, 24))
    letter_rect = letter_render.get_rect(center=(30, 30))
    button_surface.blit(letter_render, letter_rect)
    screen.blit(button_surface, (xpos, ypos))
    return button_surface

def displayMessage(status, random_word, attempts):
    if status == "win" :
        UImodalText = default_font.render(f"YOU WON! You guessed the word : {random_word} in {attempts} attempts.",True, (255,255,255))
    else :
        UImodalText = default_font.render(f"You LOST! The correct word is: {random_word}",True, (255,255,255))
    modalSurface = pygame.Surface((800, 200))
    modalSurface.fill((16,5,24))
    modalSurface.blit(UImodalText, (50,50))
    screen.blit(modalSurface, (200,200))

def createButton(text, xpos, ypos):
    button_text = medium_font.render(text, True, (255,255,255))
    text_rect = button_text.get_rect()
    button_width = text_rect.width + 20
    button_height = text_rect.height + 20
    button_surface = pygame.Surface((button_width,button_height))
    button_surface.fill((0,0,0))
    button_surface.blit(button_text, ((10,10)))
    screen.blit(button_surface, (xpos,ypos))