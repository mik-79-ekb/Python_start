"""
Task 4.2
"""
my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [my_list[x] for x in range(1, len(my_list)) if my_list[x]>my_list[x-1]]
print(new_list)

