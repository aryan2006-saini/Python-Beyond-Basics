import json

x =  '{ "name":"John", "age":30, "city":"New York"}'
# parse x:
y = json.loads(x)
print(y)


data = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
# convert into JSON:
json_string = json.dumps(data)
# the result is a JSON string:
print(json_string)