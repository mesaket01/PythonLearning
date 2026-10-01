def print_result_decorator(func):
    def wrapper(*args):
        print(args)
        result = func(*args)
        return result
    return wrapper

def greatest_first_decorator(func):
    def wrapper(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)
    return wrapper

# @print_result_decorator
@greatest_first_decorator
def div(a,b):
    return a/b

# @print_result_decorator
@greatest_first_decorator
def sub(a,b):
    return a-b

@print_result_decorator
def add(a,b,c):
    return a+b+c
result1 = div(2,4)
print(result1)

result2 = sub(2,8)
print(result2)

result3 = add(2,8, 16)
print(result3)