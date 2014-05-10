﻿########################################################
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
		
		#viz.EventClass.__init__(self)
		#self.callback(viz.BUTTON_EVENT,self.onButton)








		vizcam.PivotNavigate(center=[15,-10,0],

                             distance=70,

                             sensitivity=[1.0,1.0])
	
		if win:
			self.text='CONRGATRULATIONS: YOU WON. Well, YOU WON this level. But there is only one level'
		else:
			self.text='YOU LOSE. Oh well.'
		self.text_2D_world = viz.addText(self.text,pos=[2, 2, 2],scene=4)
		#self.myButton = viz.addButtonLabel('continue',scene=1) #Add a button.
	

		#self.myButton.setPosition(.5,.8) #Set its position. 
		#self.myButton.setScale(1,1) #Scale it. 
		#self.done=viztask.Signal()

		
	
		


	#def onButton(self,obj,state):
	#	if obj==self.myButton:
	#		if state == viz.DOWN:
	#			self.done.send()