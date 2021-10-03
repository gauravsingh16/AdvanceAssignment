from Factorials import Factorial
from collatz import collatz 
from link import test_link
from randomness import die

print("This is the program from group #16")
flag = 1
while flag == 1:
    print("")
    print("Please select one of the features below, stop by entering Q.")
    print("1. Factorials")
    print("2. Links")
    print("3. Randomness")
    print("4. Collatz")
    inp = input("Enter choice (stop with Q):")
    if inp == '1':
        Factorial()
    elif inp == '2':
        test_link()
    elif inp == '3':
        die()
    elif inp == '4':
        collatz()
    elif (inp == 'Q')or(inp == 'q'):
        flag = 0
    else:
        print("Wrong Input entered!!! Try again....")