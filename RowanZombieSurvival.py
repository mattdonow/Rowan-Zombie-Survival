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
import GameWrap
import vizcam
import postgame
viz.go()

sceneManager=SceneManager.SceneManager()
#Game
def ZombieGame():
			Status=True
			while(Status):
				print viz.MainScene
				viz.scene(1)
				ActiveProgram=pregame.Intro() #Destructions info
			
				yield ActiveProgram.done.wait() #Wailt for intro screen to be done
				sceneManager.switchtoScene('Charactor')
				ActiveProgram=pregame.CharacterCreation()
				playerName=yield ActiveProgram.done.wait() #Wailt for charactor creation to be done
				playerName=playerName.data
			
			
				sceneManager.switchtoScene('GameWorld')
				ActiveProgram=GameWrap.GameWrap(playerName)
				viz.link(viz.MainView,ActiveProgram.player.model)
				winStatus=yield ActiveProgram.done.wait()
				print 'You won?'
				print winStatus.data
				viz.scene(4)
				ActiveProgram=postgame.WinLose(winStatus.data)
				Status=yield ActiveProgram.done.wait()
				Status=Status.data
				print 'SHOULD I RESTART THE GAME'
				print Status
			
			
#viz.scene(3)
		#Schedule the task.
viztask.schedule(ZombieGame())
#print 'onto next'

