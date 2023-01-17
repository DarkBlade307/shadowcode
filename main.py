import shadowgame
shadowgame.SetWindow(700, 500, "Hello World!")
shadowgame.SetFillColor(shadowgame.WHITE)
Player = shadowgame.Shape('ellipse', 0, 0, 50, 50, shadowgame.BLACK, "Player")
while True:
    if shadowgame.Game() == False:
        break
    else:
        if shadowgame.GetKeys([shadowgame.pygame.K_d]) == True:
            Player.PosX += 5
        if shadowgame.GetKeys([shadowgame.pygame.K_a]) == True:
            Player.PosX -= 5
        shadowgame.Painter.append(Player)