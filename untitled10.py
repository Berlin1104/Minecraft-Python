# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 15:13:17 2018

@author: NTPU
"""

from random import randrange
from mcpi.minecraft import Minecraft
HA = Minecraft.create()

x,y,z = HA.player.getPos()

for j in range(10):
    x,y,z = HA.player.getPos()
    x = x+j
    for i in range(10):
        r = randrange(0,16)
        HA.setBlock(x,y,z,35,r)
        z = z+1
        
HA.postToChat("用劍打方塊")
r = randrange(0,16)
while True:
    hits = HA.events.pollBlockHits()
    if len(hits)>0:
        h = hits[0]
        
        block = HA.getBlockWithData(h.pos)
        data = block.data
        
        if data == r:
            HA.postToChat("恭喜你找到了!!")
            HA.setBlock(h.pos,57)
            break
        elif data>r:
            HA.postToChat("Wrong!!!找更小的顏色")
        elif data<r:
            HA.postToChat("Wrong!!!找更大的顏色")