# import necessary tools
import pygame as pg
import tkinter as tk
import random
import math

# CONSTANTS
WINSIZE = [640, 480]
WINCENTER = [320, 240]
white = 255, 240, 200
black = 20, 20, 40
# Set initial screen
pg.init()
screen = pg.display.set_mode(WINSIZE)
pg.display.set_caption("Rock Paper Scissors!")
screen.fill(black)
# Pre-defining variables
list1 = ['rock', 'paper', 'scissor']
choicePlayer = 'filter'
choicePC = 'filter2'
font = pg.font.SysFont('comicsans', 30)
# Constants(Counts)
winPC = 0
winPlayer = 0
lostPC = 0
lostPlayer = 0
totalGames = 0
ties = 0


def main():
    # done = 0
    run = True
    while run:
        redrawWindow()
        pg.display.update()
        for event in pg.event.get():
            pos = pg.mouse.get_pos()

            if event.type == pg.QUIT:
                run = False
                pg.quit()
                # sys.exit()
                quit()

            if event.type == pg.MOUSEBUTTONDOWN:
                if greenButton.isOver(pos):
                    print('clicked the button')
                    action()
                    game_loop()
                if quitButton.isOver(pos):
                    print('Exited game')
                    quitGame()

            if event.type == pg.MOUSEMOTION:
                if greenButton.isOver(pos):
                    greenButton.color = (255, 0, 0)
                else:
                    greenButton.color = (0, 255, 0)
                if quitButton.isOver(pos):
                    quitButton.color = (0, 255, 0)
                else:
                    quitButton.color = (255, 0, 0)


def quitGame():
    pg.quit()


