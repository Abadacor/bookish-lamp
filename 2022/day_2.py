HAND_SIGNS = {
        'A': 'rock', 
        'X': 'rock',
        'B': 'paper', 
        'Y': 'paper',
        'C': 'scissors', 
        'Z': 'scissors'
}

SCORING = {
    '1': 1,
    '0': 2,
    '2': 3
}

EXPECTED_RESULT = {
    'X': 2,
    'Y': 0,
    'Z': 1
}

FUCKIT_TRUTH_TABLE = {
    '0': 2,
    '1': 0,
    '2': 1
}

FUCKOFF_TRUTH_TABLE = {
    '0': 1,
    '1': 2,
    '2': 0
}


def day_2_input(filename):
    with open(filename) as strat_file:
        strat = strat_file.readlines()
    strat = [list(elem.strip().split(' ')) for elem in strat]
    return strat

def convert_input_letters_p1(strat):
    rps = ['paper', 'rock', 'scissors']
    for i, game in enumerate(strat):
        for j, sign in enumerate(game):
            strat[i][j] = rps.index(HAND_SIGNS[strat[i][j]])
    return strat

def compute_game_score(game):
    return SCORING[str(game[1])] + (6 if ((game[0] - game[1] + 3)%3 == 1) else (3 if (game[0] == game[1]) else 0))

def compute_total_score(strat):
    total_score = 0
    for game in strat:
        total_score += compute_game_score(game)
    return total_score

def convert_input_letters_p2(strat):
    rps = ['paper', 'rock', 'scissors']
    for i, game in enumerate(strat):
        strat[i][0] = rps.index(HAND_SIGNS[strat[i][0]])
        if EXPECTED_RESULT[strat[i][1]] == 0:
            strat[i][1] = strat[i][0]
        elif EXPECTED_RESULT[strat[i][1]] == 1:
            strat[i][1] = FUCKIT_TRUTH_TABLE[str(strat[i][0])]     
        else:
            strat[i][1] = FUCKOFF_TRUTH_TABLE[str(strat[i][0])]
    return strat

print(compute_total_score(convert_input_letters_p1(day_2_input('day_2_input.txt'))))
print(compute_total_score(convert_input_letters_p2(day_2_input('day_2_input.txt'))))
