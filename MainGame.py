from pygame import *
from time import *
from sys import *

#MAIN GAME LOOP
while True:
    init()
    
    for events in event.get():
        if events.type == QUIT:
            quit()
            exit()
    
    #INITIALISE THE WINDOW.
    SCREENWIDTH = 900
    SCREENHEIGHT = 600
    SCREENSIZE = [SCREENWIDTH, SCREENHEIGHT]
    SCREEN = display.set_mode(SCREENSIZE)
    bg_col = [255, 123, 67]
    gameplay_screen_col
    SCREEN.fill(bg_col)
    display.update()
    draw.rect(SCREEN, , Rect, width=0)
    
    
    
    #INITIALISE ALL OBJECTS.
    class Protag:
        def __init__(self, name, title, sprite, portrait, power):
            self.name = name
            self.title = title
            self.sprite = sprite
            self.portrait = portrait
            self.power = power

    class Player:
        def __init__(self, character, hp, lifelines, score, hit, almost, miss):
            self.character = character
            self.hp = hp
            self.lifelines = lifelines
            self.score = score
            self.hit = hit
            self.almost = almost
            self.miss = miss

    class Opponent:
        def __init__(self, name, title, sprite, portrait, stage, hp):
            self.name = name
            self.title = title
            self.sprite = sprite
            self.portrait = portrait
            self.stage = stage #stage is a function from which the full stage plays out
            self.hp = hp

    class Bullet:
        def __init__(self, sprite, direction, speed):
            self.sprite = sprite
            self.direction = direction
            self.speed = speed

    class Arrow:
        def __init__(self, sprite, direction):
            self.sprite = sprite
            self.direction = direction #direction is a number which corresponds to which sprite (up1, down2, left3, right4)
            
    

    #MUSIC IN BACKGROUND.
    #I need to make the following tracks:
    #NOTE: there is a cutscene before and after each stage
            #Title screen theme
            #Cutscene theme
            #Pre-Battle theme - plays while opponent is introduced.
            #Stage 1 Boss theme - Fairy of Many Worlds ~ Minty Portal
            #Stage 2 Boss theme - Here to teach you a lesson ~ Ms Teacha - At this stage, use school sprites
            #Stage 3 Boss theme - Lost for 500 Years ~ Marion's Ghost - At this stage, use school sprites
            #Stage 4 Boss theme - The Good Side of Evil ~ Insanity Good-demon
            #Stage 5 Boss theme - The Mastermind ~ Lightning Storm
            #Stage 6 Boss theme - The Hero's Dark Side ~ Eleeza-Storm - in this stage, player is switched to Lila
            #Extra Stage Boss theme - Sister and Brother ~ Zee and Sam - in this stage, player switched to Lee
            #Game Over theme
            #End Screen Theme

    #Also Sound FX:
            #Hit by bullet
            #Hit arrow
            #Almost arrow
            #Miss arrow

    #BULLETS:
    #MOVE THE CLONED BULLETS IN ONE CONSTANT DIRECTION
    #MOVE THEM FROM DIFFERENT PLACES
    #IF HIT
    #TAKE AWAY PLAYER HP

    #RHYTHM
    #MOVE ARROWS TO GHOST ARROW
    #IF KEY PRESSED WHEN IT REACHES THE GHOST ARROW
    #ADD TO SCORE
    #TAKE AWAY OPPONENT HP

    #GAME START
    #CALL ALL FUNCTIONS IN ORDER

    #IF KEY PRESSED
    #MOVE SPRITE
