import requests as rq
import pandas as pd 
import numpy as np 

def getData(url_link):
    r = rq.get(url_link)
    json = r.json()
    table_names = json.keys()
    
    # dfList = {}
    teams = pd.DataFrame(json['teams'])
    numPlayers = json['total_players']
    elements = pd.DataFrame(json['elements'])
    element_types = pd.DataFrame(json['element_types'])

    elements['position'] = elements.element_type.map(element_types.set_index('id').singular_name)
    elements['team'] = elements.team.map(teams.set_index('id').name)

    elements.to_csv("elements.csv", index=False)


getData('https://fantasy.premierleague.com/api/bootstrap-static/')