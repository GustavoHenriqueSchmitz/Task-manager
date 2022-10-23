import string


def increase(price=0, rate=0, format=False):

    """
    :param price: Monetary price.
    :param rate: Rate% of increase.
    :param formato: Define if it will be formated (True) or not (False).
    :return: Return the increased value.
    """

    response = price + (price * rate / 100)
    return (
        response
        if format is False
        else (f"{response}{price:>.2f}".replace(".", ","))
        if response == "R$"
        else (f"{response}{price:>.2f}".replace(",", "."))
    )


def decrease(price=0, rate=0, format=False):

    """
    :param price: Monetary price.
    :param rate: Rate% of decrease.
    :param format: Define if it will be formated (True) or not (False).
    :return: Return the decreased value.
    """

    response = price - (price * rate / 100)
    return (
        response
        if format is False
        else (f"{response}{price:>.2f}".replace(".", ","))
        if response == "R$"
        else (f"{response}{price:>.2f}".replace(",", "."))
    )


def double(price=0, format=False):

    """
    :param price: Monetary price to be doubled.
    :param format: Define if it will be formated (True) or not (False).
    :return: Return the doubled value.
    """

    response = price * 2
    return (
        response
        if format is False
        else (f"{response}{price:>.2f}".replace(".", ","))
        if response == "R$"
        else (f"{response}{price:>.2f}".replace(",", "."))
    )


def half(price=0, format=False):

    """
    :param price: Monetary price.
    :param format: Define if it will be formated (True) or not (False).
    :return: Return the value in half.
    """

    response = price / 2
    return (
        response
        if format is False
        else (f"{response}{price:>.2f}".replace(".", ","))
        if response == "R$"
        else (f"{response}{price:>.2f}".replace(",", "."))
    )


def convertCoin(price=0, coin="R$"):

    """
    :param price: Monetary price.
    :param coin: Coin type.
    :return: Return the formated price.
    """

    return (
        (f"{coin}{price:>.2f}".replace(".", ","))
        if coin == "R$"
        else (f"{coin}{price:>.2f}".replace(",", "."))
    )
