from __future__ import print_function
def trianglenum(row):
    if row < 0:
        print("invalid input")
    else:
        num = 1
        for i in range(row):
            for j in range(i+1):
                print(num, end=" ")
                num = num+1
            print("")