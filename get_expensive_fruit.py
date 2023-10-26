def get_expensive_fruit(data: str) -> str:
    """
    This function returns the name of the most expensive fruit

    args:
        data: CSV file with the fruits data
    returns:
        str: name of the most expensive fruit
    """
    # your code here
    data  = data.split()
    mx = 0
    for i in data[1:]:
        p = float(i.split(",")[1])
        n = i.split(",")[0]
        if mx<p:
            k = n
            mx = p
    return k
data = open("fruits.csv").read()
print(get_expensive_fruit(data))



