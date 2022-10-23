from asyncore import read
import os


class Archive:

    """Class with methods for manipulate files."""

    def __init__(self, file_name=str):
        self.file_name = file_name

        try:
            open(self.file_name, "r")
        except FileNotFoundError:
            open(f"{self.file_name}", "w+")
        else:
            pass

    def openRead(self):
        return open(f"{self.file_name}", "r")

    def openWrite(self):
        return open(f"{self.file_name}", "a")

    def openReadWrite(self):
        return open(f"{self.file_name}", "a+")

    def openReadWriteStart(self):
        return open(f"{self.file_name}", "r+")

    def openTruncate(self):
        return open(f"{self.file_name}", "w")

    @staticmethod
    def filterRead(file, filter=str, mode="inline"):

        file = file.readlines()
        for line in file:
            words = line.split()

            if mode == "inline":
                if filter not in words:
                    continue
                else:
                    print(line)

            elif mode == "not-inline":
                if filter in words:
                    continue
                else:
                    print(line)

    @staticmethod
    def createFile(fileName=str):
        try:
            open(fileName, "r")
        except:
            open(fileName, "w")
        else:
            print(f"\03331mThe file already exists\033[m")

    @staticmethod
    def deleteFile(fileName=str):
        try:
            os.remove(fileName)
        except:
            print(f"\033[31mError when trying to remove the file!")


def fileExists(name):

    """

    :param name: File name.
    :return: Return if the file exists.

    """

    try:
        file = open(name, "r")
        file.close()
    except FileNotFoundError:
        return False
    else:
        return True
