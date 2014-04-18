#-------------------------------------------------------------------------------
# Name:        Entity
# Purpose: Base class that will provide basic functionality for all game objects

#------------------------------------------------------------------------------
class Entity:
    def __init__ (self,name="I'm Nameless!"):
        """Stores a name.
        """
        self.name=name

    def getName(self):
        """Returns a name
        """
        return self.name



def main():
    pass

if __name__ == '__main__':
    main()
