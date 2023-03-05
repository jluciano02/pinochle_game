class Card:

    value = ""
    suit = ""
    priority = 0
    isTrump = False

    def determine_priority(self, value, suit):
        priority = 0
        match suit:
            case "diamond":
                priority += 0
            case "club":
                priority += 6
            case "heart":
                priority += 12
            case "spade":
                priority += 18

        match value:
            case "a":
                priority += 5
            case "10":
                priority += 4
            case "k":
                priority += 3
            case "q":
                priority += 2
            case "j":
                priority += 1
            case "9":
                priority += 0

        return priority

    def __init__(self, value, suit, priority = 0, isTrump = False):
        self.value = value 
        self.suit = suit
        self.priority = self.determine_priority(value, suit)

    def display(self):
        match self.suit:
            case "heart":
                    print(self.value + "♥", end = " ")
            case "diamond":
                    print(self.value + "♦", end = " ")
            case "club":
                    print(self.value + "♣", end = " ")
            case "spade":
                    print(self.value + "♠", end = " ")
