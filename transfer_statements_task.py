#problem-1
'''numbers = [25, 30, 20, 40, 15, 25]
total_sum = 0
i = 0  
while True:
    total_sum += numbers[i]
    if total_sum > 100:
        print("Sum exceeded 100")
        break
    i += 1

#print odd numbers using continue in for loop
for num in range(1, 601):
    if num % 2 == 0:  
        continue  # Skip the rest of the loop for even numbers
    print(num)

#checking even or odd using pass
num_1 = int(input("Enter the number to check "))
if num_1%2 == 0:
    print(f"{num_1} is even")
    pass'''

given_list = input("Enter the words : ").split()
for word in given_list:
    if word == "break":
        break
    elif word == "skip":
        continue
    else:
        print(f"{word}")