import json

data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

serialized_data = json.dumps(data)  # Serialize data to JSON string
print(serialized_data)



# deserialized_data = json.loads(serialized_data)  # Deserialize JSON string to Python data
# print(deserialized_data)



