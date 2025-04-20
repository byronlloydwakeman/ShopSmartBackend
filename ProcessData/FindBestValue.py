from ProcessData.FindUnit import *
from ProcessData.Compare import *
from ProcessData.Convert import *

def TescoFindBestValue(data):
    """
    Data is an array of lots of different tesco items, we need to put the cost/measurement into a standard format,
    then return the one with the lowest cost per measurement value
    :param data: An array of objects in format {"name", "price", "image", "value"}
    :return: The best value item
    """
    # Get array of most common array
    commonArray = FindCommonUnit(data)

    bestValue = min(commonArray, key=lambda x: float(x["value"].split('/')[0].strip('£')))
    return bestValue

def WaitroseFindBestValue(data):
    """
    Input an array of common units e.g (["£1.97/litre", "72.9p/litre"]) and find the cheapest value
    :param data: An array of objects in format {"name", "price", "image", "value"}
    :return: return the object with the best value, An array of objects in format {"name", "price", "image", "value"}
    """
    # Get array of most common array
    common_array = FindCommonUnit(data)

    #Convert all values to pound
    pound_values = PenceToPound(common_array)

    best_value = min(pound_values, key=lambda x: float(x["value"].split('/')[0].strip('£')))

    return best_value

