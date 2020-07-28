# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 16:18:56 2020

@author: appedu
"""
from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()
mc.setBlock(x+1,y,z+0,14)
mc.setBlock(x+2,y,z+0,14)
mc.setBlock(x+2,y,z+1,14)
mc.setBlock(x+2,y,z+2,14)
mc.setBlock(x+1,y,z+2,14)
mc.setBlock(x+0,y,z+2,14)
mc.setBlock(x+0,y,z+1,14)