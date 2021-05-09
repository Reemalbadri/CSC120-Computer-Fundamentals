import random
my_randoms = []
len(my_randoms)
for i in range(50):
    if len(my_randoms) < 5:
        my_randoms.append(random.randrange(1, 100))
        number = random.randint(1,100)
    print("New:" + str(number))
    print(sorted(my_randoms))

#else:
    #my_randoms_list = my_randoms = []
    #number > my_randoms_list
    #my_randoms.replace(min(my_randoms))
    #print(sorted(my_randoms))
