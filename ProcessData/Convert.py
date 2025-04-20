def PenceToPound(values):
    """
    Convert all 'values' to pound values,
    :param values: common values array, [{"name": "milk", "price": "£1.33", "image": "", "value" : '£2.10/litre'},]
    :return: the same array of values but the "value" property is in pounds
    """
    for obj in values:
        if "p" in obj["value"]:
            pound_value = format(float(obj["value"].split("/")[0].strip("p")) / 100, ".2f")
            obj["value"] = "£" + str(pound_value) + "/" + obj["value"].split("/")[1]

    return values
