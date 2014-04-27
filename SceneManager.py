########################################################
##Matt Donow
##Electrical and computer Engineering
##Rowan University '15
##Intro to Virtual Reality Spring 2014
##
##Project: Rowan Zombie Survival
##Name: Scene Manager
##filename:SceneManager
##
##Purpose: creates and manages Scenes
##Dependencies: 
##License:
######################################################################
import viz
class SceneManager():
	def __init__(self,startScene='Intro'):
		self._sceneDict={'Intro':1, 'Charactor':2,'GameWorld':3}
		self._currentScene=startScene
	
	def switchtoScene(self,sceneName):
		self._currentScene=sceneName
		viz.scene(self._sceneDict[sceneName])
	def getCurrentScene(self):
		return self._sceneDict[self._currentScene]
	