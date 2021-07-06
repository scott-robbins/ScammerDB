class self:
	def __init__(self, me):
		self.be = me

	def __str__(self):
		return self.be

class this:
	def __init__(self):
		self.isdumb = True
		self.self = 'stupid'

	def __bool_(self):
		return self.isdumb

	def __str__(self):
		return str(self.self)

if __name__ == '__main__':
	confusing = this()
	confusing.self = self('LOL')
	if confusing:
		print(confusing)