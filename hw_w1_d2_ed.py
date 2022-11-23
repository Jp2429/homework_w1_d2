# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:
for num in numbers:
    if num % 2 == 0:
        print(num)

# 2. Print the difference between the largest and smallest value:

largest=max(numbers)
smallest=min(numbers)
difference=largest-smallest
print(difference)

# 3. Print True if the list contains a 2 next to a 2 somewhere.
previous_num=0
for num in numbers:    
    if previous_num == 2 and num ==2:
        print(True)
    previous_num=num


# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22
previous_num=0
total=0
for num in numbers:
    if previous_num == 6 and num!=7:
        print('Number has been excluded')
    elif num==7:
        previous_num=num
    elif num==6:
        previous_num=num
    else:
        total=total+num
        previous_num=num
        
print(total)

# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5.

previous_num=0
total=0
for num in numbers:
    if previous_num == 13:
        print('Number has been excluded')
        previous_num=num
    elif num==13:
        print('Number has been excluded')
        previous_num=num
    else:
        total=total+num
        previous_num=num

print(total)