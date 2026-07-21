
'''
     What is sorted() in Python?
     built-in Python function used to sort data

     sorted(iterable, key=None, reverse=False)
          iterable → list, tuple, set, dictionary, etc.
          key → function used for custom sorting
          reverse → False means ascending, True means descending
          sorted() does not change the original iterable

'''

print("\n ............. JMD ..............\n ");
numbers_list = [2,1,4,3,6,5,8,7,9]
sorted_numbers_list = sorted(numbers_list)

print('Original numbers list :' , numbers_list)
print('Sorted numbers list : ',sorted_numbers_list)

