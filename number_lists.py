empty_list = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = [even, odd]
print(numbers)


for number_list in numbers:
    print(number_list)

    for value in number_list:
        print(value)









# sorted_numbers = sorted(numbers)
# print(sorted_numbers)
# print(numbers)
#
# digits = sorted("432985617")
# print(digits)
#
# # more_numbers = list(numbers)
# # more_numbers = numbers[:]
# more_numbers = numbers.copy()
# print(more_numbers)
# print(numbers is more_numbers)
# print(numbers == more_numbers)










# even.extend(odd)
# print(even)
#
# print(80 * "-")
#
# another_even = even
# print(another_even)
#
# even.sort()
# print(even)
#
# print(80 * "-")
#
# even.sort(reverse=True)
# print(even)
# print(another_even)
#
#


# print(min(even))
# print(max(even))
# print(min(odd))
# print(max(odd))
#
# print(80 * "-")
#
# print(len(even))
# print(len(odd))
#
# print(80 * "-")
#
# print("mississippi".count("s"))
#
# print(80 * "-")
#
# print("mississippi".count("iss"))
#
# print(80 * "-")
#
# print("mississippi".count("issi"))