import pygame
import os
# window
WIN = pygame.display.set_mode((600, 700))
pygame.display.set_caption("Pixels")

# var
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GRAY = (200, 200, 200)
BLUE = (0, 0, 255)
LIGHT_BLUE = (0, 255, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BROWN = (117, 76, 41)
BG = pygame.image.load("BG.png")
PIXEL_WIDTH = 20

pixels= []
color = BLACK

#class
class pixel(object):
    def __init__(self, x, y, width, color):
        self.x = x
        self.y = y
        self.width = width
        self.color = color
    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.width)    
    
    def __str__(self):
        return f"{self.x}/{self.y}/{self.width}/{self.color}"


#screen 
def redrawscreen():
    pygame.draw.rect(WIN, WHITE, (0, 0, 600, 600))
    for s in pixels:
        s.draw(WIN)
    WIN.blit(BG, (0, 600))
    pygame.draw.circle(WIN, GRAY, (mx, my), PIXEL_WIDTH, 1)

def saveFile(fileName, li):
    try:
        file = open(fileName, 'x')
    except:
        file = open(fileName, 'w')
    for p in li:
        file.write(str(p)+"\n")
    file.close()

def openFile(fileName, li):
    try:
        file = open(fileName, 'r')
        lines = file.readlines()
        for l in lines:
            l = l.split('/')
            x = float(l[0])
            y = float(l[1])
            width = float(l[2])
            color = l[3].strip("()\n").split(",")
            color = (int(color[0].strip()), int(color[1].strip()), int(color[2].strip()))
            p = pixel(x, y, width, color)
            li.append(p)
    except:
        print("file not found")

#main loop
run = True
while run:
    mx, my = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                PIXEL_WIDTH += 1
            if PIXEL_WIDTH>1:
                if event.button == 5:
                    PIXEL_WIDTH -= 1        
            
    click = pygame.mouse.get_pressed()
    if click[0] == 1:
        pixels.append(pixel(mx, my, PIXEL_WIDTH, color))    
    if click[2] == 1:
        pixels.append(pixel(mx, my, PIXEL_WIDTH, WHITE))  
    keys = pygame.key.get_pressed()
    if keys[pygame.K_1]:
        color =BLACK
    elif keys[pygame.K_2]:
        color =GRAY
    elif keys[pygame.K_3]:
        color =RED
    elif keys[pygame.K_4]:
        color =BLUE  
    elif keys[pygame.K_5]:
        color =GREEN
    elif keys[pygame.K_6]:
        color =YELLOW
    elif keys[pygame.K_7]:
        color = BROWN
    elif keys[pygame.K_8]:
        color = LIGHT_BLUE 
    elif keys[pygame.K_ESCAPE]:
        run = False
    elif keys[pygame.K_LCTRL]:
        if keys[pygame.K_z]:
            try:
                pixels.pop()
            except:
                pass
        if keys[pygame.K_s]:
            name = input('write the file name: ')
            saveFile(name, pixels)
    
        if keys[pygame.K_f]:
            name = input('write the name of the file you want to open: ')
            pixels = []
            openFile(name, pixels)
    redrawscreen()
    pygame.display.update()
