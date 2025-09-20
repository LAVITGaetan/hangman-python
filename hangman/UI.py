import pygame
from pygame.locals import *

pygame.init()
pygame.display.set_caption("Hangman")
screen = pygame.display.set_mode((1200, 800))
bg_image = pygame.image.load('assets/game-background.jpg')
screen.blit(bg_image, (0,0))
screen_width, screen_height = screen.get_size()

default_font = pygame.font.Font(None, 35)
medium_font = pygame.font.Font(None, 70)
keyboard_font = pygame.font.Font(None, 50)

dark = (16,5,24)
white = (255,255,255)
green = (58,120,97)
purple = (106, 84, 183)

def drawWord(dashed_word):
    word_surface = pygame.Surface((330,75))
    word_surface.fill(dark)
    UIword = medium_font.render(dashed_word, True, white,dark)
    word_width = UIword.get_rect().width
    word_height = UIword.get_rect().height
    word_surface = pygame.Surface((word_width + 50,word_height + 50))
    word_surface.fill(dark)
    word_surface.blit(UIword,(20,20))
    screen.blit(word_surface, ((screen_width // 2) - (word_width // 2), (screen_height // 2) - 100))
    
def drawScore(best_score):
    UIattemptText = default_font.render(f"Attempts : 0", True, white)
    UIpenaltiesText = default_font.render(f"Penalties : 0", True, white)
    UIscoreText = default_font.render(f"Best : {best_score}", True, white)
    score_surface = pygame.Surface((1200,75))
    score_surface.fill(green)
    score_border = pygame.Surface((1200,10))
    score_border.fill(dark)
    screen.blit(score_border,(0,75))
    screen.blit(score_surface,(0,0))
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
        letter_surface = pygame.Surface((60,60))
        letter_surface.fill(dark)
        UIletter = keyboard_font.render(letter, True, white, dark)
        button_rect = pygame.Rect(x, y, 60, 60)
        letters[letter] = {"clicked" : False, "UI": UIletter, "surface" : button_rect, "xpos":x, "ypos":y}
        letter_surface.blit(UIletter, (15,15))
        screen.blit(letter_surface, (x,y))
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

def drawButton(text, xpos, ypos):
    button_text = medium_font.render(text, True, white)
    text_size = button_text.get_rect()
    button_width = text_size.width + 20
    button_height = text_size.height + 20
    if xpos == "center":
        xpos = (screen_width // 2 ) - (button_width // 2)
    button_surface = pygame.Surface((button_width,button_height))
    button_surface.fill(purple)
    button_surface.blit(button_text, ((10,10)))
    screen.blit(button_surface, (xpos,ypos))
    
def displayMessage(status, random_word, attempts):
    if status == "win" :
        modal_text = (f"YOU WON! You guessed the word : {random_word} in {attempts} attempts.")
    else :
        modal_text = (f"You LOST! The correct word is: {random_word}")
    UImodalText = medium_font.render(modal_text, True, white)
    text_size = UImodalText.get_rect()
    modal_width = text_size.width + 50
    modal_height = text_size.height + 50
    modal_surface = pygame.Surface((modal_width, modal_height))
    modal_surface.fill(dark)
    modal_surface.blit(UImodalText, (25,25))
    screen.blit(modal_surface, ((screen_width//2) - (modal_width//2),(screen_height//2) - (modal_height//2) - 200))
    drawButton("Play again", "center",(screen_height//2) - (modal_height//2) + 100)