def day_6_input(filename):
    with open(filename) as f:
        datastream_buffer = f.readline()
    return datastream_buffer

def find_first_n_unique_chars(data, n):
    buffer = []
    for i, char in enumerate(data):
        if(len(buffer) < n):
            buffer.append(char)
        if(len(buffer) == n):
            if(len(list(set(buffer))) == n):
                return i + 1
            else:
                buffer.pop(0)


datastream_buffer = day_6_input('/home/romain/Documents/advent_of_code/2022/day_6_input.txt')
print(find_first_n_unique_chars(datastream_buffer, 4))
print(find_first_n_unique_chars(datastream_buffer, 14))

