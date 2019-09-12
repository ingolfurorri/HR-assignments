num = int(input("Enter an integer: "))

#Initializing all the variables we need to use

sum_num = 0
max_num = 0
odd = 0
even = 0

#If the initial input is not > 0, the code will not run

if not (num <= 0):

    while(num > 0):
        sum_num += num

        if(num % 2 == 0):
            even += 1

        else:
            odd += 1

        #If the input is the highest yet, we save it as the new high

        if(num > max_num):
            max_num = num

        print(f"Cumulative total: {sum_num}")

        num = int(input("Enter an integer: "))

    #Soon as the while loop becomes false (input <= 0) we go into the else loop 

    else:
        print(f"Largest number: {max_num}")
        print(f"Count of even numbers: {even}")
        print(f"Count of odd numbers: {odd}")
