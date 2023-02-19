# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 18:02:49 2023

@author: Hannah
"""
#Randomly select one aninmal from the list to move and have it act accordingly

#Write a Python program to simulate an ecosystem containing two types of creatures, bears and fish. The ecosystem consists of a river, which is modeled as a relatively large list. Each element of the list should be a Bear object, a Fish object, or None. In each time step, based on a random process, each animal either attempts to move into an adjacent list location or stay where it is. If two animals of the same type are about to collide in the same cell, then they stay where they are, but they create a new instance of that type of animal, which is placed in a random empty (i.e., previously None) location in the list. If a bear and a fish collide, however, then the fish died (i.e., it disappears).

from abc import ABCMeta, abstractmethod
import random

#Creating a parent class called "Creature" to be inherited later
class Creature(metaclass=ABCMeta):
    def __init__(self, animal):
        self.animal = animal
    
    @abstractmethod
    def move(self, river, spot):
        pass

  
#Creating a Bear class from Creature    
class Bear(Creature):
    def __init__(self):
        super().__init__("Bear")
    
    def move(self, river, index):
        none_spot = [i for i in range(len(river)) if river[i] == None]
        fish_spot = [i for i in range(len(river)) if isinstance(river[i], Fish)]
        bear_spot = [i for i in range(len(river)) if isinstance(river[i], Bear)]
        new_spot = index + random.choice([-1, 0, 1])
        if new_spot in none_spot: #bear moves to new empty spot
            river[new_spot] = self
            river[index] = None
        elif new_spot in fish_spot: #bear moves to new spot and eats the fish peacefully living there
            river[new_spot] = self
            river[index] = None
        elif new_spot in bear_spot:
            if len(none_spot) > 0: #Adds a baby bear to the river ecosystem if there's room
                bear_baby_spot = random.choice(none_spot)
                river[bear_baby_spot] = Bear()
        
#Creating a Fish class from Creature
class Fish(Creature):
    def __init__(self):
        super().__init__("Fish")
    
    def move(self, river, index):
        none_spot = [i for i in range(len(river)) if river[i] == None]
        fish_spot = [i for i in range(len(river)) if isinstance(river[i], Fish)]
        bear_spot = [i for i in range(len(river)) if isinstance(river[i], Bear)]
        new_spot = index + random.choice([-1, 0, 1])
        if new_spot in none_spot:
            river[new_spot] = self #fish successfully moves to new spot in the river
            river[index] = None #if the fish moves successfully, its previous spot will now be "None"
        elif new_spot in bear_spot: #uh oh, landed on a bear :/
            river[index] = None #fish eaten :(
        elif new_spot in fish_spot: #fish collide and create a baby fish
            if len(none_spot) > 0:
                fish_baby_spot = random.choice(none_spot)
                river[fish_baby_spot] = Fish()