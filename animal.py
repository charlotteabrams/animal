class Animal(object):
	def __init__(self, name):
		self.name = name
		self.health = 100
	def walk(self):
		self.health -= 1
		return self
	def run(self):
		self.health -= 5
		return self
	def displayHealth(self):
		if(self.health <= 0):
			self.health = 0
		print "Name: ", self.name, " Health: ", self.health
		return self

animal = Animal("Rhino")
animal.walk().walk().walk().run().run().displayHealth()