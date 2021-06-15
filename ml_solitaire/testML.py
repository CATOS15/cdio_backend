import torch
import pandas
import json
import cv2

# TODO

# Model
model = torch.hub.load('ultralytics/yolov5', 'custom', path='ml_solitaire/yolov5v2/thebest.pt', source='local')
model.conf = 0.7

data_solitaire = {
    'stacks': [
    ],
    'fountains': [
    ],
    'cardpile': [
    ],
}


def getCardsFromImage(path):
    img = path
    results = model(img)
    resultsPanda = results.pandas().xyxy[0].to_json(orient="records")
    resultsJSON = json.loads(resultsPanda)
    cv2.imwrite("oink.png", path)
    s = set()
    for result in resultsJSON:
        s.add(result["name"])
    return s


def get_suit_value(s):
    if s == 'd':
        return 1
    elif s == 'h':
        return 2
    elif s == 's':
        return 3
    else:
        return 4


def get_card_value(s):
    card = ""
    suit = ""
    if len(s) > 2:
        suit = s[2]
        return {'number': 10, 'suit': get_suit_value(suit)}
    elif len(s) == 2:
        card, suit = s[0], s[1]

    if card == 'A':
        return {'number': 1, 'suit': get_suit_value(suit)}
    elif card == 'K':
        return {'number': 13, 'suit': get_suit_value(suit)}
    elif card == 'Q':
        return {'number': 12, 'suit': get_suit_value(suit)}
    elif card == 'J':
        return {'number': 11, 'suit': get_suit_value(suit)}
    elif int(card) > 1 and int(card) < 10:
        return {'number': int(card), 'suit': get_suit_value(suit)}

    return -1


def addToWaste(cards, solitaire):
    if len(cards) > 1:
        print("Error: Too many cards in waste, 1 < waste")
        return

    for card in cards:
        cardObj = get_card_value(card)
        solitaire['cardpile'].append(cardObj)


def addStackToTableau(cards, solitaire):
    columnArr = []
    for card in cards:
        cardObj = get_card_value(card)
        columnArr.append(cardObj)
    sortedCol = sorted(columnArr, key=lambda k: k['number'], reverse=True)
    solitaire['stacks'].append(sortedCol)


def addToFountain(cards, solitaire):
    fountainArr = []

    for card in cards:
        cardObj = get_card_value(card)
        fountainArr.append(cardObj)

    if len(fountainArr) > 4:
        print("Error: Too many cards in fountain, 4 < fountain")
        for x in range(0, 4):
            solitaire['fountains'].append({'number': 0, 'suit': x+1})
        return

    sortedFountain = sorted(fountainArr, key=lambda k: k['suit'])
    # print(sortedFountain)

    counter2 = 1
    fountainCounter = 0
    for card in range(0, 4):
        if sortedFountain[fountainCounter]['suit'] == counter2:
            solitaire['fountains'].append(sortedFountain[fountainCounter])
            fountainCounter += 1
        else:
            solitaire['fountains'].append({'number': 0, 'suit': counter2})
        counter2 += 1

img = cv2.imread("oink.png")
s = getCardsFromImage(img)
print(s)

# s = getCardsFromImage("ml_solitaire/yolov5v2/tableau.jpg")
# s2 = getCardsFromImage("ml_solitaire/yolov5v2/fountain2.jpg")
# s3 = getCardsFromImage("ml_solitaire/yolov5v2/waste.jpg")
# addStackToTableau(s, data_solitaire)
# addStackToTableau(s, data_solitaire)
# addToWaste(s3, data_solitaire)
# addToFountain(s2, data_solitaire)

# print(data_solitaire)