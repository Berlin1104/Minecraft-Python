# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 10:14:14 2018

@author: NTPU
"""
import time
from mcpi.minecraft import Minecraft
HA = Minecraft.create()

time.sleep(2)

x,y,z=HA.player.getPos()
HA.setSign(x,y,z,63,2,"WA","HA","HA","HAHA!!!")

