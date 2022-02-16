from icecream import ic 

def day_21_input(filename):
    with open(filename) as file_input:
        values = [int(x.split()[-1]) for x in file_input.read().splitlines()]
    return values

def day_21_p1():
    values = day_21_input('day_21_input.txt')
    players = {e : [x, 0] for e,x in enumerate(values)}
    dice, rolls, e = 0, 0, 0
    while not any(x[1] >= 1000 for x in players.values()):
        turn = 0
        for i in range(3):
            dice = (dice + 1) % 100
            turn += dice
            rolls += 1
        next_field = (players[e % 2][0] + turn - 1) % 10 + 1
        players[e % 2][0] = next_field
        players[e % 2][1] += next_field
        e += 1
    return min(x[1] for x in players.values()) * rolls

def wtf_dice(current_player, other_player, current_score = 0, other_score = 0):
    odds_of_rolling_results = ((3,1), (4,3), (5,6), (6,7), (7,6), (8,3), (9,1))
    if other_score >= 21:
        return 0, 1
    wins_current, wins_other = 0, 0
    for turn, times in odds_of_rolling_results: 
        current_position = (current_player + turn - 1) % 10 + 1
        loss, win = wtf_dice(other_player, current_position, other_score, current_score + current_position)
        wins_current = wins_current + times * win
        wins_other = wins_other + times * loss
    return wins_current, wins_other

def day_21_p2():
    values = day_21_input('day_21_input.txt')
    return max(wtf_dice(*values))

ic(day_21_p1())
ic(day_21_p2())