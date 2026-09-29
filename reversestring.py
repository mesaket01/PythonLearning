inp_str = "hello world"
print(inp_str[::-1])

def reverse(inp_str):
    return inp_str[::-1]
print(reverse(inp_str))
def reverse1(inp_str):
    rev = ""
    for char in inp_str:
        rev = rev + char
print(reverse(inp_str))
