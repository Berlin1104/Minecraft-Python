# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 14:18:22 2018

@author: NTPU
"""
import time
from mcpi.minecraft import Minecraft
HA = Minecraft.create()

while True:
    HA.executeCommand("time add 10")
    time.sleep(0.01)