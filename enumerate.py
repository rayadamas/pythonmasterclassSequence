# for index, character in enumerate("abcdefgh"):
#     print(index, character)


# the code above ^ is the shorthand version of what we're doing here
for t in enumerate("abcdefgh"):
    index, character = t
    print(index, character)

index, character = (0, 'a')
print(index)
print(character)
# index represents the index position as we progress through the loop
# character represents "abcdefgh" as we progress through the loop
