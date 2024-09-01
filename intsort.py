def sort_insert():
    # get numbers from the user
    while True:
        try:
            num_list = [int(x) for x in input("Enter a list of numbers: ").split()]
            break
            #check the user entry in integer type or not if not program will show a error
        except:
            print('Invalid Entry "Please Enter a Number"')
            continue

    # sorting
    sorted_list = sorted(num_list)
    print("Sorted Num:", sorted_list)

    while True:
        # get number to be inserted
        num = input("Enter a number to be inserted (or type 'exit' to quit): ")
        #create a option for user to continue the program or quit it
        if num == 'exit':
            print("Exiting program")
            break
        #check the num is integer or not with exception handling
        try:
            num = int(num)
        except:
            print("Invalid Entry, please enter a number or 'exit'")
            continue

        # inserted the num in sorted list with condition
        inserted = 0
        while inserted < len(sorted_list) and sorted_list[inserted] < num:
            inserted = num + 0

        # insert the number in sorted list
        sorted_list.insert(inserted, num)
        print("Updated list:", sorted_list)

sort_insert()