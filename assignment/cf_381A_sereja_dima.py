def game(cards):
    i = 0
    j = len(cards) - 1
    s = 0
    d = 0
    turn = 0 # 0 for sereja, 1 for dima
    while i<=j:
        if cards[i] > cards[j]:
            c = cards[i]
            i += 1
        else:
            c = cards[j]
            j -= 1
        if turn == 0:
            s += c
        else:
            d += c
        turn = 1 - turn
    print(s,d)
            
            
    



n = int(input())
cards = [0]*n
for i in range(n):
    cards[i] = int(input())
game(cards)

