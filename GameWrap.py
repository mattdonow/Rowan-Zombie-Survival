########################################################
##Matt Donow
##Electrical and computer Engineering
##Rowan University '15
##Intro to Virtual Reality Spring 2014
##
##Project: Rowan Zombie Survival
##Name: Game Wrap
##filename:GameWrap.py
##
##Purpose: Wrapper for main Game
##Dependencies: 
##License:
######################################################################
import viz
import vizcam
import vizproximity
import vizinfo


import Human
import Items
import Zombie
import BattleManager
class GameWrap(viz.EventClass):
	def __init__(self):
		
		
		viz.EventClass.__init__(self)
		self.ActiveZombiesCount=0
		item=Items.Item()
		self.player=Human.Human('Matt',20,3,0,10,[0,0,0],item,'testchar.osgb')
		self.infobar={}
		#self.zombie=viz.add('testchar.osgb',scene=3)
		self.myscene=viz.add('testscene.osgb',scene=3)
		#self.testchar=viz.add('vcc_male.cfg',scene=3)
		self.zombies=Zombie.ZombieInit()
		
		
		self.target = vizproximity.Target(viz.MainView)
		self.manager = vizproximity.Manager()
		self.manager.addTarget(self.target)
		for  sensor in self.zombies.sensors:
			self.manager.addSensor(sensor)
		#self.manager.addSensor(self.sensor)
		self.manager.onEnter(None,self.EnterProximity)
		self.manager.onExit(None,self.ExitProximity)
		self.setupHealthStats(self.player)
		
		
		#testchar.setPosition(5,0,2)
		#myscene.setScale(.3,.3,.3)
		import vizshape
		vizshape.addAxes(scene=3)
	
		viz.MainView.collision( viz.ON )
		#viz.MainView.setPosition( [1, 1, 0] )

		self.camera=vizcam.KeyboardCamera(forward='w',

                                 backward='s',

                                 left='q',

                                 right='e',

                                 up='r',

                                 down='f',

                                 turnRight='d',

                                 turnLeft='a',

                                 pitchDown='h',

                                 pitchUp='y',

                                 rollRight='j',

                                 rollLeft='g',

                                 moveMode=viz.REL_LOCAL,

                                 moveScale=1.0,

                                 turnScale=1.0)
#vizcam.PivotNavigate()

		#myscene.setScale(.1,.1,.1)
		self.myscene.setPosition(0,0,0)
		directionLight=viz.addLight()
		directionLight.setAxisAngle( [1, 0, 0 , -90] ) 
		directionLight.color(1,1,1)
		directionLight.setPosition(0,100,0)
		directionLight.spread(360)

		self.myscene.enable(viz.LIGHTING)
	
	def EnterProximity(self,e):
		"""@args vizproximity.ProximityEvent()"""
		print 'entered',e.sensor
		a=e.sensor.getSourceObject()
		b=e.sensor.getSource()
		print b._node
		print self.zombies.zombies[b._node].name
		zombie=self.zombies.zombies[b._node]
		self.setupHealthStats(zombie)
		
		self.bm=BattleManager.BattleManager(self.player,zombie)
		self.callback(viz.KEYDOWN_EVENT,self.onKeyDown)
		
	def ExitProximity(self,e):
		print 'exited',e.sensor
		a=e.sensor.getSourceObject()
		b=e.sensor.getSource()
		print b._node
		print self.zombies.zombies[b._node].name
		zombie=self.zombies.zombies[b._node]
		self.removeHealthStats(zombie)
		self.callback(viz.KEYDOWN_EVENT,0) #remove callback when outdw of range
		
	def setupHealthStats(self,charactor):
		
		self.message=charactor.playerStatusString()
		name=charactor.getName()
		
		
		self.infobar[name]=vizinfo.add(self.message)
		self.infobar[name]._group.parent(viz.SCREEN, 3)
		self.infobar[name].title("Stats and Options")
		self.infobar[name].drag(viz.ON)
		
	def updateHealthStats(self,charactor):
		name=charactor.getName()
		self.message=charactor.playerStatusString()
		self.infobar[name].message(self.message)
		
	def removeHealthStats(self,charactor):
		name=charactor.getName()
		g=self.infobar[name]
		g.remove()
		
	def onKeyDown(self,key):
		if key==' ':
			#gm=BattleManager.BattleManager(self.player,self.zombie)
			self.bm.attack()
			self.updateHealthStats(self.player)
			
		
	
		
		
		

def main():
	viz.go()
	viz.scene(3)
	m=GameWrap()
	viz.link(viz.MainView,m.player.model)
	
	
	
	

if __name__ == '__main__':
    main()
