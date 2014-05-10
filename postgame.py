########################################################
##Matt Donow
##Electrical and computer Engineering
##Rowan University '15
##Intro to Virtual Reality Spring 2014
##
##Project: Rowan Zombie Survival
##Name: postgame
##filename:postgame
##
##Purpose: Win/lose message
##Dependencies: viz,
##License:
######################################################################
import viz
import vizcam
import vizact
import viztask
import Human
import Items


class WinLose(viz.EventClass):
	def __init__(self,win):
		
		viz.EventClass.__init__(self)
		self.callback(viz.BUTTON_EVENT,self.onButton)







		viz.cam.reset()
		vizcam.PivotNavigate(center=[15,-10,-2],

                             distance=70,

                             sensitivity=[1.0,1.0])
	
		if win:
			self.text='CONRGATRULATIONS: YOU WON. Well, YOU WON this level. But there is only one level'
		else:
			self.text='YOU LOSE. Oh well.'
		self.text_2D_world = viz.addText(self.text,pos=[2, 2, 2],scene=4)
		#self.myButton = viz.addButtonLabel('Play Again',scene=4) #Add a button.
		#Weird Issue resetting scenes , disabling fo rnow

		#self.myButton.setPosition(.5,.) #Set its position. 
		#self.myButton.setScale(1,1) #Scale it. 
		self.done=viztask.Signal()
		self.myquit = viz.addButtonLabel('Quit Game',scene=4) #Add a button.
	

		self.myquit.setPosition(.5,.5) #Set its position. 
		self.myquit.setScale(1,1) #Scale it. 
		self.done=viztask.Signal()
		self.continu=False
		
	
		


	def onButton(self,obj,state):
		if obj==self.myButton:
			if state == viz.DOWN:
				self.continu=True
				#print continu
				self.done.send(data=self.continu)
				
				
		elif obj==self.myquit:
			self.continu=False
			viz.quit()
			self.done.send(data=self.continu)
			