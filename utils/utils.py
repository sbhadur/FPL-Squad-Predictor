import json
import requests

def getFullInfo():
    #All Info
    response = requests.get("https://fantasy.premierleague.com/api/bootstrap-static/")
    info = json.loads(response.text)
    return info

def getTop10BasedOnForm():
    #Get top 10 players based on form from each category: Defenders, GoalKeepers, Forwards, MidFielders
    info = getFullInfo()
    minDForm = float('-inf')
    minGForm = float('-inf')
    minMForm = float('-inf')
    minFForm = float('-inf')
    
    defenders = {}
    goalkeepers = {}
    midfield = {}
    forward = {}

    for element in info['elements']:
        if element['element_type'] == 1:
            if element['form'] > minGForm:
                minGForm = element['form']
                goalkeepers = element
        elif element['element_type'] == 2:
            if element['form'] > minDForm:
                minDForm = element['form']
                defenders = element
        elif element['element_type'] == 3:
            if element['form'] > minMForm:
                minMForm = element['form']
                midfield = element
        else:
            if element['form'] > minFForm:
                minFForm = element['form']
                forward = element
    
getTop10BasedOnForm()