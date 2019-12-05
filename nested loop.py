#Nested Loop that goes through a file. 1st loop goes through every line, 2nd goes through every word that is split by , then breaks out of that loop back to the first till executing last line.

def main():
    fileName = input("What file are the numbers in?") #make sure the file is in the same directory as this file.
    infile = open(fileName, 'r')
    sum = 0.0 # must intiate the count at 0 or what ever number you want before the loop
    count = 0 # same as above
    line = infile.readline() #readline is a premade method() infile, refers to the file you had opened
    while line != "": #while line is not blank
        #this is the 1st loop
        for xStr in line.split(","): #2nd loop uses split() at every ","
            sum = sum + eval(xStr) #goes through every xStr, and sums it up, Uses the eval since it would be a string and not a number input
            count = count + 1 # means adds 1 to the count, since it was zero the first loop is 1
        line = infile.readlint()
    print("\nThe average of the number is, ", sum/count)
    
