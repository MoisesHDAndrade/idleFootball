import random
from itertools import combinations,groupby


class App:

	def __init__(self):
		self.cup = []
		self.groups = []

	def define_cup(self):
		with open('teams.txt','r') as file:
			lines = file.readlines()
			group = [{'team':item.strip(),'points':0,'goals':0,'total_goals':0,'victory':0,'draw':0,'loss':0} for item in lines]
			#groups = {'teams':random.sample(lines,36)}
			self.cup = random.sample(group,36)
			with open('cup.txt', 'w') as arch:
				arch.write(str(self.cup))
			

	def define_groups(self):
		group = []
		while len(self.cup) > 0:
			if len(group) < 4:
				group.append(self.cup.pop())
			elif len(group) >=4:
				self.groups.append(group)
				group = []
		with open('groups.txt','w') as file:
			file.write(str(self.groups))
		

	def team_matches(self):
		lista = []
		for item in self.groups:
			for i in combinations(item,2):
				lista.append(i)
		for item in lista:
			print(f"{item[0]['team']} X {item[1]['team']}")
		print(lista)
		
app = App()
app.define_cup()
app.define_groups()
app.team_matches()
