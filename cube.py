#calculate sphereRadius

from math import *



def sphereArea(radius):
    return 4 * pi * radius * radius

def sphereVolume(radius):
    return 4.0/3.0 * pi * radius**3

def main():
    r = float(input("enter in radius of sphere"))
    print("The surface area is %0.2f sqaure units." % (sphereArea(r)))
    print("The volume is %0.2f cubic units." % (sphereVolume(r)))

main()

def main2():
    x = int(input("please put in a number"))
    print(sumN(x))
    
def sumN(x):
    sum = 0
    
    for i in range(x + 1):
        sum = sum + i
        
        return sum

main2()
