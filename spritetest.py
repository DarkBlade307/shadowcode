import shadowgame
import customs
shadowgame.SetWindow(700, 500, "Hello World!")
Player = shadowgame.Sprite(['1.png', '2.png', '3.png'], (70, 70))
PlayerBox = shadowgame.Hitbox(Player.PosX, Player.PosY, 16, 16, shadowgame.RED, "PlayerHitbox")
while True:
    if shadowgame.Game() == False:
        break
    else:
        shadowgame.Painter.append(Player)
        shadowgame.Painter.append(PlayerBox)
        if shadowgame.MouseCollisionCheck(PlayerBox.whole) == True:
            if shadowgame.pygame.mouse.get_pressed()[0] == True:
                Player.ImageNo = 2
            else:
                Player.ImageNo = 1
        else:
            Player.ImageNo = 0