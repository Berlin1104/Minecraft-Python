# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 15:31:03 2018

@author: NTPU
"""

import time
from mcpi.minecraft import Minecraft
HA = Minecraft.create()
time.sleep(3)


HA.postToChat("I'm watching you.WA HA HA")
while True:
    x,y,z = HA.player.getPos()
    HA.postToChat("You're loacted on:"+str(x) +str(y) +str(z))
    time.sleep(0.5)