import shadowgame
# I mostly use the customs file to test things I want to add to the main SHADOWGAME file
class Sprite():
    def __init__(self, img, position):
        self.Images = []
        self.ImageNo = 0
        self.PosX = position[0]
        self.PosY = position[1]
        for i in img:
            self.Images.append(shadowgame.pygame.image.load(i))
    def Paint(self):
        shadowgame.screen.blit(self.Images[self.ImageNo], (self.PosX, self.PosY))