# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 14:39:25 2018

@author: NTPU
"""

from mcpi.minecraft import Minecraft
HA = Minecraft.create()

x,y,z = HA.player.getPos()

for i in range(50):
    HA.setBlock(x+i,y-1,z+i,2)
    HA.setBlock(x+i+1,y-1,z+i,1)
    HA.setBlock(x+i+2,y-1,z+i,2)