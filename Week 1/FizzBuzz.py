

def fizzbuzz(n):

    for i in range(1, n + 1):

        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")

        elif i % 3 == 0:
            print("Fizz")

        elif i % 5 == 0:
            print("Buzz")

        else:
            print(str(i)) 


user_input = input("Enter a number: ")


n = int(user_input)


fizzbuzz(n)

