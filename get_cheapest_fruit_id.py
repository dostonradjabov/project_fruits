def get_cheapest_fruit_id(data: str) -> int:
    """
    This function returns the index of the cheapest fruit

    args:
        data (str): CSV file with the fruits data
    returns:
        int: id of the cheapest fruit
    """
    # your code here
    from csv import reader
    f = open(data)
    a = []
    for i in f:
         a.append(i[:])
    return tuple(a[1:2])  
print(get_cheapest_fruit_id("fruits.csv"))