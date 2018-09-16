
class Group_Word:
	def __init__(self, description = "", x = 0, y = 0, width = 0, height = 0, is_math = 0):
		self.DESCRIPTION = description
		self.X = x
		self.Y = y
		self.WIDTH = width
		self.HEIGHT = height
		self.IS_MATH = is_math

	def toString(self):
		return [self.DESCRIPTION, self.X, self.Y, self.WIDTH, self.HEIGHT, self.IS_MATH]

	def get_description(self):
		return self.DESCRIPTION

	def get_x(self):
		return self.X

	def get_y(self):
		return self.Y

	def get_width(self):
		return self.WIDTH

	def get_height(self):
		return self.HEIGHT

	def get_math(self):
		return self.IS_MATH


	def set_description(self, description):
		self.DESCRIPTION = description

	def set_math(self, is_math):
		self.IS_MATH = is_math




	def merge(self, other_word):
		new_word = Group_Word(
			self.DESCRIPTION + " " + other_word.DESCRIPTION, 
			self.X, 
			self.Y, 
			abs(self.X - other_word.X) + other_word.WIDTH,
			abs(self.Y - other_word.Y) + self.HEIGHT, 
			self.IS_MATH)
		return new_word

	def should_merge_lines(self, other_word, space_y, img_height):
		
		#horizontal = False
		vertical = False

		#horizontal_diff = max(self.X, other_word.X) - min(self.X, other_word.X)
		#horizontal_diff = abs(other_word.X - self.X)
		#horizontal_diff = (img_width -horizontal_diff) / img_width 

		#horizontal = (horizontal_diff <= space_x)


		vertical_diff = abs(self.Y - other_word.Y)
		#vertical_diff = max(self.Y, other_word.Y) - min(self.Y, other_word.Y)
		#vertical_diff = (img_height - vertical_diff) / img_height 

		vertical = (vertical_diff <= space_y)
		math_merge = not((self.IS_MATH and not other_word.IS_MATH) or (not self.IS_MATH and other_word.IS_MATH))

		#return [horizontal and math_merge, vertical and math_merge] #Ensures math merges with math and non-math merges with non-math
		return [math_merge, vertical]