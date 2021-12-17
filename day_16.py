from icecream import ic 
import math

SUM_VERSION = 0

def day_16_input(filename):
    packet = open('day_16_input.txt').read().splitlines()[0]
    bin_packet = ''.join(format(int(char, base=16), '#06b')[2:] for char in packet)
            
    return bin_packet

def product(values):
    prod = 1
    for value in values:
        prod *= value
    return prod

def gt(values):
    return int(values[0] > values[1])

def lt(values):
    return int(values[0] < values[1])

def equals(values):
    return int(values[0] == values[1])

def parse_literals(binary):
    i = 6
    total = ''
    while True:
        total += binary[i + 1:i + 5]
        if binary[i] == '0':
            return i + 5, int(total, 2)
        i += 5
    
def parse_operation(binary, operation):
    values = []
    if binary[6] == '1':
        i = 18
        for _ in range(int(binary[7:18], 2)):
            j, value = parse_packet(binary[i:])
            i += j
            values.append(value)
    elif binary[6] == '0':
        i = 22
        while i < 22 + int(binary[7:22], 2):
            j, value = parse_packet(binary[i:])
            i += j
            values.append(value)
    return i, operation(values)

def process_header(binary):
    return int(binary[0:3], 2), int(binary[3:6], 2)

def parse_packet(binary):
    version, id = process_header(binary)
    global SUM_VERSION
    SUM_VERSION += version
    if id == 4:
        return parse_literals(binary)
    else:
        operations = {0: sum, 1: product, 2: min, 3: max, 5: gt, 6: lt, 7: equals}
        return parse_operation(binary, operations[id])


def day_16_p2():
    packet = day_16_input('day_16_example.txt')
    global SUM_VERSION
    SUM_VERSION = 0
    return parse_packet(packet)[-1]

ic(day_16_p2())
ic(SUM_VERSION)
