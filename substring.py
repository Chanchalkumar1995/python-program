
if 'x' in 'xyz':
    print(True)
 #another program   
    string =input("enter a string\n")
    substring="chan"
    match string:
        case x if substring in x:
            print("present")
        case _:
         print("Not present")