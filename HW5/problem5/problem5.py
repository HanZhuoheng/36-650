from __future__ import print_function
def trianglestar(row):
    if row < 0:
        print("invalid input")
    else:
        num = row-1
        for i in range(row):
            for j in range(num):
                print(end=" ")
            num = num-1
            for j in range(i+1):
                print("*", end=" ")
            print("")