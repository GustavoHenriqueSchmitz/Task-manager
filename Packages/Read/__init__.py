def readFile(name):

    """

    :param name: Name of file to read.
    :return: Nothing.

    """

    try:
        file = open(name, "r")
    except:
        print("Error while to read file!")
    else:
        fileRead = file.read()
        print(f"\n{fileRead}\n")
        file.close()


def readInteger(text="Integer number: "):

    """
    :param text: Text to be displayed in the input.
    :return: Return a integer value.
    """

    while True:
        try:
            value = int(input(text))
        except (TypeError, ValueError):
            print(f"\033[31mThe typed value is not an integer.\033[m")
            continue
        except (KeyboardInterrupt):
            print("\n\033[31mCanceled!\033[m")
            return
        else:
            return value


def readBinary(text="Binary number: "):

    """
    :param text: Text to be displayed in the input.
    :return: Return the binary value.
    """

    counter = 0
    while True:
        value = str(input(text)).strip().upper()
        for v in value:
            if v != "0" and v != "1" and v != "Q":
                counter += 1
        if counter > 0:
            print("\033[31m>>> The typed number is not binary !!!\033[m")
            counter = 0
        return value


def readMoney(text="Monetary value: "):

    """
    :param text: Text to be displayed in the input.
    :return: Return the value in the monetary type.
    """

    value = str(input(text)).strip()
    if value.replace(".", "").isnumeric() or value.replace(",", "").isnumeric():
        return float(value.replace(",", "."))
    while True:
        print(f'\033[31mError: "{value}" the value is not valid currency!\033[m')
        value = str(input(text)).strip()
        if value.replace(".", "").isnumeric() or value.replace(",", "").isnumeric():
            return float(value.replace(",", "."))


def readFloat(text="Float number: "):

    """
    :param text: Text to be displayed in input.
    :return: Return a float value.
    """

    while True:
        try:
            value = float(input(text))
        except (TypeError, ValueError):
            print(f"\033[31mThe typed value is not a float number.\033[m")
            continue
        except (KeyboardInterrupt):
            print("\n\033[31mCanceled!\033[m")
            return 0
        else:
            return value


def readResponse(text="Response: ", possibilities=1):

    """
    :param text: Text to be displayed in the input.
    :param possibilities: Maximum answers.
    :return: Return the response in a integer value.
    """

    while True:
        try:
            response = int(input(text))
        except:
            print("\033[31mError! Invalid response!\033[m")
        else:
            if response > possibilities or response <= 0:
                print("\033[31mError! Invalid response!\033[m")
                continue
            else:
                return response


def readResponseYN(text="Response: ", upperOrLower="lower"):

    """
    :param text: Text to be displayed in the input.
    :param upperOrLower: Defines whether the response is returned as uppercase or lowercase.
    :return: Return a value Y(YES) or N(NOT).
    """

    while True:
        response = str(input(text))
        if upperOrLower == "upper":
            if (
                response not in "S"
                and response not in "s"
                and response not in "n"
                and response not in "N"
            ):
                print("\033[Error! Type a valid value [Y/N]..\033[m")
                continue
            response = response.upper()
            if response == "S" or "N":
                return response
        if upperOrLower == "lower":
            if (
                response not in "S"
                or response not in "s"
                or response not in "n"
                or response not in "N"
            ):
                print("\033[Error! Type a valid value [Y/N]..\033[m")
                continue
            response = response.lower()
            if response == "s" or "n":
                return response
