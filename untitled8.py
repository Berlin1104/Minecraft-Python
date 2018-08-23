# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 11:23:14 2018

@author: NTPU
"""

import random
from mcpi.minecraft import Minecraft
HA = Minecraft.create()

x,y,z = HA.player.getPos()

for i in range(20):
    r = random.randange(1,13)
    c = random.randange(0,16)
    l = random.randange(3,16)
    if r == 1 or 7:
        HA.setBlocks(x,y,z,x+l,y,z,35,c)
        x = x+l
    elif r == 2 or 8:
        HA.setBlocks(x,y,z,x-l,y,z,35,c)
        x = x-l
    elif r == 3 or 9:
        HA.setBlocks(x,y,z,x,y,z+l,35,c)
        z = z+l
    elif r == 4 or 10:
        HA.setBlocks(x,y,z,x,y,z-l,35,c)
        z = z-l
    elif r == 5 or 11:
        HA.setBlocks(x,y,z,x,y+l,z,35,c)
        y = y+l
    elif r == 6 or 12:
        HA.setBlocks(x,y,z,x,y-l,z,35,c)
        y = y-l