# JSON is a syntax for storing and exchanging data.
# JSON - JavaScript Object Notation
#
# JSON is text, written with JavaScript object notation.
# You can convert Python objects of the following types, into JSON strings:
#
# dict
# list
# tuple
# string
# int
# float
# True
# False
# None
import json

if __name__ == '__main__':
    # some JSON:
    x = '{ "name":"John", "age":30, "city":"New York"}'

    # parse x:
    y = json.loads(x)

    # the result is a Python dictionary:
    print(y["city"])
    print(type(y))

    # convert into JSON:
    y = json.dumps(y)

    print(type(y))
#
    print(json.dumps({"name": "John", "age": 30}))
    print(json.dumps(["apple", "bananas"]))
    print(json.dumps(("Nigeria", "Cameroon")))
    print(json.dumps("hello"))
    print(json.dumps(42))
    print(json.dumps(31.76))
    print(json.dumps(True))
    print(json.dumps(False))
    print(json.dumps(None))
#
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

    print(json.dumps(x, indent=3, separators=("; ", "->"), sort_keys=True))
#
# #     Result format
#     json.dumps(x, indent=4, separators=(". ", " = "))
#
# #     Order result
#     json.dumps(x, indent=4, sort_keys=True)
