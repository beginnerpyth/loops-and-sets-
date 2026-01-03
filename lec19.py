#num4 = 10
#def addition(x,y=0,z=1):
# addition(2)




z = 30
def b():
    global z
    z = z + 5
    print("inside function",z)
    b()
    print("outside functions",z)


def b(*varj):#tuples jasari kaam garxa
    print(varj)
    b(1,5,7,8,97,8,7)
def c(**kaks):
    print(kaks)
    c(name="man",age=12)

def fact(n):
    if n == 0 or n == 1:
        return 1
    return n*