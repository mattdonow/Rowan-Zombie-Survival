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
##ISSUES: Can only be in contact with 1 zombie at a time
######################################################################
import viz
import vizcam
import vizproximity
import vizinfo


import Human
import Items
import Zombie
import BattleManager
import viztask
class GameWrap(viz.EventClass):
	def __init__(self,playerName='Nameless'):
		self.objectSelection=False #Allow object selection
		viz.EventClass.__init__(self)
		self.callback(viz.KEYDOWN_EVENT,self.onKeyDown)
		self.callback(viz.MOUSEUP_EVENT,self.onMouseUp)
		
		self.done=viztask.Signal()
		self.item=Items.Item()
		self.player=Human.Human(playerName,1,1,0,10,[.2,6,0],self.item,'testchar.osgb')
		viz.MainView.setPosition(.25,3,.25) #Not sure why neccesarry, but it fixes it, no sense rebreaking it 
		self.infobar={}
		self.objectSelction=False
		#self.zombie=viz.add('testchar.osgb',scene=3)
		#self.myscene=viz.add('testscene.osgb',scene=3)
		self.myscene=viz.add('resources\\world.osgb',scene=3)
		
		
		
		#self.testchar=viz.add('vcc_male.cfg',scene=3)
		self.items=Items.ItemGenerator()
		self.zombies=Zombie.ZombieInit()
		
		self.enemyEngaged=None
		self.enableBattle=False
		
		
		
		self.target = vizproximity.Target(viz.MainView)
		self.manager = vizproximity.Manager()
		self.manager.addTarget(self.target)
		for  sensor in self.zombies.sensors:
			self.manager.addSensor(sensor)
		#self.manager.addSensor(self.sensor)
		self.manager.onEnter(None,self.EnterProximity)
		self.manager.onExit(None,self.ExitProximity)
		self.player.setupHealthStats()
		self.player.infobar.translate(.6,.95)
		
		
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
		self.enemyEngaged=self.zombies.zombies[b._node]
		
		self.enemyEngaged.setupHealthStats()
		
		self.bm=BattleManager.BattleManager(self.player,self.enemyEngaged,self.zombies,self.done)
		#self.callback(viz.KEYDOWN_EVENT,self.onKeyDown)
		self.enableBattle=True
	
	def ExitProximity(self,e):
		print 'exited',e.sensor
		
		
		self.enemyEngaged.removeHealthStats()
		#self.callback(viz.KEYDOWN_EVENT,0) #remove callback when outdw of range
		self.enableBattle=False
		
#	def setupHealthStats(self,charactor):
#		
#		self.message=charactor.playerStatusString()
#		name=charactor.getName()
#		
#		
#		self.infobar[name]=vizinfo.add(self.message)
#		self.infobar[name]._group.parent(viz.SCREEN, 3)
#		self.infobar[name].title("Stats and Options")
#		self.infobar[name].drag(viz.ON)
#		
#	def updateHealthStats(self,charactor):
#		name=charactor.getName()
#		self.message=charactor.playerStatusString()
#		self.infobar[name].message(self.message)
#		
#	def removeHealthStats(self,charactor):
#		name=charactor.getName()
#		g=self.infobar[name]
#		g.remove()
		
	def onKeyDown(self,key):
		if key==' ' and self.enableBattle==True:
			#gm=BattleManager.BattleManager(self.player,self.zombie)
			self.bm.battleLoop()
			self.player.updateHealthStats()
			self.enemyEngaged.updateHealthStats()
		elif key=='p' or key=='P':
			self.objectSelection=True
			print 'Object Selection Enabled'
##OBJECT SELECTION			
	def onMouseUp(self,button):
		print 'mouse clicked'
		if self.objectSelection==True:
			if button==viz.MOUSEBUTTON_LEFT:
				a=viz.pick(info=True)
				print 'picked'
				if (a.valid):
					print 'valid'
					print a.object
					
					try:
						tmpobject=self.items.items[a.object]
						allowPick=True
						print 'allowpick=true'
						
					except:
						allowPick=False
						print 'key not in dic'
						
					if allowPick:
						print 'allow pick'
						self.player.updateItem(tmpobject)
						
						tmpobject.model.remove()
						self.player.updateHealthStats()
					
					
		#a=e.sensor.getSourceObject()
		#b=e.sensor.getSource()
		#print b._node
		#print self.zombies.zombies[b._node].name
		#self.enemyEngaged=self.zombies.zombies[b._node]
					
					
					
					
					
				#else:
					#print 'Item is not in list'
					#print 'Object selection disabled'
					#self.objectSelection=False
					
					
##				tmpObject = viz.pick()
##				print self.object!=tmpObject
##				if (tmpObject.valid()) and (self.object!=tmpObject):
##					for roomName,pos,name in Zombie.zombies:
##						if tmpObject._node==name:
##							self.player.updateItem(tmpItem)
##							tmpObject.model.remove()
##							self.select==False
##							print 'object selection disabled'
#				else:
#					print 'object selection disabled'
#						
#					self.object=tmpObject
				#else:
					#self.object='None'
	
	
			
			
		
			
		
		
		

def main():
	viz.go()
	viz.scene(3)
	m=GameWrap()
	viz.link(viz.MainView,m.player.model)
	
	
	
	

if __name__ == '__main__':
    main()
