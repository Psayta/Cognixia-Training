#Fizzbuzz is a code that counts any number divisible by 3 as Fizz, 5 as Buzz, and both as Fizzbuzz

num = int(input("Enter a number: ")) #input number to start Fizzbuzz
fizzbuzz = [] #empty fizzbuzz list
for i in range(1,num): #uses the range based on the number inputted starting at 1 
    if (i % 3 == 0 and i % 5 == 0): fizzbuzz.append("Fizzbuzz") #replaces any number divisible by 3 and 5 with fizzbuzz 
    elif (i % 5 == 0): fizzbuzz.append("Buzz") #replaces any number divisible by 5 with Buzz
    elif (i % 3 == 0): fizzbuzz.append("Fizz") #replaces any number divisible by 3 with Buzz
    else: fizzbuzz.append(i) #adds the number as is if the other if conditions aren't met 
print(fizzbuzz)# prints the list of numbers and Fizzbuzzes 

sum = 0 
for elm in fizzbuzz: #uses list of numbers in fizzbuzzz
    if (isinstance(elm, int)): #if the number is an integer 
        sum += elm #iteratively adds it with itself until it reaches the end of the list 

print("Sum of all integers =", sum) #sums the entirety of fizzbuzz 
print("Sum of Fizz =", fizzbuzz.count('Fizz')) #counts the number of fizz
print("Sum of Buzz =", fizzbuzz.count('Buzz')) #counts the number of buzz 
print("Sum of Fizzbuzz =", fizzbuzz.count('Fizzbuzz')) #counts the number of FizzBuzz
