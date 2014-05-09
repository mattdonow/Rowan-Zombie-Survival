#-------------------------------------------------------------------------------
# Name:        Human
# Purpose: Playable charactor

#------------------------------------------------------------------------------
import Entity
import viz
import vizinfo
import Stats
import Items

class Human(Entity.Entity): # ? Inherits from Entity, represents the playable character.
    def __init__(self,name='player',power=0,toughness=0,min=0,max=0,location=[0,0,0],item=Items.Item(name='None', power=0, toughness=0,pos=[0,0,0],model='None'),model='test.osgb'):
        """
        Creates a Human Player. Use Human(name=,power,toughness,min,max,locationName,item)

        """
        #a. Attributes
        Entity.Entity.__init__(self,name)
        """
        creates Human name
        """
        self.model=viz.add(model,scene=3)
        
        self.model.setScale(.01,.01,.01)
        self.model.setPosition(location)
        self.power=power          #? the base power of the human
        self.toughness=toughness      #? the base toughness of the human
        self.hitpoints=Stats.Range(max,min,max)    #? instance of Range to hold the current number of hitpoints
        self.location=location   #? the name of the location of the human
        self.item=item          #? an instance of an item
        self.min=min
        self.max=max

        #b. Methods
    def getPower(self): #? returns the power of the human
        """
        Returns power of Human, summing human power and object power
        """
        power=Stats.Range(0,0,1000)

        power.setCurrent(self.power+self.item.getPower())
        return power.getCurrent()
        


    def getToughness(self) :#? returns the toughness of the human
        """
        Returns toughness of Human, summing human toughness and object toughness
        """
        toughness=Stats.Range(0,0,1000)
        toughness.setCurrent(self.toughness+self.item.getToughness())

        return toughness.getCurrent()
    def kill(self): # ? kills the human, making the HP equal to zero
        """
        Kills Human, sets HP=0
        """
        self.hitpoints.setCurrent(0)
        self.model.remove()
        self.removeHealthStats()
        


    def isAlive(self): # ? checks whether the human is alive or dead
        """
        Returns True if human is still alive
        """
        if self.hitpoints.getCurrent()>0:
            return True
        else:
            return False


    def updateHitpoints(self,hitpoints):
        """
        Updates hitpoints of Human
        """
        current=self.hitpoints.getCurrent()
        self.hitpoints.setCurrent(current-hitpoints)

    def updateItem(self,item):
        """
        Updates Item with new Item
        """
        self.item=item

    def playerStatusString(self): # to print out human attributes
        """
        Prints out human Attributes
        """
        #string= '%s:\n %s power %s toughness in %s. Hitpoints Min:%s/C:%s/Max:%s' % (self.name, self.getPower(), self.getToughness(), self.locationName,self.hitpoints.getMin(),self.hitpoints.getCurrent(), self.hitpoints.getMax())
        string='%s :\n Power: %s\n Toughness: %s\n Hitpoints: Min:%s/C:%s/Max:%s' % (self.name, self.getPower(), self.getToughness(),self.hitpoints.getMin(),self.hitpoints.getCurrent(), self.hitpoints.getMax())
        if self.item.getName()=='None':
            string=string
        else:
            string=string+'\n You have %s' %(self.item.getName())
        return string
        
    def setupHealthStats(self):

        self.message=self.playerStatusString()
        name=self.name
        
        
        self.infobar=vizinfo.add(self.message)
        
        self.infobar._group.parent(viz.SCREEN, 3)
        self.infobar.title("Stats and Options")
        self.infobar.drag(viz.ON)
    def removeHealthStats(self):
        name=self.name
        g=self.infobar
        g.remove()
    
    def updateHealthStats(self):
        name=self.name
        self.message=self.playerStatusString()
        self.infobar.message(self.message)





def main():
    pass

if __name__ == '__main__':
    main()
