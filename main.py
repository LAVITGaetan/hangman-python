from pygame import QUIT
import UI
import logic

attempts = 0
penalties = 0
bestscore = 0
random_word = logic.getRandomWord()
dashed_word = logic.createPairsWord(random_word)
isRunning = True
finished = False
# TEST
# print(random_word)

UI.drawUI( dashed_word)

letters = UI.drawAlphabet()

while isRunning :
    if dashed_word.count('_') == 0:
        finished = True
        logic.playerWon(random_word, attempts)
        
    if penalties > 11:
        finished = True
        logic.playerLost(random_word, attempts)
        
    for event in UI.pygame.event.get():
        if event.type == UI.pygame.MOUSEBUTTONDOWN:
            for letter, data in letters.items() :
                if data["surface"].collidepoint(event.pos) and not data["clicked"] and not finished:
                    old_dashed_word = dashed_word
                    attempts +=1
                    data["UI"] = UI.replaceLetter(letter, data["xpos"], data["ypos"])
                    data["clicked"] = True
                    if old_dashed_word == dashed_word :
                        penalties += 1
                    dashed_word = logic.checkInput(letter, random_word, attempts, dashed_word, penalties)
        UI.pygame.display.update()
        if event.type == QUIT:
            isRunning = False
    UI.pygame.display.flip()

UI.pygame.quit()