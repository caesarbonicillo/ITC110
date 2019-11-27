def main():
   n = int(input("how many numbers are there?"))

   #set Max to the first number
   max = eval(input("enter a number >>"))

   #now put in a loop and the previous one will knock it out if lesser.
   for i in range(n-1):
       x = float(input("Enter a number >>"))
       if x > max:
           max = x
   print("the largest number is", max)
main()

