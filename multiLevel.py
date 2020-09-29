class parent1():
	

	
	def view(self):
		print("this is parent 1")

class parent2(parent1):
	def view2(self):
		print("this is parent 2")

class child(parent2):
	def view3(self): 
		print("this is child")

ob = child()
ob.view()
ob.view2()
ob.view3()