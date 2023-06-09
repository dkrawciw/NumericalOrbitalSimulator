from random import randrange
import pygame as pg
from math import ceil
from scipy.interpolate import CubicSpline
import numpy as np

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
            planetToRadius[planet] = 1 + ceil(maxRadius * planetToMass[planet] / largestMass)

        return planetToRadius

    @staticmethod
    def renderScreen(planetList, planetScale = 10, numOfSteps = 1000):
        planetToRadius = RenderPoints._setRadiusSizes(planetList, planetScale)

        # Create the interpolation functions for each trajectory
        stepList = range(0,numOfSteps)
        newPointList = {}
        planetToColor = {}

        for planet in planetList:
            # Make a random color for the planet
            planetToColor[planet] = Color( randrange(150,256),randrange(150,256),randrange(150,256) )

            P = np.array( planet.getPositions() )
            planetTime = np.linspace(planet.timeList[0],planet.timeList[-1], numOfSteps)
            
            equations = [CubicSpline(planet.timeList, P[:,0]), CubicSpline(planet.timeList, P[:,2])]

            newPointList[planet] = [ equations[0](planetTime), equations[1](planetTime) ]


        pg.init()
        screen = pg.display.set_mode( (1500, 1500) )

        for step in stepList:
            screen.fill(Color(0, 0, 0))

            for planet in planetList:
                centerPos = ( newPointList[planet][0][step], newPointList[planet][1][step] )
                pg.draw.circle(screen, planetToColor[planet], centerPos, planetToRadius[planet])
                    
            pg.display.update()

            for event in pg.event.get():
                if event.type == QUIT:
                    pg.quit()
                    sys.exit()
                    
        pg.quit()

        

    @staticmethod
    def renderScreenNoInterpolation(planetList, planetScale = 10):
        planetToRadius = RenderPoints._setRadiusSizes(planetList, planetScale)

        pg.init()
        screen = pg.display.set_mode( (1500, 1500) )

        for pointInTime in range(0,len(planetList[0].getPositions())):
            screen.fill(Color(0, 0, 0))

            for planet in planetList:
                planetInfo = planet.getPositions()[pointInTime]
                pg.draw.circle(screen, Color(0,255,0),(planetInfo[0],planetInfo[2]),planetToRadius[planet])
                
            pg.display.update()

            for event in pg.event.get():
                    if event.type == QUIT:
                        pg.quit()
                        sys.exit()

        pg.quit()