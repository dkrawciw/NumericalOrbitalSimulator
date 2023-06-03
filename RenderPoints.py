import numpy as np
import pygame as pg
from Planet import Planet

import sys
from pygame import Color
from pygame.locals import *

class RenderPoints:

    @staticmethod
    def renderScreen(posInfo):
        pg.init()
        screen = pg.display.set_mode((1500, 1500))
        screen.fill(Color(0, 0, 0))


        for i in range(0,len(posInfo[0])):

            for event in pg.event.get():
                    if event.type == QUIT:
                        pg.quit()
                        sys.exit()
                
            for j in range(0, len(posInfo),2):
                pg.draw.circle(screen, Color(0,255,0), (posInfo[i][j],posInfo[i+1][j]), radius=1)
                pg.display.update()
                screen.fill(Color(0, 0, 0))

        # for i in range(0,len(posInfo),2):
        #     screen.fill(Color(0, 0, 0))
        #     for j in range(0,len(posInfo[i])):
        #         pg.draw.circle(screen, Color(0,255,0), (posInfo[i][j],posInfo[i+1][j]), radius=1)

        #     pg.display.update()


        pg.quit()