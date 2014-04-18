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


# Pound Includes
import viz
import pregame
import SceneManager
import viztask
import Human
viz.go()

sceneManager=SceneManager.SceneManager()
#Game
def ZombieGame():
			
			ActiveProgram=pregame.Intro() #Destructions info
			
			yield ActiveProgram.done.wait() #Wailt for intro screen to be done
			sceneManager.switchtoScene('Charactor')
			ActiveProgram=pregame.CharacterCreation()
			yield ActiveProgram.done.wait() #Wailt for charactor creation to be done
			
			
		#Schedule the task.
viztask.schedule( ZombieGame() )
#print 'onto next'

