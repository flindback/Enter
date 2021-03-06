from utilities import goToLevel, handleInvalidDirection, handleInvalidInput, takeItem, handleDoorLock, returnToMainHall, handlePersistantItems

def handleLivingRoom(userInput, state):
    if 'THROW' in userInput:
        return redPuzzle(state, userInput)
    elif userInput == 'TAKE RED KEY' or userInput == 'TAKE KEY' and 'carKeys' in state['isBurned']:
        return state['inventory'].pop('greyKey') and state['inventory'].pop('ladder') and returnToMainHall(state, 'redKey', 'MAIN_HALL_RETURN_FROM_RED')
    elif userInput == 'GO EAST':
        if 'photograph' in state['inventory']: 
            return goToLevel(state, 'KITCHEN', userInput) and handleNewKitchenDesc(state, userInput)
        else:
            return goToLevel(state, 'KITCHEN', userInput)
    elif userInput == 'GO WEST':
        if 'carKeys' in state['inventory']: 
            return goToLevel(state, 'HALL', userInput) and handleNewHallDesc(state, userInput)
        else:
            return goToLevel(state, 'HALL', userInput)
    elif userInput == 'GO NORTH' or userInput == 'GO SOUTH':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleKitchen(userInput, state):
    if userInput == 'GO WEST':
        if 'photograph' and 'carKeys' and 'canvas' in state['inventory']: 
            return goToLevel(state, 'LIVING_ROOM', userInput) and handleNewLivingRoomDesc(state, userInput)
        else:
            return goToLevel(state, 'LIVING_ROOM', userInput)
    elif userInput == 'TAKE PHOTOGRAPH':
        return takeItem(state, 'photograph') 
    elif userInput == 'TAKE STAIRS' or userInput == 'USE STAIRS':
        if 'ladder' in state['inventory']: 
            return goToLevel(state, 'BASEMENT', userInput) and handleNewBasementDesc(state, userInput)
        else:
            return goToLevel(state, 'BASEMENT', userInput)
    elif userInput == 'GO NORTH' or userInput == 'GO EAST' or userInput == 'GO SOUTH':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleBasement(userInput, state):
    if userInput == 'TAKE STAIRS' or userInput == 'USE STAIRS':
        if 'photograph' in state['inventory']: 
            return goToLevel(state, 'KITCHEN', userInput) and handleNewKitchenDesc(state, userInput)
        else:
            return goToLevel(state, 'KITCHEN', userInput)
    elif userInput == 'TAKE LADDER':
        return takeItem(state, 'ladder')
    elif userInput == 'TAKE TOYS' or userInput == 'TAKE OLD TOYS':
        return handleInvalidToy(state)
    elif userInput == 'GO WEST' or userInput == 'GO SOUTH' or userInput == 'GO EAST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleHall(userInput, state):
    if userInput == 'GO EAST':
        if 'photograph' and 'carKeys' and 'canvas' in state['inventory']: 
            return goToLevel(state, 'LIVING_ROOM', userInput) and handleNewLivingRoomDesc(state, userInput)
        else:
            return goToLevel(state, 'LIVING_ROOM', userInput)
    elif userInput == 'TAKE CAR KEYS' or userInput == 'TAKE KEY':
        return takeItem(state, 'carKeys')
    elif userInput == 'TAKE STAIRS' or userInput == 'USE STAIRS':
        if 'photograph' and 'carKeys' and 'canvas' in state['inventory']: 
            return goToLevel(state, 'UPPER_FLOOR', userInput) and handleFireLoudDesc(state, userInput)
        else:
            return goToLevel(state, 'UPPER_FLOOR', userInput)
    elif userInput == 'TAKE PICTURE':
        return handleInvalidPicture(state)
    elif userInput == 'GO SOUTH' or  userInput == 'GO WEST' or userInput == 'GO NORTH':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleUpperFloor(userInput, state):
    if userInput == 'TAKE STAIRS' or userInput == 'USE STAIRS':
        if 'carKeys' in state['inventory']: 
            return goToLevel(state, 'HALL', userInput) and handleNewHallDesc(state, userInput)
        else:
            return goToLevel(state, 'HALL', userInput)
    elif userInput == 'USE GREY KEY' or userInput == 'USE KEY' and "greyKey" in state["inventory"]:
            return handlePersistantItems(state, "GREY KEY", 'BEDROOM')
    elif userInput == 'GO WEST':
        if 'GREY KEY' in state['usedItems']:
            if 'canvas' in state['inventory']:
                return goToLevel(state, 'BEDROOM', userInput) and handleNewBedroomDesc(state, userInput)
            else:
                return goToLevel(state,'BEDROOM', userInput)
        else:
            return handleDoorLock(state, 'UPPER_FLOOR_W', userInput)
    elif userInput == 'USE LADDER' and "ladder" in state["inventory"]:
        if 'greyKey' in state['inventory']: 
            return goToLevel(state, 'ATTIC', userInput) and handleNewAtticDesc(state, userInput)
        else:
            return goToLevel(state, 'ATTIC', userInput)
    elif userInput == 'GO NORTH':
        return handleDoorLock(state, 'UPPER_FLOOR_N', userInput)
    elif userInput == 'GO EAST' or  userInput == 'GO SOUTH':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleAttic(userInput, state):
    if userInput == 'GO SOUTH':
        return handleDoorLock(state, 'ATTIC', userInput)
    elif userInput == 'USE LADDER' and "ladder" in state["inventory"]:
        return goToLevel(state, 'UPPER_FLOOR', userInput)
    elif userInput == 'TAKE GREY KEY' or userInput == 'TAKE KEY':
        return takeItem(state, 'greyKey')
    elif userInput == 'TAKE BOX' or userInput == 'TAKE BOXES':
        return handleInvalidBox(state)
    elif userInput == 'GO NORTH' or userInput == 'GO WEST' or userInput == 'GO EAST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleBedroom(userInput, state):
    if userInput == 'GO EAST' and "greyKey" in state['inventory']:
        if 'photograph' in state['inventory'] and 'carKeys' in state['inventory'] and 'canvas' in state['inventory']: 
            state['inventory']['greyKey']['itemUse'] = True
            return goToLevel(state, 'UPPER_FLOOR', userInput) and handleFireLoudDesc(state, userInput)
        else:
            return goToLevel(state, 'UPPER_FLOOR', userInput)
    elif userInput == 'TAKE CANVAS':
        return takeItem(state, 'canvas')
    elif userInput == 'GO NORTH' or userInput == 'GO SOUTH' or userInput == 'GO WEST':
        return handleInvalidDirection(state)
    else:
        return handleInvalidInput(userInput, state)

