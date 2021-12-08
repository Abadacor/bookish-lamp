from icecream import ic

def day_8_input(filename):
    with open(filename) as file_input:
        values = file_input.readlines()
    values = [[[segment.strip('\n') for segment in v.split(' ')] for v in val.split(' | ')] for val in values]
    return values

def deduce_mapping(signal):
    mapping = ['' for i in range(10)]
    for segment in signal:
        if len(segment) == 2: 
            mapping[1] = segment
        elif len(segment) == 3: 
            mapping[7] = segment
        elif len(segment) == 4: 
            mapping[4] = segment
        elif len(segment) == 5:
            if all([c in segment for c in mapping[1]]): 
                mapping[3] = segment
            elif sum([c in segment for c in mapping[4]]) == 3: 
                mapping[5] = segment
            else: 
                mapping[2] = segment
        elif len(segment) == 6:
            if all([c in segment for c in mapping[4]]): 
                mapping[9] = segment
            elif all([c in segment for c in mapping[7]]): 
                mapping[0] = segment
            else: 
                mapping[6] = segment
        else: 
            mapping[8] = segment

    return mapping


def day_8_p1():
    values = day_8_input('day_8_input.txt')
    count = 0 
    for k, val in enumerate(values):
        for i, segments in enumerate(val):
            if(i == 1):
                for j, segment in enumerate(segments):
                    if len(segment) == 2: 
                        count += 1
                        values[k][i][j] = 2
                    if len(segment) == 3:
                        count += 1
                        values[k][i][j] = 3
                    if len(segment) == 4:
                        count += 1
                        values[k][i][j] = 4
                    if len(segment) == 7:
                        count += 1
                        values[k][i][j] = 7
    return values, count

def day_8_p2():
    values = day_8_input('day_8_input.txt')
    final_sum = 0

    for i, val in enumerate(values):
        for j, segments in enumerate(val):
            if(j == 0):
                signal = sorted(segments, key=len)
                mapping = deduce_mapping(signal)
            if(j == 1):
                addup = 0
                for k, segment in enumerate(segments):
                    for l in range(10):
                        if all([c in segment for c in mapping[l]]) and len(mapping[l]) == len(segment):
                            segments[k] = l
                addup += int("".join(map(str,segments))) 
        final_sum += addup       
    return final_sum


ic(day_8_p2())