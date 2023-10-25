def get_cheapest_fruit(data: str) -> str:
    """
    This function returns the name of the cheapest fruit

    args:
        data: CSV file with the fruits data
    returns:
        str: name of the cheapest fruit
    """
    # your code here
    from csv import reader
    f = open(data)
    a = []
    for i in f:
        a.append(i[1:])
    return tuple(i[0:]) 
print(get_cheapest_fruit("fruits.csv"))