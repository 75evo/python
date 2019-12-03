class Person:
	
	age=10

	def __init__ (self,name=None):
		self.name=name

p1=Person('Billy')
p2=Person('John')
p2.age=20
print (p2.age)
print (p2.name)