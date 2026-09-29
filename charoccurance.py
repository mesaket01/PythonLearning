inp_str = "Hello World"

def char_occur(inp_str):
    freq_char = {}
    for char in inp_str:
        if char not in freq_char:
            freq_char[char] = 1
            continue
        else:
            freq_char[char] += 1
    return freq_char
print(char_occur(inp_str))

def char_count(inp_str):
    freq_char = {}
    for char in inp_str:
        freq_char[char] = freq_char.get(char, 0)+1
    return freq_char
print(char_count(inp_str))
