from icecream import ic 
from collections import Counter
import math

def day_14_input(filename):
    with open(filename) as file:
        polymer, rules = file.read().split("\n\n")
        rules = {a:b for a, b in [rule.split(' -> ') for rule in rules.splitlines()]}
        
    return polymer, rules

def step(polymer, rules):
    inserts = []
    for rule in rules:
        if rule[0] in polymer:
            inserts += [(rule[1], i+1) for i in range(len(polymer)) if polymer.startswith(rule[0], i)]
    inserts.sort(key=lambda a: a[1], reverse=True)
    for elem in inserts:
        polymer = polymer[:elem[1]] + elem[0] + polymer[elem[1]:]
    return polymer

def day_14_p1():
    polymer, rules = day_14_input('day_14_example.txt')
    step(polymer, rules)
    for _ in range(10):
        polymer = step(polymer, rules)
    res = Counter(polymer)
    return res[max(res, key = res.get)] - res[min(res, key = res.get)]

def step_p2(pairs, rules):
    buff_pairs = {i:0 for i in [pair for pair in rules.keys()]}
    for elem in pairs:
        if pairs[elem] > 0 and elem in rules.keys():
            buff_pairs[str(elem[0]+rules[elem])] += pairs[elem]
            buff_pairs[str(rules[elem]+elem[1])] += pairs[elem]
    return buff_pairs

def day_14_p2():
    polymer, rules = day_14_input('day_14_input.txt')
    ic(polymer, len(rules))
    pairs = {i:0 for i in [pair for pair in rules.keys()]}
    for rule in rules:
         if rule in polymer:
             pairs[rule] += polymer.count(rule)
    for _ in range(40):
        pairs = step_p2(pairs, rules)
    
    letters = {}
    for elem in pairs:
        if elem[0] in letters.keys():
            letters[elem[0]] += pairs[elem]
        else:
            letters[elem[0]] = pairs[elem]
    letters[polymer[len(polymer)-1]] += 1
    
    return max(letters.values()) - min(letters.values())

#ic(day_14_p1())
ic(day_14_p2())