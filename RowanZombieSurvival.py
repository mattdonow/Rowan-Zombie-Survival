########################################################
##Matt Donow
##Electrical and computer Engineering
##Rowan University '15
##Intro to Virtual Reality Spring 2014
##
##Project: Rowan Zombie Survival
##Name: Rowan Zombie Survival
##filename:RowanZombieSurvival
##
##Purpose: Main file for Zombie Survival Game
##Dependencies: 
##License:
######################################################################

import viz
import pregame
import SceneManager
import viztask
viz.go()

def ZombieGame():
			#Wait for a keypress.
			Introduction=pregame.Intro()
			yield viztask.waitButtonDown(Introduction.myButton)
			print 'onto next'

			
		#Schedule the task.
viztask.schedule( ZombieGame() )
#print 'onto next'

