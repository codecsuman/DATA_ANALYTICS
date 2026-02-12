#parameters and arguments 
def add(x,y):
    #parameters 
    print(x+y)

    #arguments 
add(12,17)


def hello(*name):
    print("hello , my name is ", name[1])
hello("john","pitter")

def hello():
    return("hello")
print(hello())

def add(a,b):
    return (a+b)
print(add(7,8))