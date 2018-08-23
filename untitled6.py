# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 10:22:17 2018

@author: NTPU
"""

from mcpi.minecraft import Minecraft
HA = Minecraft.create()


number = 1
x,y,z = HA.player.getPos()

for j in range(8):
    for i in range(number):
        HA.spawnEntity(x,y.z,60)
        
        number = number*2
        HA.postToChat("恭喜妳生成了"+str(number)+"隻")