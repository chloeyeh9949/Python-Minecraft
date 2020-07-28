# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 15:50:08 2020

@author: appedu
"""
from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()
mc.setBlock(x,y,z,14)