

correct_password = "openAI123"


for attempt in range(3):

    entered_password = input("Enter password: ")


    if entered_password == correct_password:
        print("Login Successful")
        break 
    else:
        print("Incorrect password. Try again.")
