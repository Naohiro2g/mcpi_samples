from mcpi.minecraft import Minecraft
from time import sleep


mc = Minecraft.create()
mc.postToChat("pyramid maker")


def setPyramid(mc=mc, x=0, z=0, size=3, y=0, blockTypeId=41, blockData=0):
    while size > 0:
        mc.setBlocks(x, y, z, x + size - 1, y, z + size - 1, blockTypeId, blockData)
        x += 1
        z += 1
        size -= 2
        y += 1
        sleep(0.01)


def woolRainbow(mc=mc, x=0, z=0, size=7, n=64):
    for i in range(n):
        setPyramid(x=x, z=z, size=size, blockTypeId=35, blockData=(i % 16))
        sleep(0.25)


def clearField(mc=mc):
    mc.setBlocks(-50, 0, -50, 50, 19, 50, 0)


clearField()
sleep(1)
setPyramid(x=0, z=0, size=21, blockTypeId=41, blockData=0)
sleep(2)
setPyramid(x=15, z=15, size=15, blockTypeId=42, blockData=0)
sleep(2)
woolRainbow(x=0, z=20, size=11, n=32)