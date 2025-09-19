

prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


middle_five = prime_numbers[2:7]


every_second = prime_numbers[::2]


last_three = prime_numbers[-3:]


reversed_list = prime_numbers[::-1]


descending_order = sorted(prime_numbers, reverse=True)


print("Middle Five Primes:", middle_five)
print("Every Second Prime:", every_second)
print("Last Three Primes:", last_three)
print("Reversed List:", reversed_list)
print("Descending Order:", descending_order)
