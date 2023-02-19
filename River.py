# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 18:04:03 2023

@author: Hannah
"""
import random
from Creatures import Bear
from Creatures import Fish


class River:
    
    def __init__(self, n_room):
        self.n_room = n_room
        self.river = [None] * self.n_room 
    
    #Creating a method to populate the river ecosystem with Bears and Fish
    def populate_river(self, animal):
        none_spot = [i for i in range(len(self.river)) if self.river[i] == None]
        if len(none_spot) > 0:
            random_spot = random.choice(none_spot)
            self.river[random_spot] = animal
    
    #Creating a method to advance time based on a specified number of rounds
    def next_time_step(self, n_rounds):
        for x in range(n_rounds):
            index = random.randint(0, len(self.river) - 1)
            if isinstance(self.river[index], Fish): 
                self.river[index].move(self.river, index)
            elif isinstance(self.river[index], Bear):
                self.river[index].move(self.river, index)
            elif self.river[index] == None:
                continue