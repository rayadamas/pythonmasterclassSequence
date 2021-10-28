flowers = [
    "Daffodil",
    "Evening Primrose",
    "Hydrangea",
    "Iris",
    "Lavender",
    "Sunflower",
    "Tiger Lily",
]

# for flower in flowers:
#     print(flower)

separator = ", "
output = separator.join(flowers)# .join() is iterating over the list for us w/o a for loop
print(output)

#all the items in the iterable must be STRINGS if you want to join them