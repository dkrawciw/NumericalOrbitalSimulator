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
            planetToRadius[planet] = ceil(maxRadius * planetToMass[planet] / largestMass)

        return planetToRadius

    @staticmethod
    def renderScreen(planetList, planetScale = 10, numOfSteps = 1000):
        planetToRadius = RenderPoints._setRadiusSizes(planetList, planetScale)

        # Create the interpolation functions for each trajectory
        planetToSpline = {}
        for planet in planetList:
            P = np.array( planet.getPositions() )
            
            planetToSpline[planet] = [CubicSpline(planet.timeList, P[:,0]), CubicSpline(planet.timeList, P[:,2])]

        pg.init()
        screen = pg.display.set_mode( (1500, 1500) )

        stepList = range(0,numOfSteps)
        newPointList = {}

        for planet in planetList:
            planetTime = np.linspace(planet.timeList[0],planet.timeList[-1], numOfSteps)
            newPointList[planet] = [ planetToSpline[planet][0](planetTime), planetToSpline[planet][1](planetTime) ]

        for step in stepList:
            screen.fill(Color(0, 0, 0))

            for planet in planetList:
                centerPos = ( newPointList[planet][0][step], newPointList[planet][1][step] )
                pg.draw.circle(screen, Color(0,255,0), centerPos, planetToRadius[planet])
                    
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