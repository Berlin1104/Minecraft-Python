# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 16:04:33 2018

@author: NTPU
"""
import time
from mcpi.minecraft import Minecraft
HA = Minecraft.create()

x,y,z = HA.player.getPos()
time.sleep(3)
while y <= 101:
    HA.setBlock(x,y-1,z,46)
    time.sleep(0.5)
    HA.setBlock(x+1,y-1,z,46)
    time.sleep(0.5)
    HA.setBlock(x+2,y-1,z,46)
    time.sleep(0.5)
    HA.setBlock(x+3,y-1,z-1,46)
    time.sleep(0.5)
    HA.setBlock(x+3,y-1,z-2,46)
    time.sleep(0.5)
    HA.setBlock(x+3,y-1,z-3,46)
    time.sleep(0.5)
    HA.setBlock(x+2,y-1,z-4,46)
    time.sleep(0.5)
    HA.setBlock(x+1,y-1,z-4,46)
    time.sleep(0.5)
    HA.setBlock(x,y-1,z-4,46)
    time.sleep(0.5)
    HA.setBlock(x-1,y-1,z-3,46)
    time.sleep(0.5)
    HA.setBlock(x-1,y-1,z-2,46)
    time.sleep(0.5)
    HA.setBlock(x-1,y-1,z-1,46)
    time.sleep(0.5)
    #y = y+1
