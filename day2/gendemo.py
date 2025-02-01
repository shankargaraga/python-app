def sqaure_numbers(nums):
    for i in nums:
        yield(i*i)      #so no return we are returning generator

my_nums=sqaure_numbers([1,2,3,4,5])

print(type(my_nums)) #class generator
print(next(my_nums)) #1
print(next(my_nums)) 