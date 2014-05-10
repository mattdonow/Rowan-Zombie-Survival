########################################################
##Matt Donow
##Electrical and computer Engineering
##Rowan University '15
##Intro to Virtual Reality Spring 2014
##
##Project: Rowan Zombie Survival
##Name: pregame
##filename:pregame
##
##Purpose: Handles pregame actions such as introduction and Charactor creation
##Dependencies: viz,
##License:
######################################################################
import viz
import vizcam
import vizact
import viztask
import Human
import Items


class Intro(viz.EventClass):
	def __init__(self):
		
		viz.EventClass.__init__(self)
		self.callback(viz.BUTTON_EVENT,self.onButton)
		self.rowantext="""
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



		vizcam.PivotNavigate(center=[15,-10,0],

                             distance=70,

                             sensitivity=[1.0,1.0])

		self.text_2D_world = viz.addText(self.rowantext,pos=[2, 2, 2])
		self.myButton = viz.addButtonLabel('continue',scene=1) #Add a button.
	

		self.myButton.setPosition(.5,.8) #Set its position. 
		self.myButton.setScale(1,1) #Scale it. 
		self.done=viztask.Signal()

		
	
		


	def onButton(self,obj,state):
		if obj==self.myButton:
			if state == viz.DOWN:
				self.done.send()
class CharacterCreation(viz.EventClass):
	def __init__(self):
		
		viz.EventClass.__init__(self)
		self.done=viztask.Signal()
		self.callback(viz.BUTTON_EVENT,self.onButton)
		self.rowantext="""
Charactor Creation
Enter Your Charactor's name:
"""



		vizcam.PivotNavigate(center=[15,-10,0],

                            distance=70,

                             sensitivity=[1.0,1.0])

		self.text_2D_world = viz.addText(self.rowantext,pos=[2, 2, 2],scene=2)
		self.myButton2 = viz.addButtonLabel('Done!',scene=2) #Add a button.

		self.myButton2.setPosition(.5,.5) #Set its position. 
		self.myButton2.setScale(1,1) #Scale it. 

		#Add a text box.
		self.box = viz.addTextbox(scene=2)
		#self.box.message('default')
		#Make it twice as long.
		self.box.length(2)
		#Place it in window.
		self.box.setPosition(.5,.8)
		#Have it grow when text reaches its boundary.
		self.box.overflow(viz.OVERFLOW_GROW) 


	def onButton(self,obj,state):
		if obj==self.myButton2:
			if state == viz.DOWN:
				name=self.box.get()
				playerName=name
				self.done.send(data=playerName)


