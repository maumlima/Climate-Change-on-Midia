from ctypes import util
import json
import pandas as pd

# read json file in a dictionary
with open("Wikidata/graphe-dictionary", "r") as f:
  graphe_dict = json.load(f)

# lists to create the csv
source = []
target = []
for key, values in graphe_dict.items():
  if type(values) == list:
    utilised_values = []
    for value in values:
        if value not in utilised_values:
          utilised_values.append(value)
          source.append(key)
          target.append(value)
  else:
    source.append(key)
    target.append(values)

# create the dataframe
graphe_df = pd.DataFrame({'Source': source, 'Target': target})

# passe to csv
graphe_df.to_csv("Visualization/ipcc-words-relations.csv", index=False)