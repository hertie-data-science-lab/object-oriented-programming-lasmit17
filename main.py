# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 18:05:41 2023

@author: Hannah
"""

from River import River
from Creatures import Bear
from Creatures import Fish

#Creating the river ecosystem
river = River(40)

#Let's add the animals!
for i in range(5):
    river.populate_river(Bear())
    river.populate_river(Fish())

#Runs the simulation a preselected number of times
river.next_time_step(20)

