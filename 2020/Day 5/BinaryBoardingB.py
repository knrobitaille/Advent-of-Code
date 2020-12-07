input_file = open('boarding_passes.txt','r')
bp_lines = input_file.read().splitlines()
# print(bp_lines)


mid_row = 64
mid_col = 4

seat_scores = []

for seat in bp_lines:
    row = 0
    col = 0
    for n, x in enumerate(seat):
        if x == 'B':
            row += int(mid_row/(2**n))
        if x == 'R':
            col += int(mid_col/(2**(n-7)))
    ticket_score = row * 8 + col
    seat_scores.append(ticket_score)
    
    
seat_scores = sorted(seat_scores)

for n, seat in enumerate(seat_scores):
    if n+1 == len(seat_scores):
        pass
    else:
        if seat + 1 == seat_scores[n+1]:
            pass
        else:
            print("Your seat score is",seat + 1)


