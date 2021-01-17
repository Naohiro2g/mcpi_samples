from mcpi.minecraft import Minecraft
from time import sleep
from math import sin, cos, radians

mc = Minecraft.create()

mc.postToChat("moving cube")


def rectangleMove(x0=10, z0=10, x1=-10, z1=-10, y=10,
                  size=2, speed=10, blockTypeId=41, blockData=0):
    s = size - 1
    x, z = x0, z0
    while z >= z1:
        mc.setBlocks(x, y, z,  x + s, y + s, z + s, blockTypeId, blockData)
        sleep(1.0 / speed)
        mc.setBlocks(x, y, z,  x + s, y + s, z + s, 0)
        z -= 1

    x, z = x0, z1
    while x >= x1:
        mc.setBlocks(x, y, z,  x + s, y + s, z + s, blockTypeId, blockData)
        sleep(1.0 / speed)
        mc.setBlocks(x, y, z,  x + s, y + s, z + s, 0)
        x -= 1

    x, z = x1, z1
    while z <= z0:
        mc.setBlocks(x, y, z,  x + s, y + s, z + s, blockTypeId, blockData)
        sleep(1.0 / speed)
        mc.setBlocks(x, y, z,  x + s, y + s, z + s, 0)
        z += 1

    x, z = x1, z0
    while x <= x0:
        mc.setBlocks(x, y, z,  x + s, y + s, z + s, blockTypeId, blockData)
        sleep(1.0 / speed)
        mc.setBlocks(x, y, z,  x + s, y + s, z + s, 0)
        x += 1


def circlularMove(r=10, y=10, size=2, speed=10, blockTypeId=41, blockData=0):
    resolution = 200
    s = size - 1
    a = 0
    while a <= 360:
        x, z = r * sin(radians(a)), r * cos(radians(a))
        mc.setBlocks(x, y, z,  x + s, y + s, z + s, blockTypeId, blockData)
        sleep(1.0/10)
        mc.setBlocks(x, y, z,  x + s, y + s, z + s, 0)
        a += (speed * 360 / r) / resolution

# for i in range(2):
#    rectangleMove(x0=10, z0=10, x1=-10, z1=-10, y=10, size=2, speed=40, blockTypeId=41)


for i in range(2):
    rectangleMove(x0=10, z0=10, x1=-10, z1=-10, y=10, size=5, speed=30, blockTypeId=41)

for i in range(5):
    circlularMove(r=12, y=10, size=5, speed=50, blockTypeId=41, blockData=0)
