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
class GameWrap():
	def __init__(self):
		
		myscene=viz.add('testscene.osgb',scene=3)
		testchar=viz.add('vcc_male.cfg',scene=3)
		self.sensor = vizproximity.addBoundingSphereSensor(testchar)
		self.target = vizproximity.Target(viz.MainView)
		self.manager = vizproximity.Manager()
		self.manager.addTarget(self.target)
		self.manager.addSensor(self.sensor)
		self.manager.onEnter(None,self.EnterProximity)
		
		
		testchar.setPosition(5,0,2)
		#myscene.setScale(.3,.3,.3)
		import vizshape
		vizshape.addAxes(scene=3)
	
		viz.MainView.collision( viz.ON )
		#viz.MainView.setPosition( [1, 1, 0] )

		vizcam.KeyboardCamera(forward='w',

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
		myscene.setPosition(0,0,0)
		directionLight=viz.addLight()
		directionLight.setAxisAngle( [1, 0, 0 , -90] ) 
		directionLight.color(1,1,1)
		directionLight.setPosition(0,100,0)
		directionLight.spread(360)

		myscene.enable(viz.LIGHTING)
	def EnterProximity(self,e):
		"""@args vizproximity.ProximityEvent()"""
		print 'entered',e.sensor
		
	

def main():
	viz.go()
	viz.scene(3)
	m=GameWrap()

if __name__ == '__main__':
    main()
