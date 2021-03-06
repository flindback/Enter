from tutorial import handleGreenHouse, handleOutside, handlePorch, handleNowhere
from mainHall import handleMainHall, handleMainHallAllKeys, handleMainHallBlueKey, handleMainHallPinkKey, handleMainHallRedKey
from greenDoor import handleBeach, handleCaptainsCabin, handleCellar, handleGate, handleShedFrontDoor, handleShed, handleBeachEastSide, handleShipwreck, handleLighthouse, handleLighthouseOutside, handleLighthouseTopFloor, handleOcean
from redDoor import handleUpperFloor, handleLivingRoom, handleKitchen, handleHall, handleBedroom, handleBasement, handleAttic
from pinkDoor import handleBabyRoom, handleCribRoom, handleMessyRoom, handleNursingRoom, handleStudyRoom, handleToyCarRoom
from blueDoor import handleBlueCorridor1, handleBlueCorridor2, handleBlueCorridor3, handleBlueCorridor4, handleBlueCorridor5, handleBlueCorridor6, handleBlueCorridor7, handleBlueCorridor8, handleBlueCorridor9, handleBlueStart, handleBlueFinish, handleTorchRoom
from mirrorRoom import handleMirrorRoom1, handleMirrorRoom2, handleJoy, handleAnger1, handleAnger2, handleLove, handleSadness1, handleSadness2
from endRoom import handleLastRoom
levels = {
    'OUTSIDE': handleOutside,
    'NOWHERE': handleNowhere,
    'GREENHOUSE': handleGreenHouse,
    'PORCH': handlePorch,
    'MAIN_HALL': handleMainHall,
    'MAIN_HALL_RETURN_FROM_GREEN': handleMainHall,
    'MAIN_HALL_RETURN_FROM_RED': handleMainHall,
    'MAIN_HALL_ALL_KEYS': handleMainHallAllKeys,
    'MAIN_HALL_RED_KEY': handleMainHallRedKey,
    'MAIN_HALL_PINK_KEY': handleMainHallPinkKey,
    'MAIN_HALL_BLUE_KEY': handleMainHallBlueKey,
    'BEACH': handleBeach,
    'CAPTAINS_CABIN': handleCaptainsCabin,
    'CELLAR': handleCellar,
    'GATE': handleGate,
    'SHED_FRONT_DOOR': handleShedFrontDoor,
    'SHED': handleShed,
    'BEACH_EAST_SIDE': handleBeachEastSide,
    'SHIPWRECK': handleShipwreck,
    'LIGHTHOUSE_OUTSIDE': handleLighthouseOutside,
    'LIGHTHOUSE': handleLighthouse,
    'LIGHTHOUSE_TOP_FLOOR': handleLighthouseTopFloor,
    'LIVING_ROOM': handleLivingRoom,
    'KITCHEN': handleKitchen,
    'HALL': handleHall,
    'UPPER_FLOOR': handleUpperFloor,
    'BEDROOM': handleBedroom,
    'BASEMENT': handleBasement,
    'ATTIC': handleAttic,
    'CRIB_ROOM': handleCribRoom,
    'BABY_ROOM': handleBabyRoom,
    'TOY_CAR_ROOM': handleToyCarRoom,
    'NURSING_ROOM': handleNursingRoom,
    'STUDY_ROOM': handleStudyRoom,
    'MESSY_ROOM': handleMessyRoom,
    'BLUE_START': handleBlueStart,
    'BLUE_TORCH_ROOM': handleTorchRoom,
    'BLUE_CORRIDOR_1': handleBlueCorridor1,
    'BLUE_CORRIDOR_2': handleBlueCorridor2,
    'BLUE_CORRIDOR_3': handleBlueCorridor3,
    'BLUE_CORRIDOR_4': handleBlueCorridor4,
    'BLUE_CORRIDOR_5': handleBlueCorridor5,
    'BLUE_CORRIDOR_6': handleBlueCorridor6,
    'BLUE_CORRIDOR_7': handleBlueCorridor7,
    'BLUE_CORRIDOR_8': handleBlueCorridor8,
    'BLUE_CORRIDOR_9': handleBlueCorridor9,
    'BLUE_FINISH': handleBlueFinish,
    'MIRROR_ROOM_1': handleMirrorRoom1,
    'MIRROR_ROOM_2': handleMirrorRoom2,  
    'JOY': handleJoy,
    'ANGER_1': handleAnger1,
    'ANGER_2': handleAnger2,
    'LOVE': handleLove,
    'SADNESS_1': handleSadness1,
    'SADNESS_2': handleSadness2,
    'END': handleLastRoom,
}

def levelChecker(userInput, state):   
    level = state['level']
    return levels[level](userInput, state)