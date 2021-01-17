from mcpi.minecraft import Minecraft
from mcpi.vec3 import Vec3
from time import sleep


# mc = Minecraft.create("primbell002.local")
mc = Minecraft.create()
mc.postToChat("Crane - UFO catcher")


class Crane():
    def __init__(self, cranePos):
        self.pos = cranePos
        self.isOpen = True
        Crane.draw(self)

    def clear(self):
        Crane.draw(self, clear=True)

    def openCraw(self, pose=0.5):
        if not self.isOpen:
            Crane.draw(self, clear=True)
            self.isOpen = True
            Crane.draw(self, clear=False)
        sleep(pose)

    def closeCraw(self, pose=0.5):
        if self.isOpen:
            Crane.draw(self, clear=True)
            self.isOpen = False
            Crane.draw(self, clear=False)
        sleep(pose)

    def draw(self, blockTypeId=41, blockData=0, clear=False):
        x, y, z = self.pos.x, self.pos.y, self.pos.z
        if clear:
            blockTypeId = 0
        # bar y=1..21
        mc.setBlocks(x, y + 1, z,  x, y + 21, z,   blockTypeId, blockData)
        # cross y=0
        mc.setBlocks(x + 3, y, z,      x - 3, y, z,        blockTypeId, blockData)
        mc.setBlocks(x,     y, z + 3,  x,     y, z - 3,    blockTypeId, blockData)

        # virtical upper  y=-1..-3
        mc.setBlocks(x + 3, y - 1, z,  x + 3, y - 3, z,   blockTypeId, blockData)
        mc.setBlocks(x - 3, y - 1, z,  x - 3, y - 3, z,   blockTypeId, blockData)
        # virtical upper  y=-1..-3
        mc.setBlocks(x, y - 1, z + 3,  x, y - 3, z + 3,   blockTypeId, blockData)
        mc.setBlocks(x, y - 1, z - 3,  x, y - 3, z - 3,   blockTypeId, blockData)

        if self.isOpen:
            # virtical lower  y=-4..-6
            mc.setBlocks(x + 3, y - 4, z,  x + 3, y - 6, z,   blockTypeId, blockData)
            mc.setBlocks(x - 3, y - 4, z,  x - 3, y - 6, z,   blockTypeId, blockData)
            # virtical lower  y=-4..-6
            mc.setBlocks(x, y - 4, z + 3,  x, y - 6, z + 3,   blockTypeId, blockData)
            mc.setBlocks(x, y - 4, z - 3,  x, y - 6, z - 3,   blockTypeId, blockData)
        else:
            # Crane  y=-4
            mc.setBlocks(x + 3, y - 4, z,     x + 1, y - 4, z,     blockTypeId, blockData)
            mc.setBlocks(x - 3, y - 4, z,     x - 1, y - 4, z,     blockTypeId, blockData)
            mc.setBlocks(x,     y - 4, z + 3, x,     y - 4, z + 1, blockTypeId, blockData)
            mc.setBlocks(x,     y - 4, z - 3, x,     y - 4, z - 1, blockTypeId, blockData)

    def move(self, dX=None, dY=None, dZ=None, speed=1, pose=0.5):
        step = 1
        if dX:
            if dX < 0:
                step = -1
            for i in range(cranePos.x, cranePos.x + dX, step):
                cranePos.x = i
                Crane.draw(self)
                sleep(0.1)
                Crane.draw(self, clear=True)
        if dY:
            if dY < 0:
                step = -1
            for i in range(cranePos.y, cranePos.y + dY, step):
                cranePos.y = i
                Crane.draw(self)
                sleep(0.1)
                Crane.draw(self, clear=True)
        if dZ:
            if dZ < 0:
                step = -1
            for i in range(cranePos.z, cranePos.z + dZ, step):
                cranePos.z = i
                Crane.draw(self)
                sleep(0.1)
                Crane.draw(self, clear=True)
        Crane.draw(self)
        sleep(pose)


# main

# mc.setBlocks(-50, 0, -50,   50, 40, 50,  0)

cranePos = Vec3(-10, 25, 5)
crane1 = Crane(cranePos)
crane1.move(pose=1)

for j in range(2):
    crane1.closeCraw(pose=1)
    crane1.openCraw(pose=1)
crane1.move(dX=40)
crane1.move(dZ=10)

crane1.move(dY=-10)
crane1.closeCraw(pose=2)
crane1.move(dY=10)
crane1.move(dX=-20)

crane1.openCraw(pose=3)

crane1.clear()
