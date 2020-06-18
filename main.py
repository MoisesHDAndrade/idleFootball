import random
from itertools import combinations,groupby


class App:

	def __init__(self):
		self.cup = []
		self.groups = []
	def define_cup(self):
		with open('teams.txt','r') as file:
			lines = file.readlines()
			#groups = {'teams':random.sample(lines,36)}
			groups = random.sample(lines,36)
			with open('cup.txt', 'w') as arch:
				arch.write(str(groups))
			self.cup = groups
		print(len(self.cup))

	def define_groups(self):
		group = []
		while len(self.cup) > 0:
			if len(group) < 4:
				group.append(self.cup.pop())
			elif len(group) >4:
				self.group.append(group)
				group = []
		with open('groups.txt','w') as file:
			file.write(str(self.groups))


app = App()
app.define_cup()
app.define_groups()
