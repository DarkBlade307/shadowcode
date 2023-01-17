import shadowgame
shadowgame.SetWindow(700, 500, "Set Fill Color Example!")
shadowgame.SetFillColor(shadowgame.GREEN)
while True:
    if shadowgame.Game() == False:
        break
    else:
        pass # The juicy non-base-template code goes here