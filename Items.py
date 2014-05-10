#-------------------------------------------------------------------------------
# Name:        Items
# Purpose: contains Item and ItemGenerator classes for managing items in the game

#-------------------------------------------------------------------------------
import Entity
import Stats
import random
import viz


#ITEMS

itemList=[
#Name,power,toughness, pos, model
['toilet', 1,2,[8,0,2],'Shen_Urinal.OSGB']
]


class Item(Entity.Entity):#  ? Inherits from Entity. Objects that can be picked up by the player and equipped to increase power/toughness.
    def __init__(self, name='None', power=0, toughness=0,pos=[0,0,0],model='None'):
        """
        Creates an item. use Item( name,description, power, toughness)
        """
        
        Entity.Entity.__init__(self,name)       #set name of object
        """
        Sets object Name
        """

        #self.description=description # ? a description of the object
        self.stats=Stats.Stats(power, toughness)   # ? an instance of stats, holding the power/toughness of the object.
        
        if model!='None':
            self.model=viz.add(model,scene=3)
        
            self.model.setScale(.1/3,.1/3,.1/3)
            self.model.setPosition(pos)
            print 'Item init, model pos'
            print self.model.getPosition()


   

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




class ItemGenerator: #?
       def __init__(self):
        """
        Generates the items
        """
         # a dictionary of all the possible items in the game
        self.items={}
        self.initialize()
       #  Methods:
        

       def initialize(self):
        """
        Creates the items specified in itemList
        """
        #['Toilet', 1,2,[4,0,2],'Shen_Urinal.OSGB']
        self.items={}
        ccc=0
        for name, power,toughness,pos,model in itemList:
            ccc=ccc+1
            print ccc
            tempItem=Item(name=name, power=power, toughness=toughness,pos=pos,model=model)
            tempItem=Item(name=name, power=power, toughness=toughness,pos=pos,model=model)
            a=tempItem.model
            print 'a model pos'
            print a.getPosition()
            self.items[a]=tempItem
            print 'adding object'
            print a
            #tempItem.model=viz.add(model)
            #self.items[name]=tempItem #Depreciated due to obtaining object via placing object in world
            
       
            

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



if __name__ == '__main__':
    main()
