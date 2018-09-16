
class Group_Word:
	def __init__(self, description = "", x = 0, y = 0, width = 0, height = 0):
		self.DESCRIPTION = description
		self.X = x
		self.Y = y
		self.WIDTH = width
		self.HEIGHT = height

	def toString(self):
		return [self.DESCRIPTION, self.X, self.Y, self.WIDTH, self.HEIGHT]


	def merge(self, other_word):
		return group_word
		[	self.DESCRIPTION + " " + other_word.DESCRIPTION, 
			min(self.X, other_word.X), 
			min(self.Y, other_word.Y), 
			max(self.X, other_word.X) - min(self.X, other_word.X),
			max(self.Y, other_word.Y) - min(self.Y, other_word.Y)]

	def should_merge(self, other_word, space_x, space_y, img_width, img_height):
		horizontal = False
		vertical = False

		horizontal_diff = max(self.X, other_word.X) - min(self.X, other_word.X)
		horizontal_diff = int(horizontal_diff / img_width * 100) 

		horizontal = (horizontal_diff < space_x)


		vertical_diff = max(self.Y, other_word.Y) - min(self.Y, other_word.Y)
		vertical_diff = int(vertical_diff / img_height * 100) 

		vertical = (vertical_diff < space_y)

		return [horizontal, vertical]