import enum

def FindValuesUnit(data):
    """
    Takes a value such as 50p/each. We then return the enum value of the measurement.
    :param data: A value as a string e.g "10p/100g"
    :return: A string value of the respective unit e.g "100g"
    """
    def find_match(string):
        for item in ["each", "100g", "litre", "lt", "100ml", "kg"]:
            if item.lower() in string.lower():
                return item
        raise Exception("Invalid unit found: " + data)

    unit = find_match(data)

    return unit

def FindCommonUnit(data):
    """
    The search resutls might have different units which will be difficult to compare
    e.g 68p/100g or 21p/each
    So we can find the most common unit and assume that as the most important
    :param data: Array of items
    :return: Array of items with the common unit
    """
    dictCount = {"each": [], "100g": [], "litre": [], "lt": [], "100ml": [], "kg": []}
    for el in data:
        unit = FindValuesUnit(el["value"])
        dictCount[unit].append(el)

    item_with_max_count = max(dictCount, key=lambda x: len(dictCount[x]))

    # Find the longest array and return it
    return dictCount[item_with_max_count]


