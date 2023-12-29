import json

x = '{"name": "Chandu", "age": 30, "city": "hyderabad"}'
p = {"name": "Chandu", "age": 30, "city": "hyderabad"}
y = json.loads(x)

# print(x["age"])
print(y["age"])

q = json.dumps(p)

print(q)
print(type(q))

x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}
# Sorting by keys
# print(dict(sorted(x.items())))
# Sorting by values
y = dict(sorted(x.items(), key=lambda item: str(item[1])))
print(y)


# print(json.dumps(x))
# print(json.dumps(x, indent=4, sort_keys=True))
# print(type(x))

# =========================================================
# Sorting Dict without using builtin methods


def sorting_dict_with_out_builtin_method(input_dict):
    # Extract Key and values as lists
    keys = list(input_dict.keys())
    values = list(input_dict.values())
    n = len(keys)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if keys[j] > keys[j + 1]:
                keys[j], keys[j + 1] = keys[j + 1], keys[j]
                values[j], values[j + 1] = values[j + 1], values[j]

    sorted_dict = {}

    for k, v in zip(keys, values):
        sorted_dict[k] = v
    return sorted_dict


sd = sorting_dict_with_out_builtin_method(x)
print("Sorted Dict : ",sd)
