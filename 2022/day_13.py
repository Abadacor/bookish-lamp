def day_13_input(filename):
    with open(filename,'r') as f:
        data = [row.split('\n') for row in f.read().strip().split('\n\n')]
    
    pairs = [(eval(a),eval(b)) for a,b in data]
    bigdata = [eval(x) for x in sum(data, [])] + [[[2]]] + [[[6]]]
    return pairs, bigdata

def compare_pair(left, right):
    n = max(len(left), len(right))

    for i in range(n):
        if i >= len(left): return True
        if i >= len(right): return False
        left_value, right_value = left[i], right[i]
        left_type, right_type = type(left_value), type(right_value)

        if left_type is int and right_type is int:
            if left_value < right_value: return True
            elif left_value > right_value: return False
        else:
            if left_type is int: left_value = [left_value]
            if right_type is int: right_value = [right_value]
            res = compare_pair(left_value, right_value)
            if res is not None: return res

def bubble_sort(big_list):
    for i in range(len(big_list)-1):
        for j in range(0, len(big_list)-i-1):
            if compare_pair(big_list[j + 1], big_list[j]): 
                big_list[j], big_list[j + 1] = big_list[j + 1], big_list[j]
    return big_list

def compute_decoder_key(bigdata):
    bigdata = bubble_sort(bigdata)
    for i, elem in enumerate(bigdata):
        if elem == [[2]]: x = i+1
        if elem == [[6]]: y = i+1
    return x*y

data, bigdata = day_13_input('C:\\Users\\romai\\Documents\\GitHub\\bookish-lamp\\2022\\day_13_input.txt')
part1 = sum([i+1 for i, (left,right) in enumerate(data) if compare_pair(left,right)])
part2 = compute_decoder_key(bigdata)

print(part1)
print(part2)