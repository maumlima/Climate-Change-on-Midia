import pywikibot
from pywikibot import pagegenerators as pg
import json

# open the most-frequent-words-list json as a list
with open("Extraction/most-frequent-monobigrams-list", "r") as fp:
  words_list = json.load(fp)

# dictionary to save a list of labels for all teh words in the list
labels_dict = {}

# one request for each word
for i in range(len(words_list)):
  QUERY = "SELECT DISTINCT ?item\nWHERE {\n\t?item rdfs:label '" + words_list[i] + "'@en.\n\t?item ?p ?o\n}"
  # yet to do : get all useful Q-codes from a key word

  wikidata_site = pywikibot.Site("wikidata", "wikidata")
  generator = pg.WikidataSPARQLPageGenerator(QUERY, site=wikidata_site)

  aux_list = []
  for item in generator:
    aux_list.append(str(item)[11:-2])
  
  labels_dict[words_list[i]] = aux_list

# # save the dictionary in json
# with open("Wikidata/monobigrams-labels-dictionary", "w") as fp:
#   json.dump(labels_dict, fp)

# save the dictionary in txt
with open('monobigrams-labels-dictionary.txt', 'w') as f:
    for key in labels_dict:
        f.write("%s" % key)
        for Qcode in labels_dict[key]:
          f.write(" %s" % Qcode)
        f.write("\n")