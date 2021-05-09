def my_first_function():

    import random
    my_list = []
    MAX_LEN = 50
    for i in range (MAX_LEN):
        my_list.append(random.randint(1,99))
    print(my_list)
my_first_function()
import random
my_list = []
MAX_LEN = 50
for i in range (MAX_LEN):
    my_list.append(random.randint(1,99))
#print(my_list)
maximum = max(my_list)
print(maximum)
minimum = min(my_list)
print(minimum)
