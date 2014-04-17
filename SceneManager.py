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
class SceneManager():
	def __init__(self):
		self.sceneDict={'Intro':1, 'Charactor':2}
		self.currentScene='Intro'
	
	def switchtoScene(self,sceneName):
		self.currentScene=sceneName
		viz.scene(self.sceneDict[sceneName])