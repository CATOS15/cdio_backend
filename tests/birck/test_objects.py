class ContourMatch():
    def __init__(self, name, ground_truth):
        self.name = name
        self.ground_truth = ground_truth
        self.match_deck = -1
        self.match_card = -1

    def find_best_result(self, result, is_deck):
        if is_deck:
            if self.match_deck == -1 or self.match_deck > result:
                self.match_deck = result
        else:
            if self.match_card == -1 or self.match_card > result:
                self.match_card = result


    def __str__(self):
        return "name: " + self.name + "\tmatch_deck:" + str(self.match_deck) + "\tmatch_card: " + str(self.match_card)
