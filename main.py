from RenderPoints import RenderPoints
from Planet import Planet
import numpy as np

def main():
    p1 = Planet(2,[np.array([500,-1,500,-1])])
    p2 = Planet(1,[np.array([250,1,250,-1])])

    Planet.eulerSim([p1,p2],[0,10],0.25)

    print(f"First Planet: {p1.getPositions()}")
    print(f"Second Planet: {p2.getPositions()}")

    # RenderPoints.renderScreen([p1, p2])

if __name__ == '__main__':
    main()