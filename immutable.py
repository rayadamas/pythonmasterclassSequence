# result = True
# another_result = result
# print(id(result))
# print(id(another_result))

# id() returns the identity of an object, it will be unique & constant for the objects lifetime
# will change each time program is run

# result = False
# print(id(result))

result = "Correct"
another_result = result
print(id(result))
print(id(another_result))

result += "ish"
print(id(result))