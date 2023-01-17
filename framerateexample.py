import shadowgame
shadowgame.SetWindow(700, 500, "Hello World!")
shadowgame.SetFPS(6000000000) # Don't actually do this
while True:
    if shadowgame.Game() == False:
        break
    else:
        pass # The juicy non-base-template code goes here