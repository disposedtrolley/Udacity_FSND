class Parent():
	def __init__(self, last_name, eye_colour):
		print("Parent constructor called")
		self.last_name = last_name
		self.eye_colour = eye_colour

	def show_info(self):
		print("Last Name: " + self.last_name)
		print("Eye Colour: " + self.eye_colour)


class Child(Parent):
	def __init__(self, last_name, eye_colour, number_of_toys):
		print("Child constructor called")
		Parent.__init__(self, last_name, eye_colour)
		self.number_of_toys = number_of_toys

	def show_info(self):
		print("Last Name: " + self.last_name)
		print("Eye Colour: " + self.eye_colour)
		print("Number of toys: " + str(self.number_of_toys))


billy_cyrus = Parent("Cyrus", "blue")
# billy_cyrus.show_info()
miley_cyrus = Child("Cyrus", "blue", 5)
miley_cyrus.show_info()