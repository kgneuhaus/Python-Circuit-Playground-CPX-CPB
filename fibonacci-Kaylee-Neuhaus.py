import random

my_fibonacci = []

print("Enter the first number of your fibonacci sequence:")

try:
    fib_int1 = int(input())
    
    if 0 <= fib_int1 <= 9:
        print("The first number in your fibonacci sequence is ", fib_int1)
        
        list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        fib_int2 = int(random.choice(list1))
        print("The second number in your finonacci squence has been randomly selected to be ", fib_int2)

        my_fibonacci.append(fib_int1)
        print(my_fibonacci)
        my_fibonacci.append(fib_int2)
        print(my_fibonacci)

        for x in range (10):
            
            new_fib = fib_int1 + fib_int2
            my_fibonacci.append(new_fib)
            print(my_fibonacci)
            fib_int1 = fib_int2
            fib_int2 = new_fib
            
        print(my_fibonacci)
        print("Done!!")
        
    else:
        print("enter a differnet number")
    
except:
    print("enter a number, not a word")
