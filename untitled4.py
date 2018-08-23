# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 14:08:14 2018

@author: NTPU
"""

from mcpi.minecraft import Minecraft
HA = Minecraft.create()
while True:
    hits = HA.events.pollProjectileHits()
    if len(hits)>0:
        h = hits[0]
        x,y,z = h.pos.x,h.pos.y,h.pos.z
        HA.createExplosion(x,y,z,70)