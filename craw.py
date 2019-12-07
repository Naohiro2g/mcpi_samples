from mcpi.minecraft import Minecraft
from time import sleep


#mc = Minecraft.create("primbell002.local")
mc = Minecraft.create()
mc.postToChat("craw - UFO catcher")


def drawCraw(mc=mc, x=0, z=0, y=0, blockTypeId=41, blockData=0, clear=False, open=True):
    if clear:
        blockTypeId = 0
    # bar y=1..21
    mc.setBlocks(x, y + 1, z,  x, y + 21, z,   blockTypeId, blockData)
    # cross y=0
    mc.setBlocks(x + 3, y, z,  x - 3 , y, z,   blockTypeId, blockData)
    mc.setBlocks(x, y, z + 3,  x, y, z - 3,    blockTypeId, blockData)

    # virtical upper  y=-1..-3
    mc.setBlocks(x + 3, y - 1, z,  x + 3, y - 3, z,   blockTypeId, blockData)
    mc.setBlocks(x - 3, y - 1, z,  x - 3, y - 3, z,   blockTypeId, blockData)
    # virtical upper  y=-1..-3
    mc.setBlocks(x, y - 1, z + 3,  x, y - 3, z + 3,   blockTypeId, blockData)
    mc.setBlocks(x, y - 1, z - 3,  x, y - 3, z - 3,   blockTypeId, blockData)

    if open:
        # virtical lower  y=-4..-6
        mc.setBlocks(x + 3, y - 4, z,  x + 3, y - 6, z,   blockTypeId, blockData)
        mc.setBlocks(x - 3, y - 4, z,  x - 3, y - 6, z,   blockTypeId, blockData)
        # virtical lower  y=-4..-6
        mc.setBlocks(x, y - 4, z + 3,  x, y - 6, z + 3,   blockTypeId, blockData)
        mc.setBlocks(x, y - 4, z - 3,  x, y - 6, z - 3,   blockTypeId, blockData)
    else:
        # craw  y=-4
        mc.setBlocks(x + 3, y - 4, z,  x + 1, y - 4, z,   blockTypeId, blockData)
        mc.setBlocks(x - 3, y - 4, z,  x - 1, y - 4, z,   blockTypeId, blockData)
        mc.setBlocks(x, y - 4, z + 3,  x, y - 4, z + 1,   blockTypeId, blockData)
        mc.setBlocks(x, y - 4, z - 3,  x, y - 4, z - 1,   blockTypeId, blockData)


while True:
    for x in range(-20, 20):
        drawCraw(x=x, z=5, y=15, blockTypeId=41, open=True)
        sleep(0.1)
        drawCraw(x=x, z=5, y=15, blockTypeId=41, clear=True)
    for i in range(4):
        drawCraw(x=x, z=5, y=15, blockTypeId=41, open=False)
        sleep(0.5)
        drawCraw(x=x, z=5, y=15, blockTypeId=41, open=False, clear=True)
        drawCraw(x=x, z=5, y=15, blockTypeId=41, open=True)
        sleep(0.5)
        drawCraw(x=x, z=5, y=15, blockTypeId=41, open=True, clear=True)
    for x in range(19, -21, -1):
        drawCraw(x=x, z=5, y=15, blockTypeId=41)
        sleep(0.2)
        drawCraw(x=x, z=5, y=15, blockTypeId=41, clear=True)
