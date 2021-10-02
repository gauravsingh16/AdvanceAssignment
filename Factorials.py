def fact_of_number(n):
    fact = 1
    for index in range(1,n+1):
        fact = fact * index
    print(n,"! = ",fact)


def Factorial():
    num = int(input("Enter a number: "))
    print()
    for i in range(1,num+1):
        fact_of_number(i)
