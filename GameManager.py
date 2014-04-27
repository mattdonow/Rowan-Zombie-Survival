#-------------------------------------------------------------------------------
# Name:        GameManager
# Purpose: manages all aspects of the game

#------------------------------------------------------------------------------
import Layout
import Human
import BattleManager
import Items
class GameManager():
    def __init__(self):
        """
        Creates the game manager to manage the game
        """

        self.layout=Layout.LayoutManager()
        self.items=Items.ItemGenerator()
        self.player='Null'
        self.playLoop=True #Gameloop vairable
        self.playGame=True #T/F for starting a NEW game







    def printIntro(self):
        """
        Print out awesome game introduction
        """
        print intro


    def startBool(self):
        """
        Prompts the user to start a new game or quit
        """
        print('New Game?')
        yesno=raw_input(" 1) Start New Game \n 2)Quit\n")

        if yesno=='1':
            return True
        else:
            return False

    def createPlayer(self):
        """
        Creates a new player, getting name from the input
        """
        print('Enter Your Name')
        name=raw_input('Charactor Name \n')
        print('Well hello, %s' %(name)) #Not a debugging statement, I like welcoming people

        self.player=Human.Human(name=name,power=10,toughness=10,min=0,max=10,locationName='Atrium')




    def gameLoop(self):
        """
        The Actual game loop. handles prompting and flow-of-action logic
        """
        fleed='False' # for determining if fleed. If they flee, they must leave room immediately as opposed to exploring it
        won=False #winning variable
        self.printIntro()
        self.playGame=self.startBool()

        while (self.playGame):
            self.createPlayer()
            self.playLoop=True
            while (self.playLoop):

            ######PLAY LOOOP#####################


                room=self.layout.getCurrentRoom()
                if room.getIsItemSpawnPoint()==True: #Generate item if it is random, so I can print
                    itemName=room.getItemName()
                    object=self.items.getItem(itemName)
                    itemName=object.getName()
                    room.changeItemName(itemName)

                if room.isSafeRoom()==True: #win if at safe room
                    won=True

                if not won:
                    spawn=room.getSpawnPoint()
                    #spawn if  zombies may be present. The battle manager handles the case where
                    #zombies may be present but 1 or more zombies are dead. (ie came back into a room)
                    if spawn==True:
                        bm=BattleManager.BattleManager(self.player,room.getZombies())

                        fleed=bm.battleLoop(room)

                    if self.player.isAlive()==True:
                        if fleed==True: #if fleed, they must exit room immediately. If they choose to stay in room, battle will recommence
                            self.leaveRoom()
                        else:
                            self.exploreOptions()
                    if not  self.player.isAlive():
                        self.playLoop=False
                else:
                    self.playLoop=False
            ######END PLAY LOOP
            if won==True:
                print('\n\n\nCONGRATS. LEVEL 1 of 1 COMPLETED. YOU WIN!!!!!!!!!!')
            else:
                print('\n\n\nYOU LOSE')
            print('\n\n\nWould you like to play again?')
            self.playGame=self.startBool()
        print("Thanks for playing Rowan Zombie Survival Guide. Hope you enjoyed!")



    def exploreOptions(self):
        """
        Allows player to explore the room and pick up objects
        """

        room=self.layout.getCurrentRoom()
        if room.getIsItemSpawnPoint()==True: #ITEM SPAWN LOOP
            print ('You find %s' %(room.getItemName()))
            string='1)Inspect Room \n2)Take Item \n3) Leave\n4)Quit'

            answer=raw_input(string)
            if answer=='1':
                self.inspectRoom()
            elif answer=='3':
                self.leaveRoom()
            elif answer=='2':
                self.takeItem()
            else:
                self.quit()



        else: #Non Item spawn loop

            string='1)Inspect Room \n2)Leave\n3)Quit'
            answer=raw_input(string)
            if answer=='1':
                self.inspectRoom()
            elif answer=='2':
                self.leaveRoom()
            else:
                self.quit()


    def inspectRoom(self):
        """
        Prints info about room
        """
        room=self.layout.getCurrentRoom()
        print room

        if room.getIsItemSpawnPoint()==True:
            itemname=room.getItemName()
            print self.items.getItem(itemname)


    def takeItem(self):
        """
        Allows player to take item(replacing current item)
        """
        room=self.layout.getCurrentRoom()
        itemName=room.getItemName()
        item=self.items.getItem(itemName)
        self.player.updateItem(item)
        room.removeItemSpawn()
        print('You take %s' %(item.getName()))


    def leaveRoom(self):
        """
        Allows player to leave room, or change their mind and stay in current room
        """
        inputDict={}
        n=1
        menu=''
        currentRoom=self.layout.getCurrentRoom()
        print('Where would you like to go?')
        for roomName in currentRoom.getConnections():
               #menu=menu+'\n' +str(n)+') '+ roomName
               menu+="%s) %s \n" % (n,roomName)
               #print menu
               inputDict[n]=currentRoom.getConnections()[roomName]
               n=n+1

        menu+="%s) Stay in current room" % (n)
        answer=raw_input(menu)



        if answer==str(n):
            pass

        else:
            for x in range(1, n):
                if answer==str(x):
                    i=inputDict[x]
              #Move to room
            self.layout.moveToRoom(i)
            self.player.locationName=roomName
            print('You moved to %s' %(roomName))











    def quit(self):
        """
        Allows user to quit the game
        """
        self.playLoop=False
        self.playGame=False



intro="""








 _____                      _____           _   _
| __  |___ _ _ _ ___ ___   |__   |___ _____| |_|_|___
|    -| . | | | | .'|   |  |   __| . |     | . | | -_|
|__|__|___|_____|__,|_|_|  |_____|___|_|_|_|___|_|___|


 _____             _         _    _____     _   _
|   __|_ _ ___ _ _|_|_ _ ___| |  |   __|_ _|_|_| |___
|__   | | |  _| | | | | | .'| |  |  |  | | | | . | -_|
|_____|___|_|  \_/|_|\_/|__,|_|  |_____|___|_|___|___|



May  2004: Electrical and Computer Engineering Students work on a new
           bio-algorithm to create zombies for the Biology Department.

July 2004: The Biology Department finds a major bug in the algorithm, and
           expects them to all die off, so he hides them under the Engineering
           Building.

Feb  2014: The Zombies are still alive. Due to the Engineering Building sinking
           6 inches, the Zombies are extremely uncomfortable and ESCAPE.


Instructions: Fight off the zombies to get to the roof of the Engineering
              Building. From there, you will zipline to the Science Building
              where the Biology Department can give you a cure.
              Make sure to grab objects along the way, so you can increase your
              power and toughness

GOOD LUCK. No pressure, just all of our lives depend on you




"""



def main():
    gm=GameManager()
    gm.gameLoop()

if __name__ == '__main__':
    main()
