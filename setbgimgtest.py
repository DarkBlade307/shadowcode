import shadowgame
import customs
shadowgame.SetWindow(700, 500, "Background Image Test!!")
shadowgame.SetFPS(60)
shadowgame.SetBgImg("bgtest.jpeg")
while True:
    if shadowgame.Game() == False:
        break