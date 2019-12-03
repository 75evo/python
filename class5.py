class My2Vector(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def __add__(self, other):
		return My2Vector(self.x+other.x, self.y+other.y) 

v1 = My2Vector(1, 2)
print(v1)
v2 = My2Vector(3, 2) 
print(v2)
v3 = v1 + v2
print(v3)