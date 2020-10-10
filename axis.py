 # GLASS               = Block(20)                 
 # GOLD_BLOCK          = Block(41)            
 # IRON_BLOCK          = Block(42)                 
 # DIAMOND_BLOCK       = Block(57)                 
 # NETHER_REACTOR_CORE = Block(247) 

from mcpi.minecraft import Minecraft
from time import sleep


mc = Minecraft.create()
mc.postToChat("xyz-axis")


def draw_XYZ_axis0(mc=mc, wait=0.5, clear=False):
    blockTypeIdX = 1
    blockTypeIdY = 2
    blockTypeIdZ = 41
    blockTypeIdAir = 0
    blockTypeIdGround = 2

    # x-axis
    blockTypeId = blockTypeIdX
    if clear:
        blockTypeId = blockTypeIdAir
    mc.setBlocks(-20,  20,   0,   20, 20,   0,   blockTypeId)
    mc.setBlocks( 19,  20,  -1,   19, 20,   1,   blockTypeId)
    if clear:
        blockTypeId = blockTypeIdGround
    mc.setBlocks(-20,  -1,   0,   20,  -1,  0,   blockTypeId)
    mc.setBlocks( 19,  -1,  -1,   19,  -1,  1,   blockTypeId)
    sleep(wait)

    # y-axis
    blockTypeId = blockTypeIdY
    if clear:
        blockTypeId = blockTypeIdAir
    mc.setBlocks( 0,  0,  0,     0,  40,   0,   blockTypeId)
    sleep(wait)

    # z-axis
    blockTypeId = blockTypeIdZ
    if clear:
        blockTypeId = blockTypeIdAir
    mc.setBlocks(  0,  20, -20,    0,  20,  20,  blockTypeId)
    mc.setBlocks( -1,  20,  19,    1,  20,  19,  blockTypeId)
    if clear:
        blockTypeId = blockTypeIdGround
    mc.setBlocks(  0,  -1, -20,    0,  -1,  20,  blockTypeId)
    mc.setBlocks( -1,  -1,  19,    1,  -1,  19,  blockTypeId)

def draw_XYZ_axis(mc=mc, wait=0.1):
    # x-axis
    blockTypeId, blockData = 1, 0
    x, y, z = -20, 20, 0
    while x <= 20:
        mc.setBlock(x, y, z, blockTypeId, blockData)  # pseudo origin of coordinates
        mc.setBlock(x,-1, z, blockTypeId, blockData)  # ground level
        if x < 0:
            x += 2
            sleep(wait * 2)
        else:
            x += 1
            sleep(wait)
    # y-axis
    blockTypeId, blockData = 2, 0
    x, y, z = 0, 0, 0
    while y <= 40:
        mc.setBlock(x, y, z, blockTypeId, blockData)
        if y < 20:
            y += 2
            sleep(wait * 2)
        else:
            y += 1
            sleep(wait)
    # z-axis
    blockTypeId, blockData = 41, 0
    x, y, z = 0, 20, -20
    while z <= 20:
        mc.setBlock(x, y, z, blockTypeId, blockData)
        mc.setBlock(x,-1, z, blockTypeId, blockData)
        if z < 0:
            z += 2
            sleep(wait * 2)
        else:
            z += 1
            sleep(wait)

def reset_Minecraft_World(mc=mc):
    mc.setBlocks(-100, 0, -100,   100, 60, 100,    0)
    mc.setBlocks(-100,-1, -100,   100, -1, 100,    2)

#reset_Minecraft_World()

#draw_XYZ_axis0(clear=True)
#sleep(1)
#draw_XYZ_axis0(clear=False)
#sleep(10)
#draw_XYZ_axis0(clear=True)
draw_XYZ_axis0()
