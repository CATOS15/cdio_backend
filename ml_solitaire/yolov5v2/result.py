import cv2
import json
import torch
import image_processing.objects as obj
import image_processing.g_img as g_img

model = torch.hub.load('ultralytics/yolov5', 'custom', path='ml_solitaire/yolov5v2/cardrecognizer.pt')

model.conf = 0.7
waste = 'waste'
tableau = 'tableau'
foundation = 'fountains'

data_solitaire = {
    tableau: [
    ],
    foundation: [
    ],
    waste: [
    ],
}


def map_img_cards(path):
    results = model(path)
    resultsPanda = results.pandas().xyxy[0].to_json(orient="records")
    resultsJSON = json.loads(resultsPanda)

    pobjs = []
    for result in resultsJSON:
        json_card = result["name"]
        conf = result["confidence"]
        rank_suit = get_card_value(json_card)
        card = obj.Card(g_img.Suits(rank_suit['suit']), g_img.Ranks(rank_suit['number']), conf, conf)
        pobjs.append(card)
    return pobjs



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
        return g_img.Suits.DIAMOND.value
    elif s == 'h':
        return g_img.Suits.HEART.value
    elif s == 's': #c for clubs
        return g_img.Suits.SPADE.value
    else:
        return g_img.Suits.CLUB.value


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