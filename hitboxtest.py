import shadowgame
import customs
shadowgame.SetWindow(700, 500, "Hitbox test!")
shadowgame.SetFillColor(shadowgame.BLACK)
Player = shadowgame.Shape("rect", 70, 70, 50, 50, shadowgame.BLUE, "Player")
PlayerBox = shadowgame.Hitbox(Player.PosX, Player.PosY, Player.Width, Player.Height, shadowgame.RED, "PlayerHitbox")
while True:
    if shadowgame.Game() == False:
        break
    else:
        shadowgame.Painter.append(Player)
        shadowgame.Painter.append(PlayerBox)
        if shadowgame.MouseCollisionCheck(PlayerBox.whole) == True:
            if shadowgame.pygame.mouse.get_pressed()[0] == True:
                Player.Color = shadowgame.RED
            else:
                Player.Color = shadowgame.GREEN
        else:
            Player.Color = shadowgame.BLUE