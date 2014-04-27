#-------------------------------------------------------------------------------
# Name:        layout
# Purpose: manages layout. Contains Layoutmanager and room classes

#-------------------------------------------------------------------------------
import Zombie
import Entity
import Items
#Room list for now, eventually put this in an xml or something
rowanHallRooms=[

#name, description,  spawnPoint, itemSpawnPount,Item name, SafeRoom
#for item name, use 'Random' to spawn a random item

#6 rooms for now, Ill build more later. Shorter and better testing
['Atrium','An open area with A large 3 story window',  False,False,'None',False],
['RH101', ' A Classroom with tables, chairs, and whiteboard', True,True,'Random',False],
['RH201',' A classroom with round tables and Mac music lab', True,True, 'Random',False],
['RH237', ' An ECE lab with fancy monitors',False, True, 'Random', False],
['RH203',' An ECE Lab with Fancy Scopes',True,False,'None',False],
['Roof','The Zipline Awaits',False, False, 'None',True]
]

# One way connections
rowanHallOneWay=[
#From, To

['Atrium','RH201'],
['RH237','Roof'],
]

rowanHallTwoWay=[
['Atrium','RH101'],
['RH201','RH203'],
['RH237','RH203']
]


#Zombies
zombies=[
#roomName,name, power, toughness,hitpoints
['RH101','Dr. Merril',3,7,10],
['RH201','Dr. Head',4,3,10,],
['RH101','Dr. Rassa',5,3,10],
['RH201','Dr. Ravi',3,5,10],
['RH203','Krhcnavek',5,5,10]
]




class Room(Entity.Entity):
    def __init__ (self,name='hi', description='NULL',spawnPoint=False,isItemSpawnPoint=False,itemName='None',safeRoom=False):
        """
        Creates a room. use Room(name, description,spawnPoint,isItemSpawnPoint,itemName,safeRoom)
        spawnpoint is for zombies, while isItemSpawnPoint is to spawn an item
        """

        Entity.Entity.__init__(self,name)       #set name of room
        """
        creates room name
        """
        self._description=description            #  string describing the room
        self._zombies=[]                   # list of zombies in the room
        self._connections={}           #  dictionary mapping connected room names to room instances
        self._isSpawnpoint=spawnPoint           # ? spawn point Boolean flag to indicate the room creates zombies
        self._isItemSpawnPoint=isItemSpawnPoint #Bool flag to spawn item
        self._itemName=itemName                 #Name of item in room. Use 'Random' to spawn random
        self._safeRoom=safeRoom



#methods
    def  __str__(self): #? to print the room name, description and contents
        """
        prints string about room
        """
        return 'You are in  %s . %s ' % (self.name, self._description)


    def _addConnection(roomName,roomInstance):
        """
        Adds connections
        """
        self._connections[roomName] =roomInstance

    def getConnections(self):
        """
        Returns list of connections
        """
        return self._connections

    def getSpawnPoint(self):
        """
        Returns if it is a zombie spawnpoint
        """
        return self._isSpawnpoint

    def getZombies(self):
        """
        Returns list of zombie instances in room
        """
        return self._zombies

    def getIsItemSpawnPoint(self):
        """
        Returns boolean flag to spawn item.
        """
        return  self._isItemSpawnPoint
    def getItemName(self):
        """
        Return name of item in room
        """
        return self._itemName
    def removeItemSpawn(self):
        """
        Removes item spawn after item is taken (aka no infinite spawns
        """
        self._isItemSpawnPoint=False

    def isSafeRoom(self):
        """
        Returns if it is a winning room
        """
        return self._safeRoom
    def changeItemName(self,itemName):
        """
        Change Item name.
        """#Used to populate random item earlier than plan due to printing issue
        self._itemName=itemName








class LayoutManager:   #Handles generation of the game world, including all the rooms. Does the heavy listing of creating instances of every room, providing their information and connection information.
    def __init__ (self):
        """
        Creates all of the rooms in the game
        """
        self._rooms=[] #? List of all rooms
        self._currentRoomIndex=0
        self._name2InstanceMap={}
        self._createLayout()


    #b. Methods:
    def _createLayout(self): # ? to construct all the rooms in the game
        """
        Creates the actual layout
        """
        i=0

         #for name,description, zombies,connections, spawnpoint  in rowanHallRooms:
         #   self.createRoom(name,description, zombies, spawnpoint)
         #   i=i+1
        self._createRoom()
        for roomFrom,roomTo in rowanHallOneWay:
            self._addOneWayConnection(roomFrom,roomTo)
        for roomFrom,roomTo in rowanHallTwoWay:
            self._addTwoWayConnection(roomFrom,roomTo)

    def _createRoom(self):#,name,description, zombies, spawnpoint):
          """
          Creats an individual room. See Room list in Layout.py for info
          """
          i=0
          #create rooms
          for name,description, spawnpoint,itemSpawnPoint,item,safeRoom  in rowanHallRooms:
            tempRoom=Room(name,description,spawnpoint,itemSpawnPoint,item,safeRoom )
            self._rooms.append(tempRoom)
            self._name2InstanceMap[name]=i
            i=i+1
          #create zombies
          for roomName,name, power, toughness,hitpoints in zombies:
            zombietmp=Zombie.Zombie(name=name, power=power,toughness=toughness,min=0,max=hitpoints,locationName=roomName)
            roomid=self._name2InstanceMap[roomName]
            self._rooms[roomid]._zombies.append(zombietmp)

    def _addOneWayConnection(self,roomFrom, roomTo):# ? to create single direction room connection
        """
        Creates a one way connection between rooms
        """
        roomFromInstance=self._name2InstanceMap[roomFrom]
        roomToInstance=self._name2InstanceMap[roomTo]
        self._rooms[roomFromInstance]._connections[roomTo]=roomToInstance

    def _addTwoWayConnection(self, roomFrom, roomTo): #? to add connections in both directions between rooms
         """
         Creates a two way connection
         """
         self._addOneWayConnection(roomFrom, roomTo)
         self._addOneWayConnection(roomTo,roomFrom)

    def getCurrentRoom(self):
        """
        returns the room you are in
        NOTE: Will be depreciated soon in favor of another design to support multiplayer
        """
        return self._rooms[self._currentRoomIndex]
    def moveToRoom(self,index):
        """
        Moves player to room
        """
        self._currentRoomIndex=index




def main():
    pass

if __name__ == '__main__':
    main()