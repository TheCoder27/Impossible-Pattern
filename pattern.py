# Rule 1: if even - n/2
# Rule 2: if odd - (n * 3) + 1

import time

steps = 0
n = -1
originalN = 0

def pattern():
    global n, originalN, steps

    if(n != -1):
        print(n)
        while(n != 1):

            if(n % 2 == 0):
                n = n/2
            elif(n % 2 != 0):
                n = (n*3) + 1

            print(n)
            time.sleep(0.01)
            steps += 1
        print(f"It took {steps} steps to get to 1 from {originalN}")
    else:
        try:
            n = int(input("Type a positive integer: "))
            originalN = n
            pattern()
        except(ValueError):
            pattern()

pattern()