def handleNewLivingRoomDesc(state, userInput):
    response = {
        'state': state,
        'pageChanges': {
            'levelTitle': "Living Room",
            'levelDescription': "With the photograph, car keys and canvas in your possession, you can feel the heat getting stronger and more violent. There is a huge message painted in red all over the room. Three Objects, Three Memories. You should try to throw objects into the fire.",
            'levelChatboxText': ' YOU ' + userInput.upper() + "."
        }
    }
    return response

def handleNewKitchenDesc(state, userInput):
    response = {
        'state': state,
        'pageChanges': {
            'levelTitle': "Kitchen",
            'levelDescription': "An old kitchen, but with some modern modifications. The fridge is old, and it doesn't work anymore. There are some stairs leading down to the basement.",
            'levelChatboxText': ' YOU ' + userInput.upper() + "."
        }
    }
    return response

def handleNewHallDesc(state, userInput):
    response = {
        'state': state,
        'pageChanges': {
            'levelTitle': "Hall",
            'levelDescription': "A small hall with a clothing rack on the side and a small red carpet with the letter 'A' on it. Why the letter 'A'? There are also some pictures and the wall, however, you can't seem to see persons' faces in the pictures for some reasons. Every face is blurry. Beneath the pictures is a small table with an empty bowl. There are some stairs leading up to the upper floor.",
            'levelChatboxText': ' YOU ' + userInput.upper() + "."
        }
    }
    return response

def handleNewBasementDesc(state, userInput):
    response = {
        'state': state,
        'pageChanges': {
            'levelTitle': "Basement",
            'levelDescription': "It's cold in the basement. There is not so much down here, just some old furnitures and some boxes filled with old toys, pictures, watches and so on. Most of it seems to be covered by a red cloth to protect them from getting all dusty. There are some stairs leading up.",
            'levelChatboxText': ' YOU ' + userInput.upper() + "."
        }
    }
    return response

def handleNewAtticDesc(state, userInput):
    response = {
        'state': state,
        'pageChanges': {
            'levelTitle': "Attic",
            'levelDescription': "The attic is very dark, but the sunbeams from the windows make it much easier to distinguish what hides behind the dark. There are some boxes with the label 'memories'.",
            'levelChatboxText': ' YOU ' + userInput.upper() + "."
        }
    }
    return response

