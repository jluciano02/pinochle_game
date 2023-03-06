from card import Card
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


def count_meld(hand, trump_suit):

    hand_strings = [f"{card.value}_{card.suit}" for card in hand] # A bit easier to work with for this particular purpose
    
    # Count runs
    runs = 0

    if (hand_strings.count(f"a_{trump_suit}") == 2 and hand_strings.count(f"10_{trump_suit}") == 2 and hand_strings.count(f"k_{trump_suit}") == 2 and hand_strings.count(f"q_{trump_suit}") == 2 and hand_strings.count(f"j_{trump_suit}") == 2):
        runs = 2
    elif (hand_strings.count(f"a_{trump_suit}") >= 1 and hand_strings.count(f"10_{trump_suit}") >= 1 and hand_strings.count(f"k_{trump_suit}") >= 1 and hand_strings.count(f"q_{trump_suit}") >= 1 and hand_strings.count(f"j_{trump_suit}") >= 1):
        runs = 1
    
    # Count aces, kings, queens, jacks around (one of every suit = one around)
    around = {}

    for card in ["a", "k", "q", "j"]:
        if (hand_strings.count(f"{card}_spade") == 2 and hand_strings.count(f"{card}_heart") == 2 and hand_strings.count(f"{card}_club") == 2 and hand_strings.count(f"{card}_diamond") == 2):
            around[card] = 2
        elif (hand_strings.count(f"{card}_spade") >= 1 and hand_strings.count(f"{card}_heart") >= 1 and hand_strings.count(f"{card}_club") >= 1 and hand_strings.count(f"{card}_diamond") >= 1):
            around[card] = 1
    
    # Counting Marriages
    marriages = 0
    marriages_trump = 0

    for suit in ["spade", "heart", "club", "diamond"]:
        if(hand_strings.count(f"k_{suit}") == 2 and hand_strings.count(f"q_{suit}") == 2):
            if(suit == trump_suit):
                marriages_trump += 2 - runs
            else:
                marriages += 2
        elif(hand_strings.count(f"k_{suit}") >= 1 and hand_strings.count(f"q_{suit}") >= 1):
            if(suit == trump_suit):
                marriages_trump += 1 - runs
            else:
                marriages += 1
    
    # Counting Pinochles
    pinochles = 0
    
    if(hand_strings.count("j_diamond") == 2 and hand_strings.count("q_spade") == 2):
        pinochles = 2
    elif(hand_strings.count("j_diamond") >= 1 and hand_strings.count("q_spade") >= 1):
        pinochles = 1

    # Counting 9s of trump
    trump_9 = hand_strings.count(f"9_{trump_suit}")

    total = 0

    for card in around:
        match card:
            case "a":
                total += around["a"] * 10
            case "k":
                total += around["k"] * 8
            case "q":
                total += around["q"] * 6
            case "j":
                total += around["j"] * 4

    ######## For debugging purposes ########
    # arounds = ""
    # for card in around:
    #     match card:
    #         case "a":
    #             print("Aces Around: ", around["a"])
    #         case "k":
    #             print("Kings Around: ", around["k"])
    #         case "q":
    #             print("Queens Around: ", around["q"])
    #         case "j":
    #             print("Jacks Around: ", around["j"])
    
    # print("Runs: ", runs, "\n",
    #       "Pinochles: ", pinochles, "\n",
    #       "Trump Marriages: ", marriages_trump, "\n",
    #       "Marriages: ", marriages, "\n",
    #       "9s of Trump: ", trump_9, "\n"
    #       )
    ######## For debugging purposes ########

    # Total meld
    total += (runs * 15) + (pinochles * 4) + (marriages_trump * 4) + (marriages * 2) + trump_9

    return total

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
    print(count_meld(player1, "spade"))
    display_hand(player2)
    print(count_meld(player2, "spade"))
    display_hand(player3)
    print(count_meld(player3, "spade"))
    display_hand(kitty)


main()