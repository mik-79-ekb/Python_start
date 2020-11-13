"""
Task 3.3
"""
def my_func (*args):
        return sum(args) - min(args)
print(my_func(7, 2, 6))