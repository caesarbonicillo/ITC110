def main():
    print ("this is a chaos function") 
    x = eval (input ("enter a number between 0 and 1"))
    n = eval (input ("how many times should I print?"))

    for i in range (n):
        x = 3.9 * x * (1 -x)
        print ("Times printed", i+1, ":", x)

main()



