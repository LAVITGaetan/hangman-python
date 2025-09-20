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
    finished = logic.checkGameStatus(penalties, random_word, attempts, dashed_word)
    old_dashed_word = dashed_word
    for event in UI.pygame.event.get():
        if event.type == UI.pygame.MOUSEBUTTONDOWN:
            for letter, data in letters.items() :
                if data["surface"].collidepoint(event.pos) and not data["clicked"] and not finished:
                    attempts +=1
                    data["UI"] = UI.replaceLetter(letter, data["xpos"], data["ypos"])
                    data["clicked"] = True
                    dashed_word = logic.checkInput(letter, random_word, attempts, dashed_word, penalties)
                    if old_dashed_word == dashed_word :
                        penalties += 1
        UI.pygame.display.update()
        if event.type == QUIT:
            isRunning = False
    UI.pygame.display.flip()

UI.pygame.quit()