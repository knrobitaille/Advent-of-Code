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

finished = False

round = 1
while not finished:
    p1_deck_copy = p1_deck.copy()
    p2_deck_copy = p2_deck.copy()
    
    # print("-- Round",round,"--")
    
    p1_card = p1_deck_copy[0]
    p1_deck = p1_deck[1:]
    # print("Player 1 plays",p1_card)
    
    p2_card = p2_deck_copy[0]
    p2_deck = p2_deck[1:]
    # print("Player 2 plays",p2_card)
    
    if p1_card > p2_card:
        # print("Players 1 wins the round!")
        p1_deck.extend([p1_card,p2_card])
    elif p2_card > p1_card:
        # print("Players 2 wins the round!")
        p2_deck.extend([p2_card,p1_card])
        
    else:
        pass
        # print("Tie")
    
    
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
    else:
        round += 1
    # print()

print()
print("== Post-game results ==")
print("P1 Deck",p1_deck)
print("P2 Deck",p2_deck)  
print()



score = 0
for n, i in enumerate(reversed(winning_deck)):
    score += (n+1)*i
print("Winning score is",score)