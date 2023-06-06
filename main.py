from RenderPoints import RenderPoints
from Planet import Planet
import numpy as np

def main():
    p1 = Planet(100000,[np.array([750,10,750,10])])
    p2 = Planet(1,[np.array([750,20,700,0])])
    p3 = Planet(1,[np.array([750,-20,800,0])])

    planetList = [p1, p2, p3]

    Planet.eulerSim(planetList,[0,100],0.001)

    RenderPoints.renderScreen( planetList, numOfSteps=1000 )

if __name__ == '__main__':
    main()