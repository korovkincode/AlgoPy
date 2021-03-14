class DequePy:
	def __init__(self, maxn):
		self.data = []
		self.maxsize = maxn
	def get_size(self):
		return len(self.data)
	def empty(self):
		return self.get_size() == 0
	def full(self):
		return self.get_size() == self.maxsize
	def front(self):
		if self.empty():
			return 'Empty'
		else:
			return self.data[0]
	def back(self):
		if self.empty():
			return 'Empty'
		else:
			return self.data[-1]
	def push_back(self, x):
		if self.full():
			return 'Full'
		else:
			self.data.append(x)
	def push_front(self, x):
		if self.full():
			return 'Full'
		else:
			self.data.insert(0, x)
	def pop_front(self):
		if self.empty():
			return 'Empty'
		else:
			self.data = self.data[1:]
	def pop_back(self):
		if self.empty():
			return 'Empty'
		else:
			self.data = self.data[:-1]