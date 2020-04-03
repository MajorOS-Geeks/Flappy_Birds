# For generating random numbers
import random 
# We will use sys.exit to exit the program
import sys
import pygame
# Basic pygame imports
from pygame.locals import * 

# Initialize all pygame's modules
pygame.init()

# Global Variables for the game
SCORE = 0
HIGHEST = 0
SPEED = 0
LEVEL = 1
SCREENWIDTH = 289
SCREENHEIGHT = 511
GROUNDY = SCREENHEIGHT * 0.8
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
MOUSE = pygame.mouse.get_pos()
FONT = pygame.font.SysFont('Arial', 14, 'b')

GAME_SPRITES = {}
GAME_SOUNDS = {}
PLAYER = 'gallery/sprites/bird.png'
BACKGROUND = 'gallery/sprites/level1.png'
PIPE = 'gallery/sprites/pipe.png'

class MainGame:

    def textObject(self, text, font, text_color):
        myText = font.render(text, True, text_color)
        return myText, myText.get_rect()

    def message_to_screen(self, msg, color, font, y_displace = 0):
        global SCREEN, SCREENHEIGHT,SCREENWIDTH

        TextSurface, TextRect = self.textObject(msg, font, color)
        # y_dispalce is used to get y displacement from centre
        TextRect.center = (SCREENWIDTH/2), (SCREENHEIGHT/2) + y_displace         
        SCREEN.blit(TextSurface, TextRect)

    def total_scores(self):
        
        global SCORE, HIGHEST
        
        paused = True
        
        totalScoreFont = pygame.font.SysFont('Arial', 25, 'b') 
        self.message_to_screen(f"Total Score: {SCORE}", (255, 40, 0), totalScoreFont, -100)
        self.message_to_screen("Press Enter and Goto the Main Screen", (0, 0, 0), FONT, 203)
        
        if(HIGHEST < SCORE):
            HIGHEST = SCORE
        SCORE = 0

        while paused:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    quit()

                if event.type == KEYDOWN:
                    paused = False

            pygame.display.update()		

    def pause(self):
        paused = True
        self.message_to_screen("Paused", (255, 40, 0), FONT, -100)
        self.message_to_screen("Press Escape to continue or q to quit", (0, 0, 0), FONT, -20)

        while paused:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    quit()

                if event.type == KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        quit()
                    elif event.key == K_ESCAPE:
                        paused = False

            pygame.display.update()		

    def button(self, bx, by, width, height, color, color2, text_color, text):
        mouse = pygame.mouse.get_pos()

        if bx + width > mouse[0] > bx and by + height > mouse[1] > by:
            pygame.draw.rect(SCREEN, color2, (bx,by,width,height))
        else:
            pygame.draw.rect(SCREEN, color, (bx,by,width,height))
        TextSurf, TextRect = self.textObject(text, FONT, text_color)
        TextRect.center = ((bx + (width/2)), (by + (height/2)))
        SCREEN.blit(TextSurf, TextRect)

    def welcomeScreen(self):
        """
        Shows welcome images on the screen
        """
        global SPEED, LEVEL, BACKGROUND

        LEVEL = 1
        BACKGROUND = 'gallery/sprites/level1.png'

        easyButton = {'x': 25, 'y': 350,'width': 60, 'height': 40, 'color': (86,215,0), 'color2': (57,255,20), 'text_color': (255,255,255), 'text': "Easy"}
        mediumButton = {'x': 115, 'y': 350,'width': 60, 'height': 40, 'color': (86,215,0), 'color2': (57,255,20), 'text_color': (255,255,255), 'text': "Medium"}
        hardButton = {'x': 205, 'y': 350,'width': 60, 'height': 40, 'color': (86,215,0), 'color2': (57,255,20), 'text_color': (255,255,255), 'text': "Hard"}
        startButton = {'x': 115, 'y': 445,'width': 60, 'height': 40, 'color': (86,215,0), 'color2': (57,255,20), 'text_color': (255,255,255), 'text': "Start"}

        playerx = int(SCREENWIDTH/5)
        playery = int((SCREENHEIGHT - GAME_SPRITES['player'].get_height())/2)
        messagex = int((SCREENWIDTH - GAME_SPRITES['message'].get_width())/2)
        messagey = int(SCREENHEIGHT*0.13)
        basex = 0

        
        while True:
            for event in pygame.event.get():
                # if user clicks on cross button, close the game
                if event.type == QUIT:
                    pygame.quit()
                    quit()

                elif event.type == MOUSEBUTTONDOWN:
                    if ((pygame.mouse.get_pos()[0] > easyButton['x'] and pygame.mouse.get_pos()[0] < easyButton['x'] + easyButton['width']) and
                    (pygame.mouse.get_pos()[1] > easyButton['y'] and pygame.mouse.get_pos()[1] < easyButton['y'] + easyButton['height'])):
                        SPEED = 30
                        GAME_SOUNDS['swoosh'].play()

                    elif ((pygame.mouse.get_pos()[0] > mediumButton['x'] and pygame.mouse.get_pos()[0] < mediumButton['x'] + mediumButton['width']) and
                    (pygame.mouse.get_pos()[1] > mediumButton['y'] and pygame.mouse.get_pos()[1] < mediumButton['y'] + mediumButton['height'])):
                        SPEED = 40
                        GAME_SOUNDS['swoosh'].play()

                    elif ((pygame.mouse.get_pos()[0] > hardButton['x'] and pygame.mouse.get_pos()[0] < hardButton['x'] + hardButton['width']) and
                    (pygame.mouse.get_pos()[1] > hardButton['y'] and pygame.mouse.get_pos()[1] < hardButton['y'] + hardButton['height'])):
                        SPEED = 50
                        GAME_SOUNDS['swoosh'].play()

                    elif ((pygame.mouse.get_pos()[0] > startButton['x'] and pygame.mouse.get_pos()[0] < startButton['x'] + startButton['width']) and
                        (pygame.mouse.get_pos()[1] > startButton['y'] and pygame.mouse.get_pos()[1] < startButton['y'] + startButton['height']) and SPEED != 0):
                            GAME_SOUNDS['swoosh'].play()
                            return

                    elif ((pygame.mouse.get_pos()[0] > startButton['x'] and pygame.mouse.get_pos()[0] < startButton['x'] + startButton['width']) and
                        (pygame.mouse.get_pos()[1] > startButton['y'] and pygame.mouse.get_pos()[1] < startButton['y'] + startButton['height'])):
                            GAME_SOUNDS['hit'].play()
                else:
                    SCREEN.blit(GAME_SPRITES['background'], (0, 0))    
                    SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))    
                    SCREEN.blit(GAME_SPRITES['message'], (messagex,messagey ))    
                    SCREEN.blit(GAME_SPRITES['base'], (basex, GROUNDY)) 
                    
                    self.button(easyButton['x'], easyButton['y'], easyButton['width'], easyButton['height'], easyButton['color'], easyButton['color2'], easyButton['text_color'], easyButton['text'])
                    self.button(mediumButton['x'], mediumButton['y'], mediumButton['width'], mediumButton['height'], mediumButton['color'], mediumButton['color2'], mediumButton['text_color'], mediumButton['text'])
                    self.button(hardButton['x'], hardButton['y'], hardButton['width'], hardButton['height'], hardButton['color'], hardButton['color2'], hardButton['text_color'], hardButton['text'])
                    self.button(startButton['x'], startButton['y'], startButton['width'], startButton['height'], startButton['color'], startButton['color2'], startButton['text_color'], startButton['text'])
                    pygame.display.flip() 
                    
                    # This is for showing the highest score lable on the welcome screen.
                    TextSurface, TextRect = self.textObject(f"Highest: {HIGHEST}", FONT, (0, 0, 0))
                    TextRect.center = (40), (20)
                    SCREEN.blit(TextSurface, TextRect)
                    pygame.display.update()
                    FPSCLOCK.tick(SPEED)

    def mainGame(self):
        
        global SCORE, LEVEL, BACKGROUND, SPEED
        cnt, cnt2, cnt3 = 0, 0, 0

        playerx = int(SCREENWIDTH/5)
        playery = int(SCREENWIDTH/2)
        basex = 0

        # Create 2 pipes for blitting on the screen
        newPipe1 = self.getRandomPipe()
        newPipe2 = self.getRandomPipe()

        # my List of upper pipes
        upperPipes = [
            {'x': SCREENWIDTH+200, 'y':newPipe1[0]['y']},
            {'x': SCREENWIDTH+200+(SCREENWIDTH/2), 'y':newPipe2[0]['y']},
        ]

        # my List of lower pipes
        lowerPipes = [
            {'x': SCREENWIDTH+200, 'y':newPipe1[1]['y']},
            {'x': SCREENWIDTH+200+(SCREENWIDTH/2), 'y':newPipe2[1]['y']},
        ]

        pipeVelX = -4

        playerVelY = -9
        playerMaxVelY = 10
        playerMinVelY = -8

        # Acceleration while flapping
        playerAccY = 1      
        # velocity while flapping
        playerFlapAccv = -8
        # It is true only when the bird is flapping
        playerFlapped = False 

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    quit()
                elif event.type == KEYDOWN and  (event.key == K_ESCAPE):
                    self.pause()
                elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                    # self.pause()
                    if playery > 0:
                        playerVelY = playerFlapAccv
                        playerFlapped = True
                        GAME_SOUNDS['wing'].play()

            # This function will return true if the player is crashed.
            crashTest = self.isCollide(playerx, playery, upperPipes, lowerPipes)
            if crashTest:
                return     

            #check for score
            playerMidPos = playerx + GAME_SPRITES['player'].get_width()/2
            for pipe in upperPipes:
                pipeMidPos = pipe['x'] + GAME_SPRITES['pipe'][0].get_width()/2
                if pipeMidPos<= playerMidPos < pipeMidPos + 4:
                    SCORE +=1
                    # print(f"Your score is {SCORE}") 
                    GAME_SOUNDS['point'].play()

            if playerVelY <playerMaxVelY and not playerFlapped:
                playerVelY += playerAccY

            if playerFlapped:
                playerFlapped = False            
            playerHeight = GAME_SPRITES['player'].get_height()
            playery = playery + min(playerVelY, GROUNDY - playery - playerHeight)

            # move pipes to the left
            for upperPipe , lowerPipe in zip(upperPipes, lowerPipes):
                upperPipe['x'] += pipeVelX
                lowerPipe['x'] += pipeVelX

            # Add a new pipe when the first is about to cross the leftmost part of the screen
            if 0 < upperPipes[0]['x'] < 5:
                newpipe = self.getRandomPipe()
                upperPipes.append(newpipe[0])
                lowerPipes.append(newpipe[1])

            # if the pipe is out of the screen, remove it
            if upperPipes[0]['x'] < -GAME_SPRITES['pipe'][0].get_width():
                upperPipes.pop(0)
                lowerPipes.pop(0)
            
            # Lets blit our sprites now
            SCREEN.blit(GAME_SPRITES['background'], (0, 0))
            for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
                SCREEN.blit(GAME_SPRITES['pipe'][0], (upperPipe['x'], upperPipe['y']))
                SCREEN.blit(GAME_SPRITES['pipe'][1], (lowerPipe['x'], lowerPipe['y']))

            SCREEN.blit(GAME_SPRITES['base'], (basex, GROUNDY))
            SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))
            myDigits = [int(x) for x in list(str(SCORE))]
            width = 0
            for digit in myDigits:
                width += GAME_SPRITES['numbers'][digit].get_width()
            Xoffset = (SCREENWIDTH - width) / 2

            for digit in myDigits:
                SCREEN.blit(GAME_SPRITES['numbers'][digit], (Xoffset, SCREENHEIGHT * 0.12))
                Xoffset += GAME_SPRITES['numbers'][digit].get_width()
            
            if(SCORE >= 10 and SCORE < 20):
                cnt += 1
                LEVEL = 2
                if(cnt == 1):
                    GAME_SOUNDS['levelup'].play()
                    SPEED += 5 
                else:
                    0
                BACKGROUND = 'gallery/sprites/level2.png'
            elif(SCORE >= 20 and SCORE < 30):
                cnt2 += 1
                LEVEL = 3
                if(cnt2 == 1):
                    GAME_SOUNDS['levelup'].play()
                    SPEED += 5 
                else:
                    0
                BACKGROUND = 'gallery/sprites/level3.png'
            elif(SCORE >= 30 and SCORE < 40):
                cnt3 += 1
                LEVEL = 4
                if(cnt3 == 1):
                    GAME_SOUNDS['levelup'].play()
                    SPEED += 5 
                else:
                    0
                BACKGROUND = 'gallery/sprites/level4.png'

            GAME_SPRITES['background'] = pygame.image.load(BACKGROUND).convert()

            TextSurface, TextRect = self.textObject(f"Level: {LEVEL}", FONT, (0, 0, 0))
            TextRect.center = (SCREENWIDTH / 2), (20)
            SCREEN.blit(TextSurface, TextRect)

            TextSurface, TextRect = self.textObject(f"Highest: {HIGHEST}", FONT, (0, 0, 0))
            TextRect.center = (40), (20)
            SCREEN.blit(TextSurface, TextRect)

            pygame.display.update()
            FPSCLOCK.tick(SPEED)

    def isCollide(self, playerx, playery, upperPipes, lowerPipes):
        
        global SPEED

        if playery > GROUNDY - 25  or playery<0:
            GAME_SOUNDS['hit'].play()
            SPEED = 0
            self.total_scores()
            return True
        
        for pipe in upperPipes:
            pipeHeight = GAME_SPRITES['pipe'][0].get_height()
            
            if((playery < pipeHeight + pipe['y']) and (abs(playerx - pipe['x']) < GAME_SPRITES['pipe'][0].get_width() - 19)):
                GAME_SOUNDS['hit'].play()
                SPEED = 0
                self.total_scores()
                return True

        for pipe in lowerPipes:
            if ((playery + GAME_SPRITES['player'].get_height() > pipe['y']) and (abs(playerx - pipe['x']) < GAME_SPRITES['pipe'][0].get_width() - 19)):
                GAME_SOUNDS['hit'].play()
                SPEED = 0
                self.total_scores()
                return True

        return False

    def getRandomPipe(self):
        """
        Generate positions of two pipes(one bottom straight and one top rotated ) for blitting on the screen
        """
        pipeHeight = GAME_SPRITES['pipe'][0].get_height()
        offset = SCREENHEIGHT/3
        y2 = offset + random.randrange(0, int(SCREENHEIGHT - GAME_SPRITES['base'].get_height()  - 1.2 *offset))
        pipeX = SCREENWIDTH + 10
        y1 = pipeHeight - y2 + offset
        pipe = [
            # Upper Pipe
            {'x': pipeX, 'y': -y1},
            # Lower Pipe
            {'x': pipeX, 'y': y2} 
        ]
        return pipe

