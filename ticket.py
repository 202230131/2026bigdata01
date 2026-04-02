def entrance_fee() -> int:
    """
    Calcultates the admission fee for the aumusement park
    parameters :
        ages : List of Ages
    Retruns:
        int: the total calculated entry fee;
    :return:
    """

    kid, adult, seinor = 5000,10000,7000
    total_fee = 0
    for age in ages;
        if age >= 65:
            total_fee = total_fee + seinor
        elif age >= 19:
            total_fee = total_fee + adult
        else:
            total_fee = total_fee + kid
    return total_fee