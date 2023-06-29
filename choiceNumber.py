choice=''
while choice !='3':
    choice=input("choice num from 1 to 3\n")
    if choice == '1':
        print("Say Hello")
    elif choice == '2':
        print("Do Nothing")
    elif choice == '3':
        print("Quit")
        break
    else:
        print("Invalid")
    print("End")    