import pandas as pd 
import numpy as np 
import statistics

ranks_data = pd.read_csv("data/US-News-Rankings-Universities.csv")

ranks_cln_data = []

for x in range (0, len(ranks_data)):

	name = ranks_data.at[x, 'Name']
	state = ranks_data.at[x, 'State']


	for y in range(0, 19):
		yr_string = ''
		if (y < 10):
			yr_string = "y0" + str(y)
		else:
			yr_string = "y" + str(y)

		rank = ranks_data.at[x, yr_string]

		entry = {
			"Name": name,
			"State": state,
			"rank": rank,
			"Year": "20" + yr_string[1:],
		}

		ranks_cln_data.append(entry)

	invalid_years = [85, 87]

	for y in range(84, 99):
		if (y not in invalid_years):
			yr_string = "y" + str(y)

			rank = ranks_data.at[x, yr_string]

			entry = {
				"Name": name,
				"State": state,
				"rank": rank,
				"Year": "19" + yr_string[1:],
			}

			ranks_cln_data.append(entry)



ranks = pd.DataFrame(ranks_cln_data)
ranks.to_csv("data/ranks.csv", index=False)