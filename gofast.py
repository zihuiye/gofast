# go fast
import random

class card:

    cards = ['1♦','1♣','1♥','1♠',
        '2♦','2♣','2♥','2♠',
        '3♦','3♣','3♥','3♠',
        '4♦','4♣','4♥','4♠',
        '5♦','5♣','5♥','5♠',
        '6♦','6♣','6♥','6♠',
        '7♦','7♣','7♥','7♠',
        '8♦','8♣','8♥','8♠',
        '9♦','9♣','9♥','9♠',
        '10♦','10♣','10♥','10♠',
    ]

    def __init__(self, card):

        if type(card) == str and card in self.cards:
            self.card = card
            self.order = self.cards.index(card)
        elif type(card) == int and 0 <= card < len(self.cards):
            self.order = self.cards.index(card)
            self.card = self.cards[card]
        else:
            raise ValueError('not a valid card')

    def __gt__(self, card):
        return self.order > card.order

    def __lt__(self, card):
        return self.order < card.order

    def __repr__(self):
        return self.card

    @classmethod
    def get_cards(self, player_num, each_num):
        if player_num * each_num > len(self.cards):
            raise ValueError('too many')
        cards = self.cards.copy()[:player_num * each_num]
        random.shuffle(cards)
        return [card(i) for i in cards]


class player:

    cards = []
    money = 0
    name = ''
    win = False
    is_snatch = False

    def receive_cards(self, cards):
        self.cards = cards
    
    def clear_cards(self):
        self.cards = []

    def play(self, total_player, remains_numbers, played_cards):
        # 写规则
        if self.win:
            return 'win'
        self.cards.sort()
        # biggest = self.cards.sort()
        pass

if __name__ == '__main__':


    cards = card.get_cards(7,5)
    print(cards)