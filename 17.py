from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z=mc.player.getTilePos()
a=0
while a<20:
    mc.setBlocks(x-10,y-1,z,x+10,y-10,z,327)
    z=z-5
    a=a+1