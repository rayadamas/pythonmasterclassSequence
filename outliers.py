# data = [4, 5, 104, 105, 110, 120, 130, 130, 150,
#         160, 170, 183, 185, 187, 188, 191, 350, 360]

# Test 1 only removing items from the start of the list
# data = [4, 5, 104, 105, 110, 120, 130, 130, 150,
#         160, 170, 183, 185, 187, 188, 191]

# Test 2 only outlying values at the end of the list
# data = [104, 105, 110, 120, 130, 130, 150,
#         160, 170, 183, 185, 187, 188, 191]

# Test 3 when there are no outlying values
# data = [104, 105, 110, 120, 130, 130, 150,
#         160, 170, 183, 185, 187, 188, 191]

# Test 4 a list with no values in the desire range
# data = [1041, 1051, 1101, 1201, 1301, 1301, 1501,
#         1601, 1701, 1831, 1851, 1871, 1881, 1911]

# Test 5 an empty data set
data = [69]

# del data[0:2]
# print(data)
#
# del data[14:]
# print(data)

min_valid = 100
max_valid = 200

# process the low values in the list
stop = 0
for index, value in enumerate(data):
    if value >= min_valid:
        stop = index
        break

print(stop)
del data[:stop]
print(data)


# process the high values in the list
start = 0
for index in range(len(data) - 1, - 1, - 1):
    if data[index] <= max_valid:
        # we have the index of the last item to keep
        # set `start` to the position of the first
        # item to delete, which is 1 after `index`
        start = index + 1
        break

print(start) # for debugging
del data[start:]
print(data)