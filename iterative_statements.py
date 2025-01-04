#sum of squares of 1 to 5
sum = 0
for i in range(1,6):
    result = i**2
    sum+=result
print(f"The sum of squares is {sum}")

# #countdown from 5 to 1
count = 5
while count > 0:
    print(count)  
    count -= 1

# #multiplication table
user_num = int(input("Enter the number you want "))
for i in range(1,11):
    print(f"{user_num} x {i} = {user_num*i} ")

#sum of even numbers sum from 1 to 10
sum = 0
for i in range(2,11):
    if i%2==0:
        sum+=i
print(sum)

#sum of all numbers from 1 to given number
sum = 0
num = int(input("Enter the digit upto ?"))
for i in range(1,num+1):
    sum+= i
print(sum)

#prime numbers
num_1 = int(input("Enter the first number : "))
num_2 = int(input("Enter the number upto range : "))
for num in range(num_1,num_2 + 1):
    if num > 1: 
        for i in range(2, num):
            if num % i == 0:  
                break
        else:
            print(num)