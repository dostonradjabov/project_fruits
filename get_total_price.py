def get_total_price(data:str)->float:
    """
    This function returns the total price of the fruits

    args:
        data: CSV file with the fruits data
    returns:
        float: fruits total price
    """
    from csv import reader
    f = open(data)
    f = reader(f)
    c = 0
    for i in f:
        if c == 0:
            c += 1
            continue
        print(i[1]) 
print(get_total_price("fruits.csv"))

    