# if __name__ == "__main__":
class button():
    # reference from 'Tech with Tim (Youtube)'
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, screen, outline=None):
        # Call this method to draw the button on the screen
        if outline:
            pg.draw.rect(screen, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pg.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pg.font.SysFont('comicsans', 18)
            text = font.render(self.text, 1, (0, 0, 0))
            screen.blit(text, (
            self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False


def redrawWindow():
    # screen.fill(black)
    greenButton.draw(screen, (0, 0, 0))
    quitButton.draw(screen, (0, 0, 0))


greenButton = button((0, 255, 0), 175, 150, 300, 150, 'START GAME')
quitButton = button((255, 0, 0), 600, 15, 35, 35, 'X')
rock = button((255, 255, 255), 170, 350, 90, 90, 'ROCK')
paper = button((255, 255, 255), 270, 350, 90, 90, 'PAPER')
scissor = button((255, 255, 255), 370, 350, 90, 90, 'SCISSOR')
rockPC = button((255, 255, 255), 170, 190, 90, 90, 'ROCK')
paperPC = button((255, 255, 255), 270, 190, 90, 90, 'PAPER')
scissorPC = button((255, 255, 255), 370, 190, 90, 90, 'SCISSOR')
label1 = button((255, 255, 255), 30, 30, 70, 30, 'Wins:')
label1a = button((255, 255, 255), 100, 30, 45, 30, '')
label2 = button((255, 255, 255), 30, 60, 70, 30, 'Losts:')
label2a = button((255, 255, 255), 100, 60, 45, 30, '')
label3 = button((255, 255, 255), 30, 90, 140, 30, 'Total Games:')
label3a = button((255, 255, 255), 170, 90, 45, 30, '')
label4 = button((255, 255, 255), 255, 140, 120, 30, 'Random')
label5 = button((255, 255, 255), 255, 300, 120, 30, 'Click One')
labelPC = button((255, 255, 255), 30, 140, 120, 30, 'Computer:')
labelPlayer = button((255, 255, 255), 30, 300, 120, 30, 'You:')
testingLable = button((255, 255, 255), 120, 120, 120, 120, 'Testing')
label6 = button((255, 255, 255), 147, 45, 70, 30, 'Ties:')
label6a = button((255, 255, 255), 217, 45, 45, 30, '')
results = button((255, 255, 255), 500, 407, 120, 30, 'Results')
retryButton = button((255, 255, 255), 350, 407, 120, 40, 'Retry')
resultsResults = button((255, 255, 255), 260, 60, 120, 40, 'Results')
resultsWins = button((255, 255, 255), 260, 120, 120, 40, 'Wins:')
resultsWins2 = button((255, 255, 255), 230, 120, 45, 40, '')
resultsLosts = button((255, 255, 255), 260, 180, 120, 40, 'Losts:')
resultsLosts2 = button((255, 255, 255), 300, 180, 45, 40, '')
resultsTotalgames = button((255, 255, 255), 220, 240, 200, 40, 'Total Games:')
resultsTotalgames2 = button((255, 255, 255), 300, 240, 45, 40, '')
resultsPercentage = button((255, 255, 255), 190, 300, 260, 40, 'Win percentage:        %')
resultsPercentage2 = button((255, 255, 255), 300, 300, 45, 40, '     ')
exitButton = button((255, 255, 255), 150, 407, 120, 40, 'Exit')


def drawGameWindow():
    screen.fill(black)
    rock.draw(screen, (0, 0, 0))
    paper.draw(screen, (0, 0, 0))
    scissor.draw(screen, (0, 0, 0))
    quitButton.draw(screen, (0, 0, 0))
    rockPC.draw(screen, (0, 0, 0))
    paperPC.draw(screen, (0, 0, 0))
    scissorPC.draw(screen, (0, 0, 0))
    label1.draw(screen, (0, 0, 0))
    label1a.draw(screen, (0, 0, 0))
    label2.draw(screen, (0, 0, 0))
    label2a.draw(screen, (0, 0, 0))
    label3.draw(screen, (0, 0, 0))
    label3a.draw(screen, (0, 0, 0))
    label4.draw(screen, (0, 0, 0))
    label5.draw(screen, (0, 0, 0))
    labelPC.draw(screen, (0, 0, 0))
    labelPlayer.draw(screen, (0, 0, 0))
    label6.draw(screen, (0, 0, 0))
    label6a.draw(screen, (0, 0, 0))
    results.draw(screen, (0, 0, 0))


def checkWin(choicePlayerb, choicePCb, winPCb, winPlayerb, totalGamesb, lostPlayerb, lostPCb):
    global winPC
    global winPlayer
    global totalGames
    global lostPC
    global lostPlayer
    global ties

    if choicePlayerb == 'rock' and choicePCb == 'paper':
        winPC = winPC + 1
        lostPlayer += 1
        totalGames += 1
    if choicePlayerb == 'rock' and choicePCb == 'scissor':
        winPlayer += 1
        lostPC += 1
        totalGames += 1
    if choicePlayerb == 'rock' and choicePCb == 'rock':
        totalGames += 1
        ties += 1
        print('TIED')
    if choicePlayerb == 'paper' and choicePCb == 'paper':
        totalGames += 1
        ties += 1
        print('TIED')
    if choicePlayerb == 'paper' and choicePCb == 'rock':
        winPlayer += 1
        lostPC += 1
        totalGames += 1
    if choicePlayerb == 'paper' and choicePCb == 'scissor':
        winPC += 1
        lostPlayer += 1
        totalGames += 1
    if choicePlayerb == 'scissor' and choicePCb == 'paper':
        winPlayer += 1
        lostPC += 1
        totalGames += 1
    if choicePlayerb == 'scissor' and choicePCb == 'rock':
        winPC += 1
        lostPlayer += 1
        totalGames += 1
    if choicePlayerb == 'scissor' and choicePCb == 'scissor':
        totalGames += 1
        ties += 1
        print('TIED')


def score(score, x, y):
    text = font.render("" + "{:.0f}".format(int(score)), 1, (0, 0, 0))
    screen.blit(text, (x, y))


def game_loop():
    run = False
    run2 = True
    while run2:
        drawGameWindow()
        pg.display.update()
        for event in pg.event.get():
            pos = pg.mouse.get_pos()

            if event.type == pg.QUIT:
                run2 = False
                pg.quit()
                quit()

            if event.type == pg.MOUSEBUTTONDOWN:
                if rock.isOver(pos):
                    print('You chosed ROCK!')
                    choicePlayer = 'rock'
                    choicePC = random.choice(list1)
                    checkWin(choicePlayer, choicePC, winPC, winPlayer, totalGames, lostPlayer, lostPC)
                    print(totalGames)
                if paper.isOver(pos):
                    print('You chosed PAPER!')
                    choicePlayer = 'paper'
                    choicePC = random.choice(list1)
                    checkWin(choicePlayer, choicePC, winPC, winPlayer, totalGames, lostPlayer, lostPC)
                    print(totalGames)
                if scissor.isOver(pos):
                    print('You chosed SCISSOR!')
                    choicePlayer = 'scissor'
                    choicePC = random.choice(list1)
                    checkWin(choicePlayer, choicePC, winPC, winPlayer, totalGames, lostPlayer, lostPC)
                    print(totalGames)
                if quitButton.isOver(pos):
                    print('Exited game')
                    quitGame()
                if results.isOver(pos):
                    print('Checking results')
                    resultsCheck()

            if event.type == pg.MOUSEMOTION:
                if rock.isOver(pos):
                    rock.color = (255, 0, 0)
                else:
                    rock.color = (0, 255, 0)
                if paper.isOver(pos):
                    paper.color = (255, 0, 0)
                else:
                    paper.color = (0, 255, 0)
                if scissor.isOver(pos):
                    scissor.color = (255, 0, 0)
                else:
                    scissor.color = (0, 255, 0)
                if quitButton.isOver(pos):
                    quitButton.color = (0, 255, 0)
                else:
                    quitButton.color = (255, 0, 0)
                if results.isOver(pos):
                    results.color = (0, 255, 0)
                else:
                    results.color = (255, 0, 0)

        score(winPlayer, 110, 20)
        score(lostPlayer, 110, 50)
        score(totalGames, 180, 80)
        score(ties, 227, 35)
        pg.display.update()


def drawResults():
    resultsResults.draw(screen, (0, 0, 0))
    resultsWins.draw(screen, (0, 0, 0))
    resultsLosts.draw(screen, (0, 0, 0))
    resultsTotalgames.draw(screen, (0, 0, 0))
    resultsPercentage.draw(screen, (0, 0, 0))
    retryButton.draw(screen, (0, 0, 0))
    exitButton.draw(screen, (0, 0, 0))


# if totalGames != 0 :
# percentage = winPlayer  / totalGames

def resultsCheck():
    run2 = False
    run3 = True
    global winPC
    global winPlayer
    global totalGames
    global lostPC
    global lostPlayer
    global ties
    while run3:
        screen.fill(black)
        drawResults()
        pg.display.update()
        for event in pg.event.get():
            pos = pg.mouse.get_pos()

            if event.type == pg.QUIT:
                run3 = False
                pg.quit()
                quit()

            if event.type == pg.MOUSEBUTTONDOWN:
                if retryButton.isOver(pos):
                    print('Game Start!')
                    run2 = True
                    run3 = False

                    # clear score, set all scores to 0
                    winPC = 0
                    winPlayer = 0
                    lostPC = 0
                    lostPlayer = 0
                    totalGames = 0
                    ties = 0
                    game_loop()

                if exitButton.isOver(pos):
                    print('Exited game')
                    quitGame()

            if event.type == pg.MOUSEMOTION:
                if retryButton.isOver(pos):
                    retryButton.color = (255, 0, 0)
                else:
                    retryButton.color = (0, 255, 0)
                if exitButton.isOver(pos):
                    exitButton.color = (0, 255, 0)
                else:
                    exitButton.color = (255, 0, 0)

        score(winPlayer, 350, 115)
        score(lostPlayer, 350, 175)
        score(totalGames, 385, 235)
        score((winPlayer / totalGames) * 100, 365, 295)
        pg.display.update()


def action():
    print("Action activated!")


main()

