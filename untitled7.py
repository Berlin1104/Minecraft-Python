# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 15:40:13 2018

@author: NTPU
"""

from mcpi.minecraft import Minecraft
HA = Minecraft.create()

x,y,z = HA.player.getPos()


def plantTree(x,y,z):
    HA.setBlocks(x-1,y+3,z-1,x+1,y+5,z+1,161)
    HA.setBlocks(x,y,z,x,y+4,z,17)
    
for i in range(10):
    for j in range(10):
        for k in range(5):
            plantTree(x+i*5,y+k*5,z+j*5)
    