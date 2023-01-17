import shadowgame
# I mostly use the customs file to test things I want to add to the main SHADOWGAME file

class Hitbox: # Basic shape class for the basic shapes that pygame can draw out of the box
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
            self.whole = shadowgame.pygame.draw.rect(shadowgame.screen, self.Color, (self.PosX, self.PosY, self.Width, self.Height))
            self.left = shadowgame.pygame.draw.rect(shadowgame.screen, self.Color, (self.PosX, self.PosY, self.Width - (self.Width - 1), self.Height))
            self.right = shadowgame.pygame.draw.rect(shadowgame.screen, self.Color, (self.PosX + (self.Width - 1), self.PosY, self.Width - (self.Width - 1), self.Height))
            self.up = shadowgame.pygame.draw.rect(shadowgame.screen, self.Color, (self.PosX, self.PosY, self.Width, self.Height - (self.Height - 1)))
            self.left = shadowgame.pygame.draw.rect(shadowgame.screen, self.Color, (self.PosX, self.PosY + (self.Height - 1), self.Width - (self.Width - 1), self.Height - (self.Height - 1)))
        elif self.Type == "ellipse":
            shadowgame.pygame.draw.ellipse(shadowgame.screen, self.Color, (self.PosX, self.PosY, self.Width, self.Height))