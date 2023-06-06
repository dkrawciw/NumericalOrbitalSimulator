from RenderPoints import RenderPoints
from Planet import Planet
import numpy as np

def main():
    p1 = Planet(10000,[np.array([750,5,750,0])])
    p2 = Planet(1,[np.array([750,10,700,0])])

    planetList = [p1, p2]

    Planet.eulerSim(planetList,[0,100],0.001)

    RenderPoints.renderScreen( planetList, numOfSteps=20 )

    RenderPoints.renderScreenNoInterpolation( planetList )

if __name__ == '__main__':
    main()