class MyVehicle:

	def __init__(self,make,model,year):
		self.make = make
		self.model = model
		self.year = year

	def vehicle_name(self):
		print("This car is : " + str(self.make)  +  " " + str(self.model) + " " + str(self.year))

v1 = MyVehicle("Alfa","Milano",1987)

print(v1.make,v1.model,v1.year)
v1.vehicle_name()