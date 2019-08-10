roomTypes = {'1':{'N':True,'E':True,'S':True,'W':False,'Objects':[]}}

theMap = ['1;####',
          '1;1;1;1;1',
          '1;#;1;##',
          '##;1;1;#']


theMap = ['1####',
          '11111',
          '1#1##',
          '##11#']

def isMapPosValid(rx,ry):
    print(rx,ry)
    #print(theMap[ry][rx])
    try: tile = theMap[ry][rx]
    except IndexError: return 'Invalid'
    if not tile[0] == '#':
        return 'Valid'
    else:
        return 'Invalid'

def getMap():
    dummyMap = []
    for i in theMap:
        dummyMap.append(i)
    return dummyMap

def getMapPosInfo(rx,ry):
    if isMapPosValid(rx,ry) == 'Valid':
        roomType = roomTypes[theMap[ry][rx]]

        #canMoveNorth = roomType['N']
        #canMoveEast = roomType['E']
        #canMoveSouth = roomType['S']
        #canMoveWest = roomType['W']

        #print('N',canMoveNorth,'E',canMoveEast,'S',canMoveSouth,'W',canMoveWest)
        return roomType
