def ValidateSupermarketLocation(targetSupermarket, supermarketModel):
    """
    This function checks that the given supermarket recieved from the yelp api is the one we're looking for
    :param supermarketModel:
    :return:
    """
    # If there are no entries
    if(len(supermarketModel) == 0):
        return False

    if targetSupermarket in supermarketModel[0]["name"]:
        return True
    else:
        return False

