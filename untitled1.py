# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 09:44:28 2018

@author: NTPU
"""
import random,time
from mcpi.minecraft import Minecraft
HA = Minecraft.create()

pos=HA.player.getPos()
while True:
    x = pos.x+random.uniform(-10,10)
    y = pos.y+40
    z = pos.z+random.uniform(-10,10)
    HA.spawnEntity(x,y,z,25)
    time.sleep(0.05)