#-------------------------------------------------------------------------------
# Name:        BattleManager
# Purpose: Manages COMBAT

#------------------------------------------------------------------------------
import random
from Stats import Range

class BattleManager():
    """
    Manages Conflict
    """

    def __init__(self,human,zombies):
        """
        Initializes Battle Manager
        """
        #Attributes
        self._human=human #Instance of Human
        self._enemies=zombies # List of zombies
        self._enemyEngaged='' #Current enemy engaged in combat
        self._room=''
        self._fleed=False


        # Pythonic case statement for menu
        self._options={
                '1' : self._attack,
                '2' : self._flee,
                '3' : self._checkPlayer,
                '4' : self._suicide
               }
        self._continueBattle=True


    def battleLoop(self,room):
        """
        Loops through combat
        """

        self._room=room


        #Loop through Menu
        for x in  range(0,len(self._enemies)): #For each zombie in room
            if self._human.isAlive()==True: #if human is still alive
                self._continueBattle=True
                self._enemyEngaged=self._enemies[x] #grab zombie
                if self._enemyEngaged.isAlive()==True:
                    self._prepareCombat()

                while(self._continueBattle==True and self._human.isAlive()==True and self._enemyEngaged.isAlive()==True): #loop menu
                    selection=self._prompt()
                    self._options[selection]()
        return self._fleed



    def _prepareCombat(self):
        """
        Prints statement warning of combat
        """
        print """
-------------------------------------------------------
You encounter a zombie!
Prepare for combat!
Zombie %s, Power %s, Tougness %s, HP min%s/C%s/Max%s
-------------------------------------------------------
""" %(self._enemyEngaged.getName(),self._enemyEngaged.getPower(),self._enemyEngaged.getToughness(),self._enemyEngaged.hitpoints.getMin(),self._enemyEngaged.hitpoints.getCurrent(),self._enemyEngaged.hitpoints.getMax())
#Sorry
    def _prompt(self): #Menu Prompt
        """
        Prompts the user for combat actions
        """
        menu=' Select a Battle Option?:\n 1)Attack\n 2)Flee\n 3)Check Player\n 4)Suicide'
        return raw_input(menu)

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
        hp=self._fight(self._human, self._enemyEngaged)
        self._enemyEngaged.updateHitpoints(hp)
        print 'ATTACK!!!\n%s hit %s for %s' %(self._human.getName(),self._enemyEngaged.getName(),hp)



        #Zombie engaged in combat turn
        hp=self._fight( self._enemyEngaged,self._human,)
        self._human.updateHitpoints(hp)
        print 'ATTACK!!!\n%s hit %s for %s' %(self._enemyEngaged.getName(),self._human.getName(),hp)



        #Stop battle if when dead
        if not(self._human.isAlive()==True and self._enemyEngaged.isAlive()==True):
            self._continueBattle=False




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
