from OWL_Stats import hero_stats

x = hero_stats.hero_stats('Reinhardt')
x.generate("D:/Documents/OWL2020 Data Fun/OWLWeek2.csv", ['Earthshatter Kills', 'Earthshatter Stuns', 'Ultimates Used'])
x.filter_playtime(60*30)
x.print()

print(x.get_stat('Ultimates Used', 60*60))
