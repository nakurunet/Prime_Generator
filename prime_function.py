def prime_num(number):
    if isinstance(number,float):
        print "The number must be a whole number"
    if isinstance(number, str):
        print "Cannot allow letters"
    if isinstance(number, list):
        print "The input must not be a list"
    if isinstance(number,tuple):
        print "The input must not be a tuple"
    if (number>1000):
        print "large numbers not allowed!!!"
    if isinstance(number,bool):
        print "The number must not be a boolean"

#Starting from 2 since 2 is a prime number
    for x in range(2,number+1):
        prime = True #initialize prime as true
        for i in range(2,x):
            if (x%i==0): #check if it is divisible 
                prime = False #it is not a prime number
        if prime:
           print x, #print prime numbers on a line

#TESTING THE FUNCTION WITH ANY RANDOM NUMBER
prime_num(423)
