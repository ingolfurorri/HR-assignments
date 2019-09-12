#Find all numbers i so that 9 < i < 100 so that the sum of individual numbers sqared equals the number it self

for i in range(10, 100):
    
    #Isolate the first and second part of the number, and sum it up in a special variable.

    num1 = i // 10
    num2 = i % 10
    num_sum = num1 + num2

    if(num_sum**2 == i):
        print(i)

#Find all numbers i so that i < 100 and i has exactly 10 divisors

for i in range(100):

    divisor_count = 0

    #With the second for-loop, we check all the numbers from 1 and to i, and count how many are divisors.

    for j in range(1, i+1):
        if(i % j == 0):
            divisor_count += 1
    
    #If the divisor count is exactly 10, we print the number before starting over.

    if(divisor_count == 10):
        print(i)