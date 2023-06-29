import random
print(random.randint(1,10))

import random
Lucky_num=random.randint(1,10)
guess_no=None
while guess_no !=Lucky_num:
    guess_no=int(input("enter thenum from 1 to 10\n"))
    if guess_no < Lucky_num:
        print("too low")
    elif guess_no > Lucky_num:
        print("too high")
    print("found the number" + str(Lucky_num))