import time
import numpy as np
import pygame as pg
from Planet import Planet
from math import ceil

import sys
from pygame import Color
from pygame.locals import *

class RenderPoints:
    @staticmethod
    def _setRadiusSizes(planetList, maxRadius):
        planetToMass = {}
        for planet in planetList:
            planetToMass[planet] = planet.getMass()
        
        largestMass = max(planetToMass.values())

        planetToRadius = {}
        for planet in planetToMass:
            planetToRadius[planet] = ceil(maxRadius * planetToMass[planet] / largestMass)

        return planetToRadius

    @staticmethod
    def renderScreen(planetList, planetScale = 10):
        planetToRadius = RenderPoints._setRadiusSizes(planetList, planetScale)

        pg.init()
        screen = pg.display.set_mode( (1500, 1500) )


        for pointInTime in range(0,len(planetList[0].getPositions())):
            screen.fill(Color(0, 0, 0))

            for planet in planetList:
                planetInfo = planet.getPositions()[pointInTime]
                pg.draw.circle(screen, Color(0,255,0),(planetInfo[0],planetInfo[2]),planetToRadius[planet])
                
            pg.display.update()
            # time.sleep(0.2)

            for event in pg.event.get():
                    if event.type == QUIT:
                        pg.quit()
                        sys.exit()

        pg.quit()