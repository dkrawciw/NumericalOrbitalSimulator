from RenderPoints import RenderPoints
from Planet import Planet
import numpy as np

def main():
    p1 = Planet(800,[np.array([500,-0.5,500,0])])
    p2 = Planet(1,[np.array([250,0,250,0])])
    p3 = Planet(1,[np.array([750,0,900,0])])
    p4 = Planet(800,[np.array([900,0.5,900,0])])

    planetList = [p1,p4]

    Planet.eulerSim(planetList,[0,1000],0.25)

    RenderPoints.renderScreen( planetList, 20 )

if __name__ == '__main__':
    main()