if __name__ == "__main__":

    # This will be the main point from where our game will start
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption('Flappy Bird by Major-Xeon')
    GAME_SPRITES['numbers'] = ( 
        pygame.image.load('gallery/sprites/0.png').convert_alpha(),
        pygame.image.load('gallery/sprites/1.png').convert_alpha(),
        pygame.image.load('gallery/sprites/2.png').convert_alpha(),
        pygame.image.load('gallery/sprites/3.png').convert_alpha(),
        pygame.image.load('gallery/sprites/4.png').convert_alpha(),
        pygame.image.load('gallery/sprites/5.png').convert_alpha(),
        pygame.image.load('gallery/sprites/6.png').convert_alpha(),
        pygame.image.load('gallery/sprites/7.png').convert_alpha(),
        pygame.image.load('gallery/sprites/8.png').convert_alpha(),
        pygame.image.load('gallery/sprites/9.png').convert_alpha(),
    )

    GAME_SPRITES['message'] =pygame.image.load('gallery/sprites/message.png').convert_alpha()
    GAME_SPRITES['base'] =pygame.image.load('gallery/sprites/base.png').convert_alpha()
    GAME_SPRITES['pipe'] =(pygame.transform.rotate(pygame.image.load( PIPE).convert_alpha(), 180), 
    pygame.image.load(PIPE).convert_alpha()
    )

    # Game sounds
    GAME_SOUNDS['die'] = pygame.mixer.Sound('gallery/audio/die.wav')
    GAME_SOUNDS['hit'] = pygame.mixer.Sound('gallery/audio/hit.wav')
    GAME_SOUNDS['point'] = pygame.mixer.Sound('gallery/audio/point.wav')
    GAME_SOUNDS['swoosh'] = pygame.mixer.Sound('gallery/audio/swoosh.wav')
    GAME_SOUNDS['wing'] = pygame.mixer.Sound('gallery/audio/wing.wav')
    GAME_SOUNDS['levelup'] = pygame.mixer.Sound('gallery/audio/levelup.wav')
    
    GAME_SPRITES['background'] = pygame.image.load(BACKGROUND).convert()
    GAME_SPRITES['player'] = pygame.image.load(PLAYER).convert_alpha()

    # Creating object of MainGame class
    mainGameObject = MainGame()
    while True:
        # Shows welcome screen to the user until he presses a button
        mainGameObject.welcomeScreen() 
        # This is the main game function 
        mainGameObject.mainGame() 