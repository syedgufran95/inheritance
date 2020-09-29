

class parent:
	def __init__(self,name,age):
		self.name=name
		self.age=age

	def view(self):
		print(self.name,self.age)

class child(parent):
	
	def __init__(self,name,age):
		#calling constructor of the parent class
		parent.__init__(self,name,age)
		self.roll=20

	def view(self):
		print(self.name,self.age,self.roll)


obj = child('Gufran',25)
obj.view()		
		
