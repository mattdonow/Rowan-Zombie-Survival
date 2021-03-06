#-------------------------------------------------------------------------------
# Name:        Zombie
# Purpose: Zombie Charactor. As of now there is no difference from Human. May,
#and would like to change in the future

#------------------------------------------------------------------------------




import Human
import vizproximity

#Zombies
zombies=[
#roomName,Location,name, power, toughness,hitpoints, model
['RH101',[8.29522, 0, 9.23450],'Krchnavek',1,1,10,'testchar.osgb'],
['RH102',[14.83561, 0, 11.06440],'Leckakes',20,20,10,'testchar.osgb'],
['RH102',[37.99508, 0, 7.48554],'Polikar',1,1,10,'testchar.osgb']
]



class Zombie(Human.Human):
    def __init__(self,name='zombie',power=0,toughness=0,min=0,max=0,location=[0,0,0],model='test.osgb'):
        """
        Creates a zombie. As of now, there is no difference to Human
        """
        Human.Human.__init__(self,name=name,power=power,toughness=toughness,min=min,max=max,location=location,model=model)
        
        

    
class ZombieInit():
    
  #create zombies
    def __init__(self):
        self.zombies={}
        self.sensors=[]
        self.zombiesCount=0
        for roomName,location,name, power, toughness,hitpoints,model in zombies:
            zombietmp=Zombie(name=name,location=location, power=power,toughness=toughness,min=0,max=hitpoints,model=model)
            a=zombietmp.model
            self.zombies[a]=zombietmp
            mysensor=vizproximity.addBoundingSphereSensor(zombietmp.model)
            self.sensors.append(mysensor)
            self.zombiesCount=self.zombiesCount+1
            
        

def main():
    pass

if __name__ == '__main__':
    main()


