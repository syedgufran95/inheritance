class parent1():
	
	def par1(self):
		print("this is parent 1")

class parent2():
		
		def par2(self):
			print("this is parent 2")

class child(parent1,parent2):
	def par3(self):
		print("this is child class")

obj = child()
obj.par1()
obj.par2()
obj.par3()
				