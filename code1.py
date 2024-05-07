import pygame, sys, os, button, random, healthbar
from pygame.locals import QUIT
from pygame import mixer

pygame.font.init()
pygame.init()
mixer.init()

comboCounter = 0
countText = ""
comboText = ""

mixer.music.load('maybe.mp3')

score = 0

mixer.music.play()
print(pygame.mixer.music.get_busy)

mixer.music.pause()

musicCounter = 0

lastPressed = ''

clock = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT, 1000)
screen = pygame.display.set_mode((300, 501))

white = (255, 255, 255)
black = (0, 0, 0)
babyBlue = (137, 207, 240)
green = (50, 205, 50)
red = (220, 20, 60)
blue = (30,144,255)

color1 = babyBlue
color2 = babyBlue
color3 = babyBlue
color4 = babyBlue

pygame.mouse.set_visible(0)
pygame.display.set_caption('TemuOsu')

rectHeight = 167
rectWidth = 70

list1 = [0, 1, 2, 3]
place1 = random.choice(list1)
list1.remove(place1)
place2 = random.choice(list1)
list1.remove(place2)
place3= random.choice(list1)
list1.remove(place3)
place4 = random.choice(list1)

ypos1 = 0 - rectHeight*place1
ymover1 = 2
ypos2 = 0 - rectHeight*place2
ymover2 = 2
ypos3 = 0 - rectHeight*place3
ymover3 = 2
ypos4 = 0 - rectHeight*place4
ymover4 = 2

sensorWidth = 72.5

playImg = pygame.image.load('btn.png').convert_alpha()
restartImg = pygame.image.load('replay.png').convert_alpha()
playWidth = playImg.get_width()
restartWidth = restartImg.get_width()
start_button = button.Button(150 - (.25 * playWidth / 2), 400, playImg, 0.3)
restart_button = button.Button(150 - (.25 * restartWidth / 2)-70, 350, restartImg, 1)

titleFont = pygame.font.Font('freesansbold.ttf', 30)
ruleFont = pygame.font.Font('freesansbold.ttf', 15)

lives = 3

