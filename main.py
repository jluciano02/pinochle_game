from pinochle_game.card import Card
import random

def generateDeck():
    ret = []

    ret.append(Card("a", "spade"))
    ret.append(Card("a", "spade"))
    ret.append(Card("10", "spade"))
    ret.append(Card("10", "spade"))
    ret.append(Card("k", "spade"))
    ret.append(Card("k", "spade"))
    ret.append(Card("q", "spade"))
    ret.append(Card("q", "spade"))
    ret.append(Card("j", "spade"))
    ret.append(Card("j", "spade"))
    ret.append(Card("9", "spade"))
    ret.append(Card("9", "spade"))
    ret.append(Card("a", "heart"))
    ret.append(Card("a", "heart"))
    ret.append(Card("10", "heart"))
    ret.append(Card("10", "heart"))
    ret.append(Card("k", "heart"))
    ret.append(Card("k", "heart"))
    ret.append(Card("q", "heart"))
    ret.append(Card("q", "heart"))
    ret.append(Card("j", "heart"))
    ret.append(Card("j", "heart"))
    ret.append(Card("9", "heart"))
    ret.append(Card("9", "heart"))
    ret.append(Card("a", "club"))
    ret.append(Card("a", "club"))
    ret.append(Card("10", "club"))
    ret.append(Card("10", "club"))
    ret.append(Card("k", "club"))
    ret.append(Card("k", "club"))
    ret.append(Card("q", "club"))
    ret.append(Card("q", "club"))
    ret.append(Card("j", "club"))
    ret.append(Card("j", "club"))
    ret.append(Card("9", "club"))
    ret.append(Card("9", "club"))
    ret.append(Card("a", "diamond"))
    ret.append(Card("a", "diamond"))
    ret.append(Card("10", "diamond"))
    ret.append(Card("10", "diamond"))
    ret.append(Card("k", "diamond"))
    ret.append(Card("k", "diamond"))
    ret.append(Card("q", "diamond"))
    ret.append(Card("q", "diamond"))
    ret.append(Card("j", "diamond"))
    ret.append(Card("j", "diamond"))
    ret.append(Card("9", "diamond"))
    ret.append(Card("9", "diamond"))
    
    return ret
    

def display_hand(hand):
    
    for card in hand:
        card.display()
    
    print("\n")

def organize_cards(hand): #Bubble-sort Algorithm

    length = len(hand)
    for i in range(length):
        # Last i elements are already sorted
        for j in range(0, length-i-1):
            # Traverse the list from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if (hand[j].priority > hand[j+1].priority):
                hand[j], hand[j+1] = hand[j+1], hand[j]
    
    hand.reverse() #Just to have spades first instead of diamonds first, personal preference on my end


def count_meld(hand):
    runs = 0
    
    #Count number of runs

    face_values = ["a", "k", "q", "j"]
    suits = ["spade", "heart", "club", "diamond"]

    # initialize counters
    aces_around = 0
    kings_around = 0
    queens_around = 0
    jacks_around = 0

    hand_strings = [] # to make this easier

    for card in hand:
        hand_strings.append(f"{card.value}_{card.suit}")

    if(hand_strings.count("a_spade") == 2 and hand_strings.count("a_heart") == 2 and hand_strings.count("a_club") == 2 and hand_strings.count("a_diamond") == 2):
        aces_around = 2
    if(hand_strings.count("a_spade") >= 1 and hand_strings.count("a_heart") >= 1 and hand_strings.count("a_club") >= 1 and hand_strings.count("a_diamond") >= 1):
        aces_around = 1
    if(hand_strings.count("k_spade") == 2 and hand_strings.count("k_heart") == 2 and hand_strings.count("k_club") == 2 and hand_strings.count("k_diamond") == 2):
        kings_around = 2
    if(hand_strings.count("k_spade") >= 1 and hand_strings.count("k_heart") >= 1 and hand_strings.count("k_club") >= 1 and hand_strings.count("k_diamond") >= 1):
        kings_around = 1
    if(hand_strings.count("q_spade") == 2 and hand_strings.count("q_heart") == 2 and hand_strings.count("q_club") == 2 and hand_strings.count("q_diamond") == 2):
        queens_around = 2
    if(hand_strings.count("q_spade") >= 1 and hand_strings.count("q_heart") >= 1 and hand_strings.count("q_club") >= 1 and hand_strings.count("q_diamond") >= 1):
        queens_around = 1
    if(hand_strings.count("j_spade") == 2 and hand_strings.count("j_heart") == 2 and hand_strings.count("j_club") == 2 and hand_strings.count("j_diamond") == 2):
        jacks_around = 2
    if(hand_strings.count("j_spade") >= 1 and hand_strings.count("j_heart") >= 1 and hand_strings.count("j_club") >= 1 and hand_strings.count("j_diamond") >= 1):
        jacks_around = 1

    print(hand_strings)

    print("Jacks: ", jacks_around, " Queens: ", queens_around, " Kings: ", kings_around, " Aces: ", aces_around)
    
    pinochles = 0
    marriages_trump = 0
    marriages = 0
    trump_9 = 0


def main():

    deck = generateDeck()

    random.shuffle(deck)

    player1 = deck[0:15]
    player2 = deck[15:30]
    player3 = deck[30:45]
    kitty = deck[45:48]

    organize_cards(player1)
    organize_cards(player2)
    organize_cards(player3)
    display_hand(player1)
    display_hand(player2)
    display_hand(player3)
    display_hand(kitty)


#main()

test_hand = []
test_hand.append(Card("a", "spade"))
test_hand.append(Card("a", "heart"))
test_hand.append(Card("a", "diamond"))
test_hand.append(Card("a", "club"))
test_hand.append(Card("a", "club"))
test_hand.append(Card("a", "diamond"))
test_hand.append(Card("a", "heart"))
test_hand.append(Card("a", "spade"))
count_meld(test_hand)