import pygame

# window
win = pygame.display.set_mode((600, 700))
pygame.display.set_caption("Pixels")

# var
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
gray = (200, 200, 200)
blue = (0, 0, 255)
light_blue = (0, 255, 255)
green = (0, 255, 0)
yellow = (255, 255, 0)
brown = (117, 76, 41)
bg = pygame.image.load("bg.png")
pixels= []
pixel_width = 20
color = black

#class
class pixel(object):
    def __init__(self, x, y, width, color):
        self.x = x
        self.y = y
        self.width = width
        self.color = color
    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.width)    


#screen 
def redrawscreen():
    pygame.draw.rect(win, white, (0, 0, 600, 600))
    for s in pixels:
        s.draw(win)
    win.blit(bg, (0, 600))
    pygame.draw.circle(win, gray, (mx, my), pixel_width, 1)

#main loop
run = True
while run:
    mx, my = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                pixel_width += 1
            if pixel_width>1:
                if event.button == 5:
                    pixel_width -= 1        
            
    click = pygame.mouse.get_pressed()
    if click[0] == 1:
        pixels.append(pixel(mx, my, pixel_width, color))    
    if click[2] == 1:
        pixels.append(pixel(mx, my, pixel_width, white))  
    keys = pygame.key.get_pressed()
    if keys[pygame.K_1]:
        color =black
    elif keys[pygame.K_2]:
        color =gray
    elif keys[pygame.K_3]:
        color =red
    elif keys[pygame.K_4]:
        color =blue  
    elif keys[pygame.K_5]:
        color =green
    elif keys[pygame.K_6]:
        color =yellow
    elif keys[pygame.K_7]:
        color = brown
    elif keys[pygame.K_8]:
        color = light_blue 
    elif keys[pygame.K_ESCAPE]:
        run = False
    elif keys[pygame.K_LCTRL]:
        if keys[pygame.K_z]:
            del pixels[-1:]
    redrawscreen()
    pygame.display.update()