# example = lambda x: x**1 if x%2 == 0 else x**2


# print(example(4))

nums = [1,2,3,4]


print(list(map(lambda x:x**2, nums)))



students = [
    {
        "id": 1,
        "name": "Alice",
        "age": 20,
        "marks": [80, 90, 85],
        "city": "Delhi"
    },
    {
        "id": 2,
        "name": "Bob",
        "age": 22,
        "marks": [70, 75, 80],
        "city": "Mumbai"
    },
    {
        "id": 3,
        "name": "Charlie",
        "age": 21,
        "marks": [95, 90, 98],
        "city": "Hyderabad"
    },
    {
        "id": 4,
        "name": "David",
        "age": 23,
        "marks": [60, 65, 70],
        "city": "Chennai"
    }
]

print((list(map(lambda x:x['name'],students))))