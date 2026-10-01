
def call(*args):
    print(args)

result1= call("saket","a")


def call_kwargs(**abc):
    print(abc)

result2 = call_kwargs(a=1,b=2,c=3)