class QueuePy:
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
	def add(self, x):
		if self.full():
			return 'Full'
		else:
			self.data.append(x)
	def pop(self):
		if self.empty():
			return 'Empty'
		else:
			self.data = self.data[1:]