import random
from itertools import combinations, groupby

class GetList:
	def __init__(self):
		self.new_country_list = []
		self.teams = []
		self.groups =[]
		self.dic = dict()

	def get_from_txt(self):
		with open('teams.txt','r') as file:
			lines = file.readlines()
			[self.new_country_list.append({'team':line.strip(), 'points':0, 'goals':0, 'goals_totais':0, 'victory':0,'loss':0, 'draw':0}) for line in lines]

	def random_teams(self):
		teams = random.sample(self.new_country_list, 36)
		for team in teams:
			self.teams.append(team)


	def group_teams(self):
		new_list = []
		while len(self.teams) > 0:
			if len(new_list) < 4 :
				new_list.append(self.teams.pop())
			elif len(new_list) >=4:
				self.groups.append(new_list)
				new_list = []
		#Aqui posso implementar numeros dos grupos(Grupo A, Grupo B, etc)
		with open('groups.txt', 'w') as file:
			file.write(str(self.groups) + '\n')
			

	def games(self):
		contador = 0
		games_list = []
		score_list = []
		for groups in self.groups:
			for group in combinations(groups,2):
				games_list.append(group)
		for line in games_list:
			line[0]['goals']=random.randint(0,5)
			line[0]['goals_totais']+=line[0]['goals']
			line[1]['goals']=random.randint(0,5)
			line[1]['goals_totais']+=line[1]['goals']
			score_list.append(f"{line[0]['team']} {line[0]['goals']} X {line[1]['goals']} {line[1]['team']}" +'\n')
			

			if line[0]['goals'] > line[1]['goals']:
				line[0]['points']+=3
				line[0]['victory']+=1
				line[1]['loss'] +=1

			if line[1]['goals'] > line[0]['goals']:
				line[1]['points'] +=3
				line[1]['victory']+=1
				line[0]['loss'] +=1

			if line[1]['goals'] == line[0]['goals']:
				line[0]['points']+=1
				line[0]['draw']+=1
				line[1]['points']+=1
				line[1]['draw']+=1
			
		
		with open('score.json','w') as arq:
			for lines in score_list:
				arq.write(lines)

	#Aqui defino os pontos ganhos a cada time dentro de cada grupo
	def group_results(self):
		ordena = lambda item: item['points']

		with open('groups.txt','w') as file:
			file.write(str(self.groups))
			
		

	def classification(self):
		ordena = lambda item: item['points']
		agrupados = ''
		with open('groups.txt', 'r') as file:
			document = file.readlines()
			for groups in combinations(document,2):
				print(groups)
			
			with open('classification.txt', 'w') as arch:
				pass
	
	

get_list = GetList()
get_list.get_from_txt()
get_list.random_teams()
get_list.group_teams()
get_list.games()
get_list.group_results()
get_list.classification()
