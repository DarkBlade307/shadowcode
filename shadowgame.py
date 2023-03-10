import pygame
# COLORS - Defines basic colours that can be used out of the box
WHITE = (255, 255, 255)
BLACK = (000, 000, 000)
RED   = (255, 000, 000)
GREEN = (000, 255, 000)
BLUE  = (000, 000, 255)

# Set Window
def SetWindow(width, height, text):
    size = (width, height)
    global screen
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(str(text))

SetWindow(700, 500, "HelloWorld!!")

fps = 60 # Default FPS in case FPS doesn't get set
clock = pygame.time.Clock() #Create the clock

# Set FPS function
def SetFPS(FPS):
    global fps
    fps = FPS

Painter = [] # List of objects to be painted by the Paint() function
PreFillPainter = [] # List of objects that get painted  BEFORE the screen gets filled (useful for hitboxes)
ColorFill = BLACK # The default colour that fills the screen at the beginning of the Paint() function
ScreenFillMode = "Solid"

def SetFillColor(color):
    global ColorFill
    ColorFill = color
    global ScreenFillMode
    ScreenFillMode  = "Solid"

def SetBgImg(IMG):
    global BGimg
    BGimg = pygame.image.load(IMG)
    global ScreenFillMode
    ScreenFillMode = "Image"

# Draws objects on the screen
def Paint():
    for i in PreFillPainter:
        i.Paint()
    if ScreenFillMode == "Solid":
        screen.fill(ColorFill)
    elif ScreenFillMode == "Image":
        screen.blit(BGimg, (0, 0))
    for i in Painter:
        i.Paint()
    pygame.display.flip()
    Painter.clear()

def GetKeys(checking):
    pressed = pygame.key.get_pressed()
    for i in checking:
        if pressed[i]:
            return True

def MouseCollisionCheck(COLLIDER):
    mousePos = pygame.mouse.get_pos()
    if COLLIDER.collidepoint(mousePos[0], mousePos[1]):
        return True
    else:
        return False
#Classes

class Shape: # Basic shape class for the basic shapes that pygame can draw out of the box
    def __init__(self, type, posX, posY, width, height, colour, name):
        self.PosX = posX # The X position of the shape on the screen
        self.PosY = posY # The Y position of the shape on the screen
        self.Color = colour # The colour of the shape
        self.Width = width # The width of the shape
        self.Height = height # The height of the shape
        self.Type = type # The type of shape (rect, elipse, etc)
        self.Name = name # The name of the object
    def Paint(self): # Built in function to paint the object
        if self.Type == "rect":
            pygame.draw.rect(screen, self.Color, (self.PosX, self.PosY, self.Width, self.Height))
        elif self.Type == "ellipse":
            pygame.draw.ellipse(screen, self.Color, (self.PosX, self.PosY, self.Width, self.Height))

class Hitbox: # Basic hitbox that allows you to get collision info
    def __init__(self, posX, posY, width, height, colour, name):
        self.PosX = posX # The X position of the shape on the screen
        self.PosY = posY # The Y position of the shape on the screen
        self.Color = colour # The colour of the shape
        self.Width = width # The width of the shape
        self.Height = height # The height of the shape
        self.Type = type # The type of shape (rect, elipse, etc)
        self.Name = name # The name of the object
        self.whole = pygame.draw.rect(screen, self.Color, (self.PosX, self.PosY, self.Width, self.Height), 1)
        self.left = pygame.draw.rect(screen, self.Color, (self.PosX, self.PosY, self.Width - (self.Width - 1), self.Height))
        self.right = pygame.draw.rect(screen, self.Color, (self.PosX + (self.Width - 1), self.PosY, self.Width - (self.Width - 1), self.Height))
        self.up = pygame.draw.rect(screen, self.Color, (self.PosX, self.PosY, self.Width, self.Height - (self.Height - 1)))
        self.down = pygame.draw.rect(screen, self.Color, (self.PosX, self.PosY + (self.Height - 1), self.Width - (self.Width - 1), self.Height - (self.Height - 1)))
    def Paint(self): # Built in function to paint the object
        global whole, left, right, up, down
        self.whole = pygame.draw.rect(screen, self.Color, (self.PosX, self.PosY, self.Width, self.Height), 1)
        self.left = pygame.draw.rect(screen, self.Color, (self.PosX, self.PosY, self.Width - (self.Width - 1), self.Height))
        self.right = pygame.draw.rect(screen, self.Color, (self.PosX + (self.Width - 1), self.PosY, self.Width - (self.Width - 1), self.Height))
        self.up = pygame.draw.rect(screen, self.Color, (self.PosX, self.PosY, self.Width, self.Height - (self.Height - 1)))
        self.down = pygame.draw.rect(screen, self.Color, (self.PosX, self.PosY + (self.Height - 1), self.Width - (self.Width - 1), self.Height - (self.Height - 1)))

class Sprite: # Sprite class that supports animations
    def __init__(self, img, position):
        self.Images = []
        self.ImageNo = 0
        self.PosX = position[0]
        self.PosY = position[1]
        for i in img:
            self.Images.append(pygame.image.load(i))
    def Paint(self):
        screen.blit(self.Images[self.ImageNo], (self.PosX, self.PosY))

def Game():
    global clock
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    Paint()
    clock.tick(fps)