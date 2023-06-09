import numpy as np
from math import ceil
from math import sqrt

class Planet:
    def __init__(self, mass = 1, indepVariables = [np.array([0,0,0,0])]):
        self._mass = mass
        self._indepVariables = indepVariables
        self.timeList = [0]

    def getPositions(self):
        return self._indepVariables
    def setPositions(self, pos):
        self._indepVariables = pos
    def addPosition(self, newPos):
        self._indepVariables.append(newPos)

    def getMass(self):
        return self._mass
    def setMass(self, newMass):
        self._mass = newMass

    def getTimeRange(self):
        return self.timeRange
    def setTimeRange(self, timeRange):
        self._timeRange = timeRange
    
    # Inputted vector should look like: [x1, x2, y1, y2]
    # Outputted vector should look like: [x1', x2', y1', y2']
    @staticmethod
    def accelFunc( mass:int, w:np.array  ):
        distance = sqrt(w[2]**2 + w[0]**2)
        if distance < 5:
            return np.array( [0,0,0,0] )

        directionIndependentVal = (-1) * mass / (distance ** 3)
        xAccel = w[0] * directionIndependentVal
        yAccel = w[2] * directionIndependentVal

        return np.array( [w[1], xAccel, w[3], yAccel] )

    @staticmethod
    def eulerSim( PlanetList, r, h ):
        numOfSteps = ceil((r[1] - r[0]) / h)
        timeRange = np.linspace(r[0],r[1],numOfSteps)

        for planet in PlanetList:
            planet.timeList = timeRange

        for point in timeRange[1:]:
            for planet in PlanetList:
                currPos = planet.getPositions()[-1]
                nextStep = currPos

                for otherPlanet in PlanetList:
                    posDif = currPos - otherPlanet.getPositions()[-1]
                    # Check that the current planet isn't compared to itself
                    if planet == otherPlanet:
                        continue
                    
                    nextStep = nextStep + h * Planet.accelFunc(otherPlanet.getMass(),posDif)
                    
                
                planet.addPosition(nextStep)

    @staticmethod
    def rk4Sim( PlanetList, r, h ):
        numOfSteps = ceil((r[1] - r[0]) / h)
        timeRange = np.linspace(r[0],r[1],numOfSteps)

        for planet in PlanetList:
            planet.timeList = timeRange

        for point in timeRange[1:]:
            for planet in PlanetList:
                currPos = planet.getPositions()[-1]
                nextStep = currPos

                for otherPlanet in PlanetList:
                    posDif = currPos - otherPlanet.getPositions()[-1]
                    # Check that the current planet isn't compared to itself
                    if planet == otherPlanet:
                        continue
                    
                    k1 = h * Planet.accelFunc(otherPlanet.getMass(),posDif)
                    k2 = h * Planet.accelFunc(otherPlanet.getMass(),posDif + k1/2)
                    k3 = h * Planet.accelFunc(otherPlanet.getMass(),posDif + k2/2)
                    k4 = h * Planet.accelFunc(otherPlanet.getMass(),posDif + k3)

                    nextStep = nextStep + (k1 + 2 * k2 + 2 * k3 + k4) / 6
                    
                
                planet.addPosition(nextStep)
        