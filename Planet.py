class Planet:
    def __init__(self, mass = 1, positions = [[0,0]]):
        self._mass = mass
        self._positions = positions

    def getPositions(self):
        return self._positions
    def setPositions(self, pos):
        self._positions = pos
    def addPositions(self, newPos):
        self._positions.append(newPos)

    def getMass(self):
        return self._mass
    def setMass(self, newMass):
        self._mass = newMass