# Define a class for a football team, only the starting eleven (no substitutes/reserves)
# it can contain 3-5 defenders, 3-5 midfield players and 1-3 strikers; it has to have 11 players in total, 1 goalkeeper
# all players have stats from 1-10 (1 bad, 10 perfect)
# goalkeepers: communication, aerial reach, reflexes, passing, concentration, stamina, strength
# defenders: communication, tackling, heading, passing, concentration, stamina, strength
# midfield players: tackling, dribbling, heading, passing, concentration, stamina, strength
# strikers: dribbling, finishing, heading, passing, composure, stamina, strength
# create 3 teams of players, one with good players, one with medium players & one with weak players

class FotballTeam:
	def defenders(self,toby, andy, joe):
		self.toby = toby
		self.andy = andy
		self.joe = joe
	def midfield(self,james, adam, sam,paul):
		self.james= james
		self.adam = adam
		self.sam = sam
		self.paul = paul
	def strikers(self, johnny, tom, bilanden):
		self.johnny = johnny
		self.tom = tom
		self.bilanden = bilanden
	def goalkeeper(self,ronaldo):
		self.ronaldo = ronaldo

class Stats:

	class Defendersstats:
		def __init__(self,communication, aerial, reach, reflexes, passing, concentration, stamina, strength):
			self.communication = communication
			self.aerial = aerial
			self.reach = reach
			self.reflexes = reflexes
			self.passing = passing
			self.concentration = concentration
			self.stamina = stamina
			self.strength = strength

	class Midfieldstats:
		def __init__(self,tackling, dribbling, heading, passing, concentration, stamina, strength):
			self.tackling = tackling
			self.heading = heading
			self.passing = passing
			self.concentration = concentration
			self.dribbling = dribbling
			self.stamina = stamina
			self.strength = strength

	class Strikersstats:
		def __init__(self,dribbling, finishing, heading, passing, composure, stamina, strength):
			self.dribbling = dribbling
			self.finishing = finishing
			self.stamina = stamina
			self.strength = strength
			self.passing = passing
			self.heading = heading
			self.composure = composure

	class Goalkeeperstats:
		def __init__(self,dribbling, finishing, heading, passing, composure, stamina, strength):
			self.dribbling = dribbling
			self.finishing = finishing
			self.heading = heading
			self.passing = passing
			self.composure = composure
			self.stamina = stamina
			self.strength = strength
class GoodTeam:

class FairTeam:

class BadTeam:
