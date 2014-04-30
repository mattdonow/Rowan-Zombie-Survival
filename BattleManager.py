#-------------------------------------------------------------------------------
# Name:        BattleManager
# Purpose: Manages COMBAT

#------------------------------------------------------------------------------
import random
import viz
from Stats import Range

class BattleManager(viz.EventClass):
    """
    Manages Conflict
    """

    def __init__(self,human,zombie):
        """
        Initializes Battle Manager
        """
        viz.EventClass.__init__(self)
        #Register callback with our event class
        self.callback(viz.KEYDOWN_EVENT,self.onKeyDown)
        #Attributes
        self._human=human #Instance of Human
        self._enemies=zombies # List of zombies
       
        self._fleed=False


        # Pythonic case statement for menu
        self._options={
                '1' : self._attack,
                '2' : self._flee,
                '3' : self._checkPlayer,
                '4' : self._suicide
               }
        self._continueBattle=True
    def onKeyDown(self,key):
        if key==' ':
            self.attack()

    def battleLoop(self,room):
       pass

    def _flee(self): #Flee Action

        i=random.randint(0,1) #Random Chance of fleeing

        if i==1: #if flee
            print('You flee from battle')
            self._continueBattle=False
            #self._room.removeItemSpawn()
            self._fleed=True


        else:
            #zombies attack
            hp=self._fight( self._enemyEngaged,self._human,)
            self._human.updateHitpoints(hp)

    def _attack(self):
        """
        performs the attack, and update the charactors hitpoints.
        """

        #Human Attack
        hp=self._fight(self._human, self._zombie)
        self._zombie.updateHitpoints(hp)
        #print 'ATTACK!!!\n%s hit %s for %s' %(self._human.getName(),self._enemyEngaged.getName(),hp)



        #Zombie engaged in combat turn
        hp=self._fight( self._zombie,self._human,)
        self._human.updateHitpoints(hp)
        #print 'ATTACK!!!\n%s hit %s for %s' %(self._enemyEngaged.getName(),self._human.getName(),hp)



        #Stop battle if when dead
        #if not(self._human.isAlive()==True and self._enemyEngaged.isAlive()==True):
           # self._continueBattle=False




    def _fight(self,attacker, attackee):
        """
        Calculates hitpoints based on Characters Power and Toughness
        """
        #
        attackerPower=attacker.getPower()

        attackerToughness=attacker.getToughness()
        attackeePower=attackee.getPower()
        attackeeToughness=attackee.getToughness()

        if attackerPower> 4*attackeeToughness:
            hp=8
        elif attackerPower> 3*attackeeToughness:
            hp=5
        elif attackerPower> 2*attackeeToughness:
            hp=2
        elif attackerPower> attackeeToughness:
            hp=1
        else:
            hp=0
        return hp




    def _checkPlayer(self):
        """
        Prints the player's stats to the screen
        """
        print self._human
    def _suicide(self):
        """Allows the player to give up combat and end the game
        """
        self._human.kill()
        self._continueBattle=False




def main():
    pass

if __name__ == '__main__':
    main()
