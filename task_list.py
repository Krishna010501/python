#Reverse list
'''my_list = [10,20,30,40,50,11]
reverse_list = my_list[::-1]
print(reverse_list)

#Common elements
list1 = [1,2,3,4,5]
list2 = [4,5,6,7,8]
common_elements = []
for item in list1:
    if item in list2:
        common_elements.append(item)
print(common_elements)

#Unique elements
original_list = [1,2,2,3,4,4,5]
unique_list = list(set(original_list))
print(unique_list)

#Remove duplicates
duplicated_list = [1,2,2,3,4,4,5]
unique_list = []
for item in duplicated_list:
    if item not in unique_list:
        unique_list.append(item)
print(unique_list)

#List concatenation
list_1 = ["krishna"]
list_2 = ["inturi"]
list_conc = list_1 + list_2
print(list_conc)

#list repetition
list_1 = [3,5,"krishna",["inturi"]]
repeat_list = list_1 * 3
print(repeat_list)'''

#list removal
list_11 = [8,19,"krishna","gayathri",["inturi"]]
list_rem = list_11.remove(8)
print(list_rem)