import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
while True:
    mc.executeCommand("time add 50")
    time.sleep(0.0)