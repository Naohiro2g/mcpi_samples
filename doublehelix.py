from mcpi.minecraft import Minecraft
from time import sleep
from math import sin, cos, radians

mc = Minecraft.create()
mc.postToChat("DNA - mystery of the double helix")


def double_helix(x=0, z=0, y=0, r=5, turns=2, speed=1):
    resolution = 12
    a = 0
    while a < 360 * turns:
        x1, z1 = r * sin(radians(a)), r * cos(radians(a))
        mc.setBlock(x + x1, y, z + z1, 35, 2)
        x2, z2 = r * sin(radians(a + 180)), r * cos(radians(a + 180))
        mc.setBlock(x + x2, y, z + z2, 35, 3)
        sleep(0.1 / speed)
        a += (360 / r) / resolution
        y += (0.5 * (r + 3)) / resolution

#x,z=50,50
#mc.setBlocks(x + 10, 0, z + 10, x - 10, 63, z - 10,  0)

double_helix(x=50, z=50, y=0, r=5, turns=2, speed=1)