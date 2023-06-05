import numpy as np

class Planet:
    def __init__(self, mass = 1, indepVariables = [np.array([0,0,0,0])]):
        self._mass = mass
        self._indepVariables = indepVariables

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
        directionIndependantVal = mass / ((w[2]**2 + w[0]**2 ) ** (3 / 2))
        xAccel = w[0] * directionIndependantVal
        yAccel = w[2] * directionIndependantVal

        return np.array( [w[1], xAccel, w[3], yAccel] )

    @staticmethod
    def eulerSim( PlanetList, r, h ):
        numOfSteps = (r[1] - r[0]) / h
        timeRange = np.linspace(0,10,50)

        for point in timeRange:
            for planet in PlanetList:
                currPos = planet.getPositions()[-1]
                nextStep = currPos

                for otherPlanet in PlanetList:
                    posDif = otherPlanet.getPositions()[-1] - currPos
                    # Check that the current planet isn't compared to itself
                    if planet == otherPlanet:
                        continue
                    
                    nextStep = nextStep + Planet.accelFunc(otherPlanet.getMass(),posDif)
                    
                
                planet.addPosition(nextStep)