passed = False
def drawText(text, color, font, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    screen.blit(textobj, textrect)
    screen.blit(textobj, textrect)

lastTile = 4

playPressed = False
text1 = "Click the respective keys as the"
text12 = "blocks move down."
text2 = "Make sure to line it up with the"
text23 = "sensors at the bottom."
text3 = "The hotkeys are d, f, j, and k."

counter = 100

timeCounter1 = 0
timeCounter2 = 0
timeCounter3 = 0
timeCounter4 = 0

rulesPage = True

firstTimeCounter = 0

musicSeconds = 0

while True:

    # sensorSurfC = pygame.Surface((300, 300))
    # sensorSurfC.fill((0, 0, 0))
    # sensorSurfC.set_alpha(100)

    screen.fill(black)
    if lives <= 0:
        playPressed = False
        rulesPage = False
        screen.fill(black)
        drawText("GAME OVER!", red, titleFont, 55, 50)
        drawText("Score: " + str(score), blue, titleFont, 55, 90)
        mixer.music.pause()
        if restart_button.draw(screen):
            mixer.music.pause()
            lives = 3
            list1 = [0, 1, 2, 3]
            place1 = random.choice(list1)
            list1.remove(place1)
            place2 = random.choice(list1)
            list1.remove(place2)
            place3 = random.choice(list1)
            list1.remove(place3)
            place4 = random.choice(list1)

            ypos1 = 0 - rectHeight * place1
            ypos2 = 0 - rectHeight * place2
            ypos3 = 0 - rectHeight * place3
            ypos4 = 0 - rectHeight * place4

            score = 0
            rulesPage = True

    clock.tick_busy_loop(60)

    if playPressed:
        screen.fill(white)
        # health_bar = healthbar(0, 0, 40, 10, 100)
        drawText(comboText, green, titleFont, 150 - (.25 * playWidth / 2), 50)
        drawText(countText, green, titleFont, 150 - (.25 * playWidth / 2), 78)
        # tiles
        pygame.draw.rect(screen, black, pygame.Rect(4, ypos1, rectWidth, rectHeight))
        pygame.draw.rect(screen, black, pygame.Rect(78, ypos2, rectWidth, rectHeight))
        pygame.draw.rect(screen, black, pygame.Rect(152, ypos3, rectWidth, rectHeight))
        pygame.draw.rect(screen, black, pygame.Rect(226, ypos4, rectWidth, rectHeight))

        drawText(comboText, green, titleFont, 150 - (.25 * playWidth / 2), 50)
        drawText(countText, green, titleFont, 150 - (.25 * playWidth / 2), 78)
        drawText(str(score), blue, titleFont, 280, 5)

        # healthbar
        if (lives == 1):
            pygame.draw.rect(screen, red, pygame.Rect(33, 10, 78, 10))
        if (lives == 2):
            pygame.draw.rect(screen, red, pygame.Rect(111, 10, 78, 10))
            pygame.draw.rect(screen, red, pygame.Rect(33, 10, 78, 10))
        if (lives == 3):
            pygame.draw.rect(screen, red, pygame.Rect(189, 10, 78, 10))
            pygame.draw.rect(screen, red, pygame.Rect(111, 10, 78, 10))
            pygame.draw.rect(screen, red, pygame.Rect(33, 10, 78, 10))
        pygame.draw.rect(screen, black, pygame.Rect(189, 10, 78, 10), 2)
        pygame.draw.rect(screen, black, pygame.Rect(111, 10, 78, 10), 2)
        pygame.draw.rect(screen, black, pygame.Rect(33, 10, 78, 10), 2)

        listNew = [1, 2, 2, 3]
        if ypos1 >= 501:
            passed = True
            ypos1 = 0 - (rectHeight)
            ymover1 = random.choice(listNew)
        if ypos2 >= 501:
            passed = True
            ypos2 = 0 - (rectHeight)
            ymover2 = random.choice(listNew)
        if ypos3 >= 501:
            passed = True
            ypos3 = 0 - (rectHeight)
            ymover3 = random.choice(listNew)
        if ypos4 >= 501:
            passed = True
            ypos4 = 0 - (rectHeight)
            ymover4 = random.choice(listNew)

        # if passed:
        #     list1 = [1, 2, 3, 4]
        #     list1.remove(lastTile)
        #     newTile = random.choice(list1)
        #     print(newTile)
        #     if newTile == 1:
        #         ypos1 = 0 - (rectHeight)
        #         lastTile = 1
        #     if newTile == 2:
        #         ypos2 = 0 - (rectHeight)
        #         lastTile = 2
        #     if newTile == 3:
        #         ypos3 = 0 - (rectHeight)
        #         lastTile = 3
        #     if newTile == 4:
        #         ypos4 = 0 - (rectHeight)
        #         lastTile = 4
        #     passed = False

        ypos1 += ymover1
        ypos2 += ymover2
        ypos3 += ymover3
        ypos4 += ymover4

        # sensor
        sensorSurf1 = pygame.Surface((rectWidth, rectHeight))
        sensorSurf2 = pygame.Surface((rectWidth, rectHeight))
        sensorSurf3 = pygame.Surface((rectWidth, rectHeight))
        sensorSurf4 = pygame.Surface((rectWidth, rectHeight))
        sensorSurf1.fill(color1)
        sensorSurf2.fill(color2)
        sensorSurf3.fill(color3)
        sensorSurf4.fill(color4)
        sensorSurf1.set_alpha(100)
        sensorSurf2.set_alpha(100)
        sensorSurf3.set_alpha(100)
        sensorSurf4.set_alpha(100)
        screen.blit(sensorSurf1, (2, 332))
        screen.blit(sensorSurf2, (77, 332))
        screen.blit(sensorSurf3, (152, 332))
        screen.blit(sensorSurf4, (227, 332))
        pygame.draw.rect(screen, black, pygame.Rect(2, 332, sensorWidth,
                                                    rectHeight), 3)
        pygame.draw.rect(screen, black,
                         pygame.Rect(76.5, 332, sensorWidth, rectHeight), 3)
        pygame.draw.rect(screen, black,
                         pygame.Rect(151, 332, sensorWidth, rectHeight), 3)
        pygame.draw.rect(screen, black,
                         pygame.Rect(225.5, 332, sensorWidth, rectHeight), 3)


    if playPressed == False and rulesPage == True:
        mixer.music.rewind()
        drawText("TemuOsu", white, titleFont, 150 - (.25 * playWidth / 2), 50)
        drawText(text1, white, ruleFont, 110 - (.25 * playWidth / 2), 200)
        drawText(text12, white, ruleFont, 110 - (.25 * playWidth / 2), 215)
        drawText(text2, white, ruleFont, 110 - (.25 * playWidth / 2), 230)
        drawText(text23, white, ruleFont, 110 - (.25 * playWidth / 2), 245)
        drawText(text3, white, ruleFont, 110 - (.25 * playWidth / 2), 260)
        if start_button.draw(screen):
            playPressed = True
    # x, y = pygame.mouse.get_pos()

    musicSeconds += clock.get_time()

    timeCounter1 += clock.get_time()
    timeCounter2 += clock.get_time()
    timeCounter3 += clock.get_time()
    timeCounter4 += clock.get_time()

    comboTimeCounter = 0
    comboTimeCounter += clock.get_time()

    if musicSeconds >= 1000:
        mixer.music.unpause()

    if (comboTimeCounter >= 1000):
        comboText = ""

    if (timeCounter1 >= 1000):
        color1 = babyBlue

    if (timeCounter2 >= 1000):
        color2 = babyBlue

    if (timeCounter3 >= 1000):
        color3 = babyBlue

    if (timeCounter4 >= 1000):
        color4 = babyBlue

    musicCounter += clock.get_time()

    # if (lastPressed == 'd' and ypos1 >= 501):
    #     mixer.music.pause()
    #
    # if (lastPressed == 'f' and ypos2 >= 501):
    #     mixer.music.pause()
    #
    # if (lastPressed == 'j' and ypos3 >= 501):
    #     mixer.music.pause()
    #
    # if (lastPressed == 'k' and ypos4 >= 501):
    #     mixer.music.pause()

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
        elif e.type == pygame.KEYDOWN:
            # unicode representation
            if e.unicode == 'd':
                if ypos1 >= 320 and ypos1 <= 344:
                    if firstTimeCounter == 0:
                        mixer.music.unpause()
                        firstTimeCounter += 1
                    comboCounter += 1
                    comboText = "STREAK"
                    countText = str(comboCounter)
                    color1 = green
                    timeCounter1 = 0
                    musicCounter = 0
                    lastPressed = 'd'
                    score += 1
                else:
                    mixer.music.pause()
                    color1 = red
                    timeCounter1 = 0
                    comboCounter = 0
                    comboText = ""
                    countText = ""
                    lives -= 1
                    musicSeconds = 0

            if e.unicode == 'f':
                if ypos2 >= 320 and ypos2 <= 344:
                    if firstTimeCounter == 0:
                        mixer.music.unpause()
                        firstTimeCounter += 1
                    comboCounter += 1
                    comboText = "STREAK"
                    countText = str(comboCounter)
                    color2 = green
                    timeCounter2 = 0
                    musicCounter = 0
                    lastPressed = 'f'
                    score += 1
                else:
                    mixer.music.pause()
                    color2 = red
                    timeCounter2 = 0
                    comboCounter = 0
                    comboText = ""
                    countText = ""
                    lives -= 1
                    musicSeconds = 0

            if e.unicode == 'j':
                if ypos3 >= 320 and ypos3 <= 344:
                    if firstTimeCounter == 0:
                        mixer.music.unpause()
                        firstTimeCounter += 1
                    comboCounter += 1
                    comboText = "STREAK"
                    countText = str(comboCounter)
                    color3 = green
                    timeCounter3 = 0
                    musicCounter = 0
                    lastPressed = 'j'
                    score += 1
                else:
                    mixer.music.pause()
                    color3 = red
                    timeCounter3 = 0
                    comboCounter = 0
                    comboText = ""
                    countText = ""
                    lives -= 1
                    musicSeconds = 0

            if e.unicode == 'k':
                if ypos4 >= 320 and ypos4 <= 344:
                    if firstTimeCounter == 0:
                        mixer.music.unpause()
                        firstTimeCounter += 1
                    comboCounter += 1
                    comboText = "STREAK"
                    countText = str(comboCounter)
                    color4 = green
                    timeCounter4 = 0
                    musicCounter = 0
                    lastPressed = 'k'
                    score += 1
                else:
                    mixer.music.pause()
                    color4 = red
                    timeCounter4 = 0
                    comboCounter = 0
                    comboText = ""
                    countText = ""
                    lives -= 1
                    musicSeconds = 0

    # screen.blit(sensorSurfC, (0, 0))

    pygame.display.update()
