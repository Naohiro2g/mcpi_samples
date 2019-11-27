from mcpi.minecraft import Minecraft
from time import sleep


mc = Minecraft.create()
mc.postToChat("pyramid maker")


def setPyramid(x=0, z=0, size=3, y=0, blockTypeId=41, blockData=0):
    while size > 0:
        mc.setBlocks(x, y, z, x + size - 1, y, z + size - 1, blockTypeId, blockData)
        x += 1
        z += 1
        size -= 2
        y += 1
        sleep(0.025)


def woolRainbow(x, z, size=7, n=64):
    for i in range(n):
        setPyramid(x=x, z=z, size=size, blockTypeId=35, blockData=(i % 16))
        sleep(0.25)


def clearField():
    mc.setBlocks(-50, 0, -50, 50, 19, 50, 0)


clearField()
sleep(1)
setPyramid(x=0, z=0, size=27, blockTypeId=41, blockData=0)
sleep(2)
setPyramid(x=15, z=15, size=27, blockTypeId=42, blockData=0)
sleep(2)
woolRainbow(x=0, z=20, size=27, n=513)