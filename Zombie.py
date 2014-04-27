#-------------------------------------------------------------------------------
# Name:        Zombie
# Purpose: Zombie Charactor. As of now there is no difference from Human. May,
#and would like to change in the future

#------------------------------------------------------------------------------
import Human

class Zombie(Human.Human):
    def __init__(self,name='name',power=0,toughness=0,min=0,max=0,locationName='Rowan'):
        """
        Creates a zombie. As of now, there is no difference to Human
        """
        Human.Human.__init__(self,name,power,toughness,min,max,locationName)





def main():
    pass

if __name__ == '__main__':
    main()


