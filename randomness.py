import random
def die():
    b=0
    n = int(input("Enter a number of dice to throw: "))
    for i in range(n):
        a= random.randint(1,6)
        print("Die {}: {}".format(i+1, a))
        b= b+a
    print("Average: {:.1f}".format(b/n))
