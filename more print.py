name = "Diamond"
age = 10

print(name, age, "Python", 2020)
print(name, age, "Python", 2020, sep=", ")



customers = ['John', 'Natasha', 'Eric', 'Sally']

for i, customer in enumerate(customers, 1):
    print("{}: {}".format(i, customer))
