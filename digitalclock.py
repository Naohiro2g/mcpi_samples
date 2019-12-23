import mcpi.block as block
import mcpi.minecraft as minecraft
import time

"""
Dot matrix digits 5 wide by 7 high.
0 - voxel should be drawn
Anything else - voxel should be cleared
"""
digit_dots = {
	'0':[
' 000',
'0   0',
'0   0',
'0   0',
'0   0',
'0   0',
' 000',
],
	'1':[
'  0',
' 00',
'  0',
'  0',
'  0',
'  0',
' 000',
],
	'2':[
' 000',
'0   0',
'    0',
'   0',
'  0',
' 0',
'00000',
],
	'3':[
'00000',
'   0',
'  0',
'   0',
'    0',
'0   0',
' 000',
],
	'4':[
'   0',
'  00',
' 0 0',
'0  0',
'00000',
'   0',
'   0',
],
	'5':[
'00000',
'0',
'0000',
'    0',
'    0',
'0   0',
' 000',
],
	'6':[
'  00 ',
' 0',
'0',
'0000',
'0   0',
'0   0',
' 000',
],
	'7':[
'00000',
'    0',
'   0',
'  0',
' 0',
' 0',
' 0',
],
	'8':[
' 000',
'0   0',
'0   0',
' 000',
'0   0',
'0   0',
' 000',
],
	'9':[
' 000',
'0   0',
'0   0',
' 0000',
'    0',
'   0',
' 00',
],
	':':[
'',
'  00',
'  00',
'',
'  00',
'  00',
'',
],
}

class Buffer():
	"""
	Double-buffer a voxel message for Minecraft.
	To improve performance, only changes are rendered.
	"""

	last_message = ''
	offscreen = []
	onscreen = []

	def __init__(self, anchor_position=minecraft.Vec3(0, 8, 0)):
		"""
		Set everything up to render messages into the world
		at the given position.
		"""
		self.anchor_position = anchor_position

	def render(self, message, blockId=block.ICE, blockData=0):
		"""
		Put message into the off-screen buffer.
		"""
		if message != self.last_message: # Do nothing if the message has not changed.
			self.last_message =  message # For next time.

			self.offscreen = [] # Clear any previous use of the buffer.
			letter_offset = 0
			for letter in message:
				rendition = digit_dots[letter]
				line_offset = 0
				for line in rendition:
					if len(self.offscreen) <= line_offset:
						# Make space to store the drawing.
						self.offscreen.append([])
					dot_offset = 0
					for dot in line:
						if dot == '0':
							self.offscreen[line_offset].append(block.Block.withData(blockId, blockData))
						else:
							self.offscreen[line_offset].append(block.AIR)
						dot_offset += 1
					for _blank in range(dot_offset, 6):
						# Expand short lines to the full width of 6 voxels.
						self.offscreen[line_offset].append(block.AIR)
					line_offset += 1
				letter_offset += 1

			# Clear the onscreen buffer.
			# Should only happen on the first call.
			# Assumption: message will always be the same size.
			# Assumption: render() is called before flip().
			if self.onscreen == []:
				# No onscreen copy - so make it the same size as the offscreen image. Fill with AIR voxels.
				line_offset = 0
				for line in self.offscreen:
					self.onscreen.append([])
					for dot in line:
						self.onscreen[line_offset].append(block.AIR)
					line_offset += 1

	def flip(self, mc):
		"""
		Put the off-screen buffer onto the screen.
		Only send the differences.
		Remember the new screen for next flip.
		"""
		line_offset = 0
		for line in self.offscreen:
			dot_offset = 0
			for dot in line:
				if self.onscreen[line_offset][dot_offset] != dot:
					self.onscreen[line_offset][dot_offset] = dot
					mc.setBlock(self.anchor_position.x+dot_offset,self.anchor_position.y-line_offset,self.anchor_position.z, dot)
				dot_offset += 1
			line_offset += 1

	def clear(self, mc):
		x,y,z=self.anchor_position
		mc.setBlocks(x-2,y+2,z, x+48,y-8,z,  41, 2)
		mc.setBlocks(x-1,y+1,z, x+47,y-7,z,  0)

# clock drawing

mc = minecraft.Minecraft.create() # Connect to Minecraft.

x, y, z = 50 * 0, 10 * 2, -5
print("anchor point(left-bottom of the clock frame):", x, y, z)
bitmapper = Buffer(anchor_position=minecraft.Vec3(x, y + 8, z))
bitmapper.clear(mc)

while True:
	timestr = time.strftime("%H:%M:%S") # Format time nicely.
	bitmapper.render(timestr, blockId=block.DIAMOND_BLOCK, blockData=1)
	bitmapper.flip(mc)
	time.sleep(0.1) # Rest a while before drawing again.