input_file = open('input.txt','r')
input_lines = input_file.read().splitlines()
# print(input_lines)
# print(len(input_lines))

p1_deck = []
p2_deck = []

switch = False
for line in input_lines:
    # print(line)
    if "Player" in line:
        continue
    if line == "":
        # print("Switch")
        switch = True
        continue
    if switch:
        p2_deck.append(int(line))
    else:
        p1_deck.append(int(line))
        
# print("P1 Deck",p1_deck)
# print("P2 Deck",p2_deck)

def recursive_combat(p1_deck,p2_deck):
    finished = False
    previous_hands = []
    round = 1
    while not finished:
        if (p1_deck,p2_deck) in previous_hands:
            finished = True
            # print((p1_deck,p2_deck),"found in previous hand.")
            # print((p1_deck,p2_deck),previous_hands)
            winner = 1
            winning_deck = p1_deck
            return winner,winning_deck
        previous_hands.append((p1_deck,p2_deck))
        # print("-- Round",round,"--")
        # print("P1 Deck",p1_deck)
        # print("P2 Deck",p2_deck)
        
        p1_card = p1_deck[0]
        p1_deck = p1_deck[1:]
        # print("Player 1 plays",p1_card)
        p2_card = p2_deck[0]
        p2_deck = p2_deck[1:]
        # print("Player 2 plays",p2_card)
        
        if p1_card <= len(p1_deck) and p2_card <= len(p2_deck):
            # print()
            # print("Recursive combat!")
            p1_recurse_deck = p1_deck.copy()[:p1_card]
            p2_recurse_deck = p2_deck.copy()[:p2_card]
            winner,winning_deck = recursive_combat(p1_recurse_deck,p2_recurse_deck)
        elif p1_card > p2_card:
            winner = 1
        elif p2_card > p1_card:
            winner = 2
        
        if winner == 1:
            # print("Players 1 wins the round!")
            p1_deck.extend([p1_card,p2_card])
        elif winner == 2:
            # print("Players 2 wins the round!")
            p2_deck.extend([p2_card,p1_card])
        
        if len(p1_deck) == 0 or len(p2_deck) == 0:
            finished = True
            if len(p1_deck) > len(p2_deck):
                winner = 1
                winning_deck = p1_deck
            else:
                winner = 2
                winning_deck = p2_deck
            # print()
            # print("Player",winner,"has won the game!")
            return winner,winning_deck
        else:
            round += 1
            
# This may take a minute to run
winner,winning_deck = recursive_combat(p1_deck,p2_deck)

print()
print("== Post-game results ==")
print("P1 Deck",p1_deck)
print("P2 Deck",p2_deck)  
print()

score = 0
for n, i in enumerate(reversed(winning_deck)):
    score += (n+1)*i
print("Winning score is",score)