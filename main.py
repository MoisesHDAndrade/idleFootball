import random
from itertools import combinations,groupby

class App:

	def __init__(self):
		
		self.cup = []
		self.groups = []
		self.round_of_sixteen = []

	def define_cup(self):
		with open('src/teams.txt','r') as file:
			lines = file.readlines()
			group = [{'team':item.strip(),'points':0,'goals':0,'total_goals':0,'goals_taken':0,'goal_balance':0,'victory':0,'draw':0,'loss':0} for item in lines]
			#groups = {'teams':random.sample(lines,36)}
			self.cup = random.sample(group,36)

			with open('src/cup.txt', 'w') as arch:
				arch.write(str(self.cup))
		

	def define_groups(self):
		contador = 0
		group = []
		while len(self.cup) > 0:
			if len(group) < 4:
				group.append(self.cup.pop())
			elif len(group) >=4:
				self.groups.append(group)
				group = []
		with open('src/groups.txt','w') as file:
			file.write(str(self.groups))
		for item in self.groups:
			
			contador+=1

	def team_matches_groups(self):
		lista = []
		results = []
		for item in self.groups:
			for i in combinations(item,2):
				lista.append(i)
		for item in lista:
			item[0]['goals'] = random.randint(0,5)
			item[1]['goals'] = random.randint(0,5)
			results.append(f"{item[0]['team']} {item[0]['goals']} X {item[1]['goals']} {item[1]['team']}")

			if item[0]['goals'] > item[1]['goals']:
				item[0]['points'] += 3 #Add 3 points to Team 0 if wins
				item[0]['victory'] += 1 #Add 1 victory to Team 0 if wins
				item[0]['total_goals'] += item[0]['goals'] #Add total goals from match
				item[0]['goals_taken'] += item[1]['goals'] #Add total goals taken from match
				item[0]['goal_balance'] = item[0]['total_goals'] - item[0]['goals_taken']
				item[1]['loss'] += 1
				item[1]['total_goals'] += item[1]['goals']
				item[1]['goals_taken'] += item[0]['goals']
				item[1]['goal_balance'] = item[1]['total_goals'] - item[1]['goals_taken']

			elif item[0]['goals'] < item[1]['goals']:
				item[1]['points']+=3
				item[1]['victory']+=1
				item[1]['total_goals'] += item[1]['goals']
				item[1]['goals_taken'] += item[0]['goals']
				item[1]['goal_balance'] = item[1]['total_goals'] - item[1]['goals_taken']
				item[0]['loss'] +=1
				item[0]['total_goals'] += item[0]['goals']
				item[0]['goals_taken'] += item[1]['goals']
				item[0]['goal_balance'] = item[0]['total_goals'] - item[0]['goals_taken']
			else:
				item[0]['total_goals'] += item[0]['goals']
				item[0]['goals_taken'] += item[1]['goals']
				item[0]['points']+=1
				item[0]['draw']	+=1
				item[0]['goal_balance'] = item[0]['total_goals'] - item[0]['goals_taken']

				item[1]['total_goals'] += item[1]['goals']
				item[1]['goals_taken'] += item[0]['goals']
				item[1]['points']+=1
				item[1]['draw']	+=1
				item[1]['goal_balance'] = item[1]['total_goals'] - item[1]['goals_taken']
		with open('src/groups.txt','w') as file:
			file.write(str(self.groups))
		with open('src/group_stage_matches.txt','w') as file:
			[file.write(str(item+'\n'))for item in results]




	def classification_for_round_of_sixteen(self):
		this_round = []
		for items in self.groups:
			items.sort(key=lambda i: (i['points'],i['goal_balance'],i['total_goals'] ),reverse=True)
			this_round.append(items)
		with open('src/groups.txt','w') as file:
			file.write(str(self.groups))
		for item in self.groups:	
			print(f"Team {item[0]['team']} | Points {item[0]['points']} | Goal Balance {item[0]['goal_balance']}| Goals {item[0]['total_goals']} | Wins {item[0]['victory']} | Draws {item[0]['draw']} | Loses {item[0]['loss']}")
			print(f"Team {item[1]['team']} | Points {item[1]['points']} | Goal Balance {item[1]['goal_balance']}| Goals {item[1]['total_goals']} | Wins {item[1]['victory']} | Draws {item[1]['draw']} | Loses {item[1]['loss']}")
			print(f"Team {item[2]['team']} | Points {item[2]['points']} | Goal Balance {item[2]['goal_balance']}| Goals {item[2]['total_goals']} | Wins {item[2]['victory']} | Draws {item[2]['draw']} | Loses {item[2]['loss']}")
			print(f"Team {item[3]['team']} | Points {item[3]['points']} | Goal Balance {item[3]['goal_balance']}| Goals {item[3]['total_goals']} | Wins {item[3]['victory']} | Draws {item[3]['draw']} | Loses {item[3]['loss']}")
			print("#################################################################################### ")
		
		# aqui estou pegando os 2 primeiros de cada grupo e atribuindo para next_stage
		self.round_of_sixteen = [item[0:2] for item in this_round]
		
	
	def round_of_sixteen_matches(self):

		print(f"{self.round_of_sixteen[0][0]['team']} X {self.round_of_sixteen[1][1]['team']}")
		print(f"{self.round_of_sixteen[0][1]['team']} X {self.round_of_sixteen[1][0]['team']}")
		print(f"{self.round_of_sixteen[2][0]['team']} X {self.round_of_sixteen[3][1]['team']}")
		print(f"{self.round_of_sixteen[2][1]['team']} X {self.round_of_sixteen[3][0]['team']}")
		print(f"{self.round_of_sixteen[4][0]['team']} X {self.round_of_sixteen[5][1]['team']}")
		print(f"{self.round_of_sixteen[4][1]['team']} X {self.round_of_sixteen[5][0]['team']}")
		print(f"{self.round_of_sixteen[6][0]['team']} X {self.round_of_sixteen[7][1]['team']}")
		print(f"{self.round_of_sixteen[6][1]['team']} X {self.round_of_sixteen[7][0]['team']}")
		
app = App()
app.define_cup()
app.define_groups()
app.team_matches_groups()
app.classification_for_round_of_sixteen()
app.round_of_sixteen_matches()