testdict = {  # Creating a dictionary
    "brand": "apple", # Key: brand, Value: apple
    "ram": "3", # Key: ram, Value: 3
    "year": "2020",# Key: year, Value: 2020
    "year": "2021" # Key: year, Value: 2021 (This will overwrite the previous year key)
} # End of dictionary

print(testdict.keys()) # Output: dict_keys(['brand', 'ram', 'year'])
print(testdict.values()) # Output: dict_values(['apple', '3', '2021'])
print(testdict.items()) # Output: dict_items([('brand', 'apple'), ('ram', '3'), ('year', '2021')])
