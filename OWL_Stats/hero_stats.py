import csv

class hero_stats:
	#A class for saving data for OWL players that have played a given hero.


	def __init__(self, hero_name):
		""" Constructor: create a hero_stats object for hero_name hero.

		Args:
			hero_name (str): The name of the hero to be given to the hero_stats object.

		"""

		self.hero_name = hero_name
		self.__data = []


	def generate(self, csv_file, desired_stats=None):
		"""Parses the OWL Player Stats CSV file, saving data for the given hero.
		
		For each player that has played hero_name hero, a dictionary for that player is added
		to the list __data. Each stat is saved as a new item in the dictionary, with the key
		equal to the name of the stat in the CSV file, and the stat value as the value.
		
		Args: 
			csv_file (str): Path to the OWL Player Stats CSV file to be parsed
			desired_stats (str, list of str): Desired stats for the hero to be added to __data. 
				The format of these strings must match how the stat names are formatted in the 
				CSV file. If desired_stats is None, all stats are stored.
		"""

		if isinstance(desired_stats, str):
			desired_stats = [desired_stats]

		with open(csv_file, newline='')  as csvfile:
			csv_reader = csv.DictReader(csvfile)
			for row in csv_reader: #iterate over CSV rows
				if row['hero_name'] == self.hero_name:
					stat_name = str(row['stat_name'])
					stat_amount = float(row['stat_amount'])

					"""Only keep data if desired_stats is not set, or if the current stat matches a 
					key in desired stats
					"""
					if desired_stats==None or any(des == stat_name for des in desired_stats) or \
						stat_name == 'Time Played':

						"""Check if player is already in list. If so, return their entry. If not, 
						return None
						"""
						entry = next((player for player in self.__data if \
							player['player_name'] == row['player_name']), None)

						"""If there is no entry for that player, add a new dict to the list with 
						name and stat. Otherwise, either add a new item to the dictionary for a
						new stat, or add the stat value in row to the stored value
						"""
						if entry == None:
							self.__data.append({'player_name': row['player_name'], \
								stat_name: stat_amount})
						else:
							current_value = entry.get(row['stat_name']) #get saved stat value for player
							if current_value == None:
								entry[stat_name] =  stat_amount
							else:
								new_value = float(current_value) + stat_amount
								entry.update({stat_name: new_value})


	def filter_playtime(self, minimum_playtime):
		"""Removes entries from __data for players with less than minimum_playtime on the hero.

		Args:
			minimum_playtime (int): The minimum playtime in seconds to retain the player's record.
		"""
		self.__data = [entry for entry in self.__data if float(entry.get('Time Played')) >= minimum_playtime]


	def get_stat(self, stat, minimum_playtime=None):
		"""Returns a dict with each player and their associated value for the desired stat.

		Args:
			stat(str): The desired stat. Format must match stat name in CSV file.
			minimum_playtime(int): Minimum playtime in seconds to be included in output.
		"""
		if minimum_playtime == None:
			minimum_playtime = 0

		data = []
		for entry in self.__data:
			if entry['Time Played'] >= minimum_playtime:
				data.append({'player_name': entry['player_name'], stat: entry[stat]})

		return data


	def print(self):
		# Prints out the information stored in __data. Not formatted. Mostly for debugging.
		for entry in self.__data:
			print(entry)
