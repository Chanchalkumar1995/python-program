num=int(input("enter a int num\n"))
print("you have entered a num ->",str(num))
match num:
    case 0:
        print("you have entered 0")
    case x if x > 0:
            print("+ve number")
    case x if x < 0 :
             print("-ve number")
    case _:
        print("no Idea !!")
                