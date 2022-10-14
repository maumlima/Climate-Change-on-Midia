import pywikibot
from pywikibot import pagegenerators as pg
import json
import time
# request paralelle query

# open the monobigrams-labels-dictionary json as a dictionary
with open("Wikidata/monobigrams-labels-dictionary", "r") as fp:
  labels_dict = json.load(fp)

# dictionary to save the data to build the graphe
graphe_dict = {}

with open("Wikidata/monobigrams-labels-dictionary", "r") as fp:
  labels_dict = json.load(fp)

wikidata_site = pywikibot.Site("wikidata", "wikidata")

tic = time.time()
passer = 0
for bigram1 in labels_dict:
    if passer < 0:
        passer += 1
        continue
    else:
        print('Searching matchings for "{}"... (time: {}s)'.format(bigram1, round(time.time() - tic), 1))
        if labels_dict[bigram1] == []:
            continue

    for code1 in labels_dict[bigram1]:
        for bigram2 in labels_dict:
            if labels_dict[bigram2] == [] or bigram1 == bigram2:
                continue

            for code2 in labels_dict[bigram2]:
                # # direct link between words
                # QUERY = "SELECT ?item WHERE {\n\twd:" + code1 + "?item wd:" + code2 + "\n}LIMIT 1"
                # secondary link between words
                QUERY = "SELECT ?item WHERE {\n\twd:" + code1 + "?relation1 ?item.\n\t?item ?relation2 wd:" + code2 + "\n}LIMIT 1"
                
                try:
                    generator = pg.WikidataSPARQLPageGenerator(QUERY, site=wikidata_site)
                    for item in generator:
                        print("{} - {} [{}] (time: {}s)".format(bigram1, bigram2, item, round(time.time() - tic), 1))
                        if bigram1 in graphe_dict:
                            graphe_dict[bigram1].append(bigram2)
                        else:
                            graphe_dict[bigram1] = [bigram2]

                        # save the dictionary in json
                        with open("Wikidata/graphe-dictionary", "w") as fp:
                            json.dump(graphe_dict, fp)

                except pywikibot.exceptions.NoWikibaseEntityError:
                    pass