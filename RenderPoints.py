import time
import numpy as np
import pygame as pg
from Planet import Planet

import sys
from pygame import Color
from pygame.locals import *

class RenderPoints:
    @staticmethod
    def renderScreen(planetList):
        pg.init()
        screen = pg.display.set_mode( (1500, 1500) )


        for pointInTime in range(0,len(planetList[0].getPositions())):
            screen.fill(Color(0, 0, 0))

            for planet in planetList:
                planetInfo = planet.getPositions()[pointInTime]
                pg.draw.circle(screen, Color(0,255,0),(planetInfo[0],planetInfo[2]),5,5)
                
            pg.display.update()
            # time.sleep(0.2)

            for event in pg.event.get():
                    if event.type == QUIT:
                        pg.quit()
                        sys.exit()

        pg.quit()