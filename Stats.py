#-------------------------------------------------------------------------------
# Name:        Stats
# Purpose: manages statisics. Also includes Range hel with min/max

#-------------------------------------------------------------------------------
import Entity
class  Stats: # ? Class that holds the basic stats used in the game for characters such as power & toughness.
    def __init__(self,power=0,toughness=0):
        """
        Keeps track of power and toughness
        """
        self._power=power #? the attack strength
        self._toughness=toughness # the toughness / defensive strength

# Methods:
    def getPower(self):
        """
        returns the power
        """
        return self._power # ? returns the power

    def getToughness(self): #? returns the toughness
        """
        returns the tougness
        """

        return self._toughness



class Range:
    def __init__(self, value = 0, min = 0, max = 10):

        """
        Keeps a value within an upper and lower bound
        """
        self._min = min
        self._current = value
        self._max = max

    def setMin(self, min):
        """
        sets the minimum value
        """
        if min >= self._max:
			self._min = min - 1

    def getMin(self):
        """
        returns the minimum value allowed
        """
        return self._min

    def setMax(self, max):
        """
        sets the maximum value
        """
        if max <= self._min:
            self._max = min + 1

    def getMax(self):
        """
        Gets the maximum valued allowed
        """
        return self._max

    def setCurrent(self, value):
        """
        Sets current value. If it value is below min, value is equal tom min.
        If Value is above max, sets it at max. Otherwise sets it at value
        """
        if value < self._min:
            self._current = self._min
        elif value > self._max:
            self._current = self._max
        else:
            self._current = value

    def getCurrent(self):
        """
        returns the current value
        """
        return self._current

def main():
    pass

if __name__ == '__main__':
    main()
