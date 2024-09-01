try:
    inp= int(input("Please enter any number:"))
    print("Your entered number is:",inp)
except Exception as e:
    print("please enter a number")
    print(e)