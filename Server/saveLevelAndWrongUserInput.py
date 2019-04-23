import json
import os

def goToLevel(state, currentLevel):
    response = {
        'state': state,
        'pageChanges': {
            "levelTitle": '',
            "levelDescription": ''
        }
    }
    data = openLevelFile()
    for level in data:
        if level["level"] == currentLevel:
            response['pageChanges']['levelTitle'] = level['levelTitle']
            response['pageChanges']['levelDescription'] = level['levelDescription']
            response['state']['level'] = level['level']
            return response

def takeItem(state, currentItem):
    print(currentItem)
    itemData = openItemFile()
    item = itemData[currentItem]
    newState = state
    newState['inventory'][currentItem] = item
    response = {
        'state': newState, 
        'pageChanges': {
                'levelChatboxText': 'You picked up ' + item["itemName"].upper() + '.'
        }
    }
    return response
    
def inspectItem(state, userInput):
    itemData = openItemFile()
    for item in itemData:
        print(item)
        if itemData[item]['itemName'].upper() in userInput:
            print(itemData[item]['itemName'])
            if item in state['inventory']:
                itemDescription = itemData[item]['itemDescription']
                response = {
                    'state': state, 
                    'pageChanges': {
                            'levelChatboxText': itemDescription
                    }
                }
                return response
            else:
                return {
                    'state': state, 
                    'pageChanges': {
                    'levelChatboxText': "Targarfbhsefbk ."
                    
                    }
                }    
    return {
            'state': state, 
            'pageChanges': {
                    'levelChatboxText': "You do not seem to be carrying that."
            }
    }
def handleInvalidDirection(state):
    response = {
        'state': state,
        'pageChanges': {
            'levelChatboxText': 'You cannot go that way.'
        }
    }
    return response  

def handleInvalidInput(userInput, state):
    response = {
        'state': state,
        'pageChanges': {
            'levelChatboxText': 'You cannot ' + userInput + '.'
        }
    }
    return response
"""
def handleInvalidTake(userInput, state):
    response = {
        'state': state,
        'pageChanges': {
            'levelChatboxText': 'You cannot take ' + userInput + '.'
        }
    }
    return response
"""
def openLevelFile():
    cwd = os.getcwd()  # Get the current working directory (cwd)
    filePath = cwd + '/Server/tutorial.json'
    
    with open(filePath, 'r') as getData:
        data = json.loads(getData.read())
        return data
        
def openItemFile():
    cwd = os.getcwd()  # Get the current working directory (cwd)
    filePath = cwd + '/Server/inventory.json'
    
    with open(filePath, 'r') as getData:
        data = json.loads(getData.read())
        return data