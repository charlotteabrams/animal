from animal import Animal
class Dog(Animal):
	def __init__(self, name):
		#super(Dog, self).__init__()
		self.health = 150
		self.name = name
	def pet(self):
		self.health += 5
		return self

class Dragon(Animal):
	def __init__(self, name):
		#super(Dragon, self).__init__()
		self.health = 170
		self.name = name
	def fly(self):
		self.health -= 10
		return self
	def displayHealth(self):
		print self.name, "is a Dragon!" 
		return Animal.displayHealth(self)

dog1 = Dog("Willard")
dog1.walk().walk().walk().run().run().pet().displayHealth()

dragon1 = Dragon("Fern")
dragon1.walk().walk().walk().run().run().fly().fly().displayHealth()
