if __name__ == '__main__':
    dict = {"fruit": "apple", "color": "orange", "country": "Nigeria", "year": 1997, "scores": [60, 80, 20]}

    # Accessing dictionaries
    year = dict.get("year")
    scores = dict.get("scores")
    values = dict.values()
    keys = dict.keys()
    print(year)
    print(values)
    print(keys)
    print(type(scores))

    # update
    dict.update({"year": 2022})
    dict["year"] = 2002
    scores[2] = 75
    print(dict)

    # remove
    dict.pop("country")
    print(dict)

    # loop
    for x, y in dict.items():
        print(x, y)

    for x in dict.keys():
        print(x)

    for y in dict.values():
        print(y)


