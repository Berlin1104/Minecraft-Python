# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 09:18:15 2018

@author: NTPU
"""

from mcpi.minecraft import Minecraft
HA = Minecraft.create()

def buildPrtamid(x,y,z,block,base = 18):
    x,y,z = HA.player.getTilePos()
    #base = 18
    height = (base//2)+1
    
    for i in range(height):
        x1 = x + i
        y1 = y + i
        z1 = z + i
        
        x2 = x + base - i
        #y與y2相同
        z2 = z + base - i
        HA.setBlocks(x1, y1, z1, x2, y1, z2, block)
        if i!=0 and i!=height-1:
            HA.setBlocks(x1+1, y1, z1+1, x2-1, y1, z2-1,0)

x,y,z = HA.player.getPos()
buildPrtamid(x,y,z,46)

