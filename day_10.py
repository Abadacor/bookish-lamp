from icecream import ic 
import numpy as np

mapping = {
        ')': '(',
        ']': '[',
        '}': '{',
        '>': '<'
    }

def day_10_input(filename):
    with open(filename) as file_input:
        values = file_input.readlines()
    for i, line in enumerate(values):
        line = line.strip() 
        values[i] = [line[i : i + 1] for i in range(0, len(line))]
    return values

def process_symbols(symbols):
    pile = []
    for symbol in symbols:
        if(symbol not in mapping.keys()):
            pile.append(symbol)
        else:
            if len(pile) == 0:
                return True, symbol
            elif mapping[symbol] == pile[-1]:
                pile.pop()
            else:
                return True, symbol
    return False, pile

def day_10_p1():
    values = day_10_input('day_10_input.txt')
    points = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
        0: 0
    }
    #return sum(points[process_symbols(symbols)] for symbols in values)
    score = 0
    for symbols in values:
        score += process_symbols(symbols)

def scoring(opening_symbols):
    points = {
        '(': 1,
        '[': 2,
        '{': 3,
        '<': 4,
    }
    score = 0 
    for sym in opening_symbols:
        score *= 5
        score += points[sym]
    return score

def day_10_p2():
    values = day_10_input('day_10_input.txt')
    final_score = []
    for symbols in values:
        corr, pile = process_symbols(symbols)
        if not corr:
            pile = pile[::-1]
            final_score.append(scoring(pile))
    return np.median(final_score)
        




ic(day_10_p2())