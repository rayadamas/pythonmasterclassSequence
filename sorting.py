pangram = "The quick brown fox jumps over the lazy dog"

letter = sorted(pangram)
print(letter)

numbers = [2.3, 4.5, 8.7, 3.1, 9.2, 1.6]
sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)

numbers.sort()
print(numbers)

missing_letter = sorted("The quick brown fox jumped over the lazy dog", key=str.casefold)
# the `()` on casefold are omitted because we don't want to call the function
# instead, we want to tell the sorted function the name of ANOTHER function it should use when comparing the values
print(missing_letter)

names = ["John",
         "Paul",
         "eddie",
         "terry",
         "matt",
         "Rob"
         ]

names.sort(key=str.casefold)
print(names)