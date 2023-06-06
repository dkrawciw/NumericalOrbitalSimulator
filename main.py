from RenderPoints import RenderPoints
from Planet import Planet
import numpy as np

def main():
    p1 = Planet(100000,[np.array([750,0,750,0])])
    p2 = Planet(1,[np.array([750,20,700,0])])
    p3 = Planet(1,[np.array([750,10,600,0])])

    planetList = [p1, p2, p3]

    Planet.rk4Sim(planetList,[0,200],0.001)

    RenderPoints.renderScreen( planetList, numOfSteps=10000 )

if __name__ == '__main__':
    main()