def handleNewBedroomDesc(state, userInput):
    response = {
        'state': state,
        'pageChanges': {
            'levelTitle': "Bedroom",
            'levelDescription': "It looks like a regular bedroom, the walls are red, a bookcase filled with obviously books, photos, a tiny leather boot and a box full of old watches. There is a big round window in the room which is painted black, but it doesn't block the sunlight which is kind of odd.",
            'levelChatboxText': ' YOU ' + userInput.upper() + ".",
        }
    }
    return response

def handleFireLoudDesc(state, userInput):
    response = {
        'state': state,
        'pageChanges': {
            'levelTitle': "Upper Floor",
            'levelDescription': "You can hear a loud noise coming from the living room, it sounds like fire, but why is the fire so loud? There are some stairs leading up.",
            'levelChatboxText': ' YOU ' + userInput.upper() + "."
        }
    }
    return response

def handleInvalidPicture(state):
    response = {
        'state': state,
        'pageChanges': {
            'levelChatboxText': "The picture seems to be stuck to the wall."
        }
    }
    return response

def handleInvalidBox(state):
    response = {
        'state': state,
        'pageChanges': {
            'levelChatboxText': "The boxes seem to be too heavy for you, and you should have workout more..."
        }
    }
    return response

def handleInvalidToy(state):
    response = {
        'state': state,
        'pageChanges': {
            'levelChatboxText': "Get yourself together, you are not a child anymore."
        }
    }
    return response

def redPuzzle(state, userInput): 
    newState = state
    objectList = state["isBurned"]
    if 'CANVAS' in userInput or 'PHOTOGRAPH' in userInput or 'CAR KEYS' in userInput:
        if len(objectList) == 0 and userInput == 'THROW CANVAS' and 'canvas' not in state['isBurned']:
            objectList.append('canvas')
            newState['isBurned'] = objectList
            newState['inventory'].pop('canvas')
            return {
                'state': newState, 
                'pageChanges': {
                    'levelChatboxText': "You burn the canvas"
                }
            }
        elif 'canvas' in state['isBurned'] and userInput == 'THROW PHOTOGRAPH' and 'photograph' not in state['isBurned']:
            objectList.append('photograph')
            newState['isBurned'] = objectList
            newState['inventory'].pop('photograph')
            return {
            'state': newState, 
            'pageChanges': {
                'levelChatboxText': "You burn the photograph."
            }
        }
        elif 'photograph' in state['isBurned'] and userInput == 'THROW CAR KEYS' and 'carKeys' not in state['isBurned']:
            objectList.append('carKeys')
            newState['isBurned'] = objectList
            newState['inventory'].pop('carKeys')
            return {
            'state': newState, 
            'pageChanges': {
                'levelChatboxText': "You burn car keys. The fire slowly dies and what is left of the fire is ashes and a red key."
            }
        }
        elif 'canvas' in state['isBurned'] and userInput == 'THROW CANVAS' or 'photograph' in state['isBurned'] and userInput == 'THROW PHOTOGRAPH' or 'carKeys' in state['isBurned'] and userInput == 'THROW CAR KEYS':
            newState = state
            return {
                'state': newState,
                'pageChanges': {
                    'levelChatboxText': "You cannot throw the same item."
                }
            }
        else:
            newState['isBurned'] = []
            newState = state
            currentItem = []
            if 'canvas' not in state['inventory']:
                currentItem.append('canvas')
            if 'photograph' not in state['inventory']:
                currentItem.append('photograph')
            if 'carKeys' not in state['inventory']:
                currentItem.append('carKeys')
            newState = takeBurnItem(state, currentItem)
            return newState
    else:
        return {
                'state': state,
                'pageChanges': {
                    'levelChatboxText': "That doen't seems to be the right thing to do..."
                }
            }

def takeBurnItem(state, currentItems):
    newState = state
    canvas = {
        "itemName": "Canvas",
        "itemDescription": "It's a canvas painted entirely in the color red."
    }
    photograph = {
        "itemName": "Photograph",
        "itemDescription": "An old dusty photograph. It's a picture of two little girls, but you can't seem to see their faces."
    }
    carKeys = {
        "itemName": "Car keys",
        "itemDescription": "Just some regular car keys, nothing fancy. However, the number '3' is engraved in the car keys."
    }
    for item in currentItems:
        if item == 'canvas':
            newState['inventory']['canvas'] = canvas
        elif item == 'photograph':
            newState['inventory']['photograph'] = photograph
        elif item == 'carKeys':
            newState['inventory']['carKeys'] = carKeys
        response = {
        'state': newState,
        'pageChanges': {
                'levelChatboxText': 'It is not in the right order, you might want to read the description for each item for this level to solve this puzzle... The items are restored to your inventory.',
        }
    }
    return response