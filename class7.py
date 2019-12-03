class employee:

	num_emps=0
	raise_amount=1.04

	def __init__ (self,first,last,pay):
		self.first=first
		self.last=last
		self.pay=pay
		self.email=first+"."+last+"@company.com"
		employee.num_emps +=1

	#methods

	def fullname(self):
		return '{} {}'.format(self.first, self.last)

	def apply_raise(self):
		#self.pay=int(self.pay * employee.raise_amount)
		self.pay=int(self.pay * self.raise_amount) #or use instance

	#@classmethod #decorator
	#def set_raise_amount(cls,amount):
	#	cls.raise_amount=amount

	@classmethod #decorator
	def from_parse_string(cls,user_string):
		first,last,pay=user_string.split('-')
		return cls(first,last,pay)

	@staticmethod
	def is_workday(day):
		if day.weekday()>4:
			return False
		else:
			return True

class developer(employee):
	raise_amount=1.1

	def __init__ (self,first,last,pay,lang):
		super().__init__(first,last,pay)
		self.lang=lang

class manager(employee):
	raise_amount=1.4

	def __init__(self,first,last,employees=None):
		super().__init__(first,last,pay)
		if employees==None:
			self.employees=[]
		else:
			self.employees=employees

	def add_emp(self,emp):
		if emp not in self.employees:
			self.employees.append(emp)

	def del_emp(self,emp):
		if emp in self.employees:
			self.employees.remove(emp)
			
	def print_emp(self):
		for emp in self.employees:
		 print("-->"+emp.fullname())
			


emp1=employee('Allen','Jamerson',5000)
emp2=employee('James','Andersen',5000)
emp3=employee('Cops','Robersen',5000)

#employee.set_raise_amount(1.06)
print(emp1.__dict__)
print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)
print(employee.num_emps)


emp4Str='Brian-Hall-40000'
first,last,pay=emp4Str.split('-')
emp4=employee(first,last,pay)
print(emp4.first)

emp5str='Jim-Rickers-90000'

emp5=employee.from_parse_string(emp5str)
print(emp5.email)

import datetime
my_date=datetime.date(2016,7,11)
print(employee.is_workday(my_date))


dev1=developer('Matt','Daly',50000,'python')
dev2=developer('Kate','Nielsen',70000,'java')
#print(help(developer))
dev2.apply_raise()
print(dev1.lang)
print(dev2.pay)
print(dev2.email)

mgr1=manager('Liam',"Gordon",[dev1,dev2])
mgr1.print_emp()