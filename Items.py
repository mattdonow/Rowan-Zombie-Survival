#-------------------------------------------------------------------------------
# Name:        Items
# Purpose: contains Item and ItemGenerator classes for managing items in the game

#-------------------------------------------------------------------------------
import Entity
import Stats
import random


#ITEMS
itemList=[
#Name, description,power,toughness
['Duck Tape','A roll of tape. It is silver', 1,2],
['Screw Driver', 'Flathead. Very small, but sharp',3,0],
['MATLAB 5.3 for Dummies','OLD, but quite entertaining',0,0],
['Shovel', 'A tool to move dirt',1,5],
['Fire Extinguisher','Put out a fire... or Zombie',3,2],
['LM741', 'From grandfathers toolbox',3,0], #Straight from digital II glossary
['TI MSP430', 'Best $4.50 you will ever spend',0,0], #except they raised the price
['Power Strip','for distributing your power',1,0]
]

class Item(Entity.Entity):#  ? Inherits from Entity. Objects that can be picked up by the player and equipped to increase power/toughness.
    def __init__(self, name='None',description='this is a item. Use it', power=0, toughness=0):
        """
        Creates an item. use Item( name,description, power, toughness)
        """
        Entity.Entity.__init__(self,name)       #set name of object
        """
        Sets object Name
        """

        self.description=description # ? a description of the object
        self.stats=Stats.Stats(power, toughness)   # ? an instance of stats, holding the power/toughness of the object.


        #Methods:
    def getDescription(self): #? returns the description of the object
        """
        Returns description of the item
        """
        return self.description


    def getPower(self):
        """
        Returns power of item
        """
        return self.stats.getPower()

    def getToughness(self):
        """
        Returns Touhness
        """
        return self.stats.getToughness()

       # return self.description
    def __str__(self): #? returns a string for printing out information about the item.
        """
        Prints description of item
        """
        return 'There is a  %s . %s. %s has power %s and toughness %s' % (self.name, self.description, self.name, self.stats.getPower(), self.stats.getToughness())


class ItemGenerator: #?
       def __init__(self):
        """
        Generates the items
        """
        self.items={} # a dictionary of all the possible items in the game
        self.initialize()
       #  Methods:


       def initialize(self):
        """
        Creates the items specified in itemList
        """
        for name,description, power,toughness  in itemList:
            tempItem=Item(name,description,power, toughness)
            self.items[name]=tempItem


       def getRandomItem(self): #? returns a random item in the game.
            """
            Creates a random Item
            """
            itemName=random.choice(self.items.keys()) #note to self: Self, Stack Overflow says this will need to be changed in version 3
            return self.items[itemName]

       def getItem(self,itemName): # ? returns an instance of a specific item by name.
            """
            If item is 'Random', it returns a Random Item. Else returns item by name
            """


            if itemName=='Random':
                return self.getRandomItem()
            else:
                return self.items[itemName]



def main():
    pass
#Random Test
##    rd='Random'
##    gen=ItemGenerator()
##    for x in range(1,500):
##        a=gen.getItem(rd)
##        print a.name


if __name__ == '__main__':
    main()
