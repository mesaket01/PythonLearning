inp = "madama"

def palindrome(inp_str):
    left = 0
    right = len(inp_str)-1
    while left < right:
        if inp[left] != inp[right]:
            return False
        left += 1
        right -= 1
        return True

print(palindrome(inp))
