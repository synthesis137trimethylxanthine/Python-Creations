print("Hi, thank you for accepting this questionnaire.")
print("Just to confirm some basic information.")

while True: 
    info_list = []
    age = input("What is your age? ")
    info_list.append(age) 

    name = input("What is your name? ")
    info_list.append(name)

    state = input("What state do you live in? ")
    info_list.append(state)

    print("Please confirm is this information accurate?")
    print(f"Age: {age}, Name: {name}, State: {state}")


    valid = ("yes", "no", "y", "n")

    
    while True: 
        answer = input("yes/no ")
        if answer.lower() in valid:
            break
        print("Please answer yes or no.") 
    if answer.lower() in ("no","n"): 
        print("Please try again")
    elif answer.lower() in("yes", "y"):
        break 
     

print("Thank you")











