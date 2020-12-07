input_file = open('boarding_passes.txt','r')
bp_lines = input_file.read().splitlines()
# print(bp_lines)


mid_row = 64
mid_col = 4

max_seat = 0

for seat in bp_lines:
    row = 0
    col = 0
    for n, x in enumerate(seat):
        if x == 'B':
            row += int(mid_row/(2**n))
        if x == 'R':
            col += int(mid_col/(2**(n-7)))
            
    ticket_score = row * 8 + col
    if ticket_score > max_seat:
        max_seat = ticket_score
            
print("Highest seat score is",max_seat)

