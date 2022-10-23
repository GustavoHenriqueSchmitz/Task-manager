def row(lineSize=0):

    """
    :param lineSize: Size of the row.
    :return: Return a line.
    """

    return print("-" * lineSize)


def header(titleText="", linesSize=50):

    """
    :param titleText: Text of the header.
    :param linesSize: Size of the lines.
    :return: No return.
    """

    print("-" * linesSize)
    print(titleText.center(linesSize))
    print("-" * linesSize)


def menu(
    list,
    colorOne="\033[m",
    colorTwo="\033[m",
    displayOptions=True,
    title="Menu",
    linesSize=50,
    returnType="int",
):

    """
    :param list: List with the options.
    :param colorOne: The first color of the menu, must be defined by ANSI code.
    -> https://raccoon.ninja/pt/dev-pt/tabela-de-cores-ansi-python/
    :param colorTwo: The second color of the menu, must be defined by ANSI code.
    -> https://raccoon.ninja/pt/dev-pt/tabela-de-cores-ansi-python/
    :param displayOptions: Define if the options will be displayed or not.
    :param title: Title of the menu.
    :param linesSize: The lines size.
    :returnType: Define the return type of the function.
    Choosing int, the function returns the number of the choosed option, this is the default return type.
    Choosing str, the function returns the text of the choosed option.
    Choosing stint, the function returns the text and number of the choosed option.
    :return: Return the choosed option, the type is defined in the returnType parameter.
    """

    if displayOptions == True:
        print("-" * linesSize)
        print(f"{title:^{linesSize}}")
        print("-" * linesSize)
        for counter, item in enumerate(list):
            print(f"{colorOne}{counter + 1} - {colorTwo}{item}\033[m")
    while True:
        print("-" * linesSize)
        try:
            option = int(input(f"{colorOne}Option:\033[m "))
        except:
            print("\033[31mdigit a numeric option\033[m")
            continue
        if option > len(list) or option < 1:
            print("\033[31mdigit a valid option\033[m")
            continue
        else:
            if returnType.lower().strip() == "int":
                return option
            elif returnType.lower().strip() == "str":
                return list[option - 1]
            elif returnType.lower().strip() == "stint":
                return option, list[option - 1]


def displayOptions(
    list, colorOne="\033[m", colorTwo="\033[m", title="Menu", linesSize=50
):

    """
    :param list: List with the options.
    :param colorOne: The first color of the menu, must be defined by ANSI code.
    -> https://raccoon.ninja/pt/dev-pt/tabela-de-cores-ansi-python/
    :param colorTwo: The second color of the menu, must be defined by ANSI code.
    -> https://raccoon.ninja/pt/dev-pt/tabela-de-cores-ansi-python/
    :param title: Title of the menu.
    :param linesSize: The lines size.
    """

    print("-" * linesSize)
    print(f"{title:^linesSize}")
    print("-" * linesSize)
    for c, item in enumerate(list):
        print(f"{colorOne}{c + 1} - {colorTwo}{item}\033[m")
