from tinydb import TinyDB, Query

def insert_db():
	db = TinyDB('db.json')
	with open('teams.txt') as file:
		lines = file.readlines()
		[db.insert({'team':item.strip(),'points':0,'goals':0,'total_goals':0,'goals_taken':0,'goal_balance':0,'victory':0,'draw':0,'loss':0}) for item in lines]

insert